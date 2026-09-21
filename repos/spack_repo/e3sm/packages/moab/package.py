# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.moab.package import Moab as BuiltinMoab

from spack.package import *


class Moab(BuiltinMoab):
    """MOAB with Eigen constrained to 3.x: MOAB's build does not enable the
    C++14 that Eigen 5 requires."""

    maintainers("xylar", "andrewdnolan")

    depends_on("eigen@:3", when="+eigen")
