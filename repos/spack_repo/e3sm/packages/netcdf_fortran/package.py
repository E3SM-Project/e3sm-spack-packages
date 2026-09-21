# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.netcdf_fortran.package import (
    NetcdfFortran as BuiltinNetcdfFortran,
)

from spack.package import *


class NetcdfFortran(BuiltinNetcdfFortran):
    """NetCDF-Fortran with releases newer than the pinned upstream package."""

    maintainers("xylar", "andrewdnolan")

    version("4.6.3", sha256="f642050e90025e7bb25848cc8f818545e1d3bdeb73fe6d103a6f8dc000a1a3d6")
