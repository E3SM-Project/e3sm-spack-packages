# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.parmetis.package import Parmetis as BuiltinParmetis

from spack.package import *


class Parmetis(BuiltinParmetis):
    """ParMETIS with a ``pic`` variant, so its static library can be linked
    into shared libraries, as Trilinos does in Polaris's Albany environments."""

    maintainers("xylar", "andrewdnolan")

    variant(
        "pic",
        default=False,
        description="Build position-independent code, so the static library "
        "can be linked into shared libraries",
    )

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"))
        return args
