# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.netcdf_c.package import NetcdfC as BuiltinNetcdfC

from spack.package import *


class NetcdfC(BuiltinNetcdfC):
    """NetCDF-C with releases newer than the pinned upstream package."""

    maintainers("xylar", "andrewdnolan")

    version("4.10.1", sha256="33c27231c478c3b35da7c7758fbdd02da1fe407abcb16ddfe195f69d164f930d")
