# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack_repo.builtin.packages.esmf.package import Esmf as BuiltinEsmf
from spack_repo.builtin.packages.esmf.package import MakefileBuilder as BuiltinMakefileBuilder

from spack.package import *


class Esmf(BuiltinEsmf):
    """ESMF as used by E3SM tools: the upstream recipe without the run-time
    dependency on a Spack-built python, plus NetCDF and oneAPI build fixes for
    E3SM-supported machines."""

    maintainers("xylar", "andrewdnolan")


# Upstream esmf@8.4.0: declares run-time dependencies on python and py-pyyaml
# for ESMX, which E3SM does not use.  A Spack-built python in the environment
# view would shadow the conda/pixi python that E3SM software runs with, so drop
# those two dependencies.  Directives are inherited and cannot be removed by a
# subclass, so this edits the dependency table after the class is created.
_ESMX_WHEN = "@8.4.0:"
for _when, _deps in Esmf.dependencies.items():
    if str(_when) == _ESMX_WHEN:
        for _name in ("python", "py-pyyaml"):
            _deps.pop(_name, None)


def _oneapi_gcc_lib64(cxx):
    """Return the lib64 directory of the GCC toolchain that icpx uses."""
    cfg_file = cxx + ".cfg"
    if os.path.exists(cfg_file):
        with open(cfg_file) as f:
            match = re.search(r"--gcc-toolchain=(\S+)", f.read())
        if match:
            lib64 = os.path.join(match.group(1), "lib64")
            if os.path.exists(lib64):
                return lib64
    # Spack's Executable rather than subprocess.run(capture_output=...):
    # Spack runs under the login shell's python, which may be 3.6
    try:
        output = Executable(cxx)("--print-file-name=libstdc++.so", output=str, error=str)
    except (OSError, ProcessError):
        return None
    libstdcxx = os.path.realpath(output.strip())
    if os.path.isabs(libstdcxx):
        return os.path.dirname(libstdcxx)
    return None


class MakefileBuilder(BuiltinMakefileBuilder):
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        super().setup_build_environment(env)
        spec = self.spec

        # On these machines, nc-config and nf-config from the system NetCDF
        # modules do not report the right --libs and --flibs, so point ESMF at
        # the netcdf-c prefix directly.
        if (
            os.environ.get("NERSC_HOST", "") == "perlmutter"
            or os.environ.get("HOST", "").startswith("ch-fe")
            or os.environ.get("LMOD_SYSTEM_NAME", "") == "frontier"
        ):
            env.set("ESMF_NETCDF", "split")
            env.set("ESMF_NETCDF_LIBPATH", spec["netcdf-c"].prefix.lib)
            env.set("ESMF_NETCDF_INCLUDE", spec["netcdf-c"].prefix.include)

        # With oneAPI (icpx/ifx), ifx's -cxxlib resolves libstdc++ from the
        # system GCC rather than from the GCC toolchain configured in the
        # compiler's .cfg files.  ESMF's F90 app link step uses
        # ESMF_F90LINKPATHS for -L flags, so adding the toolchain's lib64
        # there makes the right libstdc++ get found.
        if spec["cxx"].name == "intel-oneapi-compilers":
            gcc_lib64 = _oneapi_gcc_lib64(spec["cxx"].package.cxx)
            if gcc_lib64:
                env.set("ESMF_F90LINKPATHS", "-L%s" % gcc_lib64)
