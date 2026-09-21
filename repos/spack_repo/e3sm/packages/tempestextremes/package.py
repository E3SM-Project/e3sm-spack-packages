# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.tempestextremes.package import (
    Tempestextremes as BuiltinTempestextremes,
)

from spack.package import *


class Tempestextremes(BuiltinTempestextremes):
    """TempestExtremes with releases newer than the pinned upstream package."""

    maintainers("xylar", "andrewdnolan")

    version("2.4.2", sha256="a370faadfe3958ed0db7bfab8ca0fcd50bbc91b11aeba3dff8728d0fb0f94267")
    version("2.4.1", sha256="c586739a62e3a8d8cc41cd2f17130825806b8bd618df25e9ac26a0ce0bd72016")
    version("2.4", sha256="c1be592ae5e1975c64f65025149d9c3f7b83474fcfe67ef3d5bb7206e63b4b6a")
