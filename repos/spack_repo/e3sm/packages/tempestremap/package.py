# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.tempestremap.package import Tempestremap as BuiltinTempestremap

from spack.package import *


class Tempestremap(BuiltinTempestremap):
    """TempestRemap with the grid-element tolerance relaxed for the
    high-resolution meshes used with mbtempest."""

    maintainers("xylar", "andrewdnolan")

    # configure runs AC_PROG_CC, so a C compiler is needed as well as C++
    depends_on("c", type="build")

    # Relax tolerance for valid grid elements, needed by high resolution meshes
    # in mbtempest
    patch("grid_elements_tolerance.patch", when="@2.2.0")
