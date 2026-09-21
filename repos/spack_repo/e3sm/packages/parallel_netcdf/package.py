# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.parallel_netcdf.package import (
    ParallelNetcdf as BuiltinParallelNetcdf,
)

from spack.package import *


class ParallelNetcdf(BuiltinParallelNetcdf):
    """PnetCDF with releases newer than the pinned upstream package."""

    maintainers("xylar", "andrewdnolan")

    version("1.15.0", sha256="39813fe91ec901c7cfca3212731edbb5201029ebf55caeaaaa08d9e33c6bad65")
