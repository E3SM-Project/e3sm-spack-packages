# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.netcdf_c.package import (
    AutotoolsBuilder as BuiltinAutotoolsBuilder,
)
from spack_repo.builtin.packages.netcdf_c.package import NetcdfC as BuiltinNetcdfC

from spack.package import *


class NetcdfC(BuiltinNetcdfC):
    """NetCDF-C with releases newer than the pinned upstream package."""

    maintainers("xylar", "andrewdnolan")

    version("4.10.1", sha256="33c27231c478c3b35da7c7758fbdd02da1fe407abcb16ddfe195f69d164f930d")


class AutotoolsBuilder(BuiltinAutotoolsBuilder):
    def configure_args(self):
        config_args = super().configure_args()

        if any(self.spec.satisfies(s) for s in ["+mpi", "+parallel-netcdf", "^hdf5+mpi~shared"]):
            # MPICH-based MPIs define MPI_Comm_f2c and MPI_Info_f2c as macros, which the
            # configure script's link test misses. Starting with 4.10.1, this is a hard error.
            # See https://github.com/Unidata/netcdf-c/issues/3414
            config_args.extend(["ac_cv_func_MPI_Comm_f2c=yes", "ac_cv_func_MPI_Info_f2c=yes"])

        return config_args
