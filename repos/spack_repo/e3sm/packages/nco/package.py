# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.nco.package import Nco as BuiltinNco

from spack.package import *


class Nco(BuiltinNco):
    """NCO with releases newer than the pinned upstream package."""

    maintainers("xylar", "andrewdnolan")

    version("5.4.1", sha256="1908416c4c8c8754f48b797d1030ac847e07d7e49a6d5bf455bdee7808409aad")
    version("5.4.0", sha256="c6e03cacbde7eae908eabfe65b2c1edc7b1754e07597b8f7fe2fc894f21b2dca")
