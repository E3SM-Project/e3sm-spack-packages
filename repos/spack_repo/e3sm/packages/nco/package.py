# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.nco.package import Nco as BuiltinNco

from spack.package import *


class Nco(BuiltinNco):
    """NCO with releases newer than the pinned upstream package."""

    maintainers("xylar", "andrewdnolan")

    version("5.4.0", sha256="c6e03cacbde7eae908eabfe65b2c1edc7b1754e07597b8f7fe2fc894f21b2dca")
