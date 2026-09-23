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

    def configure_args(self):
        args = super().configure_args()

        # Starting 1.15.0, configure adds '-fvisibility=hidden' to FFLAGS and
        # FCFLAGS if the Fortran compiler accepts it. GNU Fortran ignores the
        # flag but Intel ifx honors it and also marks *undefined* references
        # (e.g. all the nfmpi_* calls made from the Fortran 90 module) as
        # hidden. When libpnetcdf.so is linked, the linker applies the most
        # restrictive visibility, which hides the whole Fortran API and
        # breaks linking of the Fortran benchmarks (and of user programs).
        # The Fortran bindings contain nothing but the public API, so there
        # is nothing to hide there. Tell configure the flag is not supported.
        if self.spec.satisfies("@1.15:+fortran"):
            args.append("ax_cv_check_fcflags___fvisibility_hidden=no")

        return args
