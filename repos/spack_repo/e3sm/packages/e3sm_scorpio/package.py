# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.e3sm_scorpio.package import E3smScorpio as BuiltinE3smScorpio

from spack.package import *


class E3smScorpio(BuiltinE3smScorpio):
    """SCORPIO with releases newer than the pinned upstream package and a fix
    for the Cray Fortran compiler."""

    maintainers("xylar", "andrewdnolan")

    version("2.0.3", sha256="ff9570e250e6b75b723b778b17453d9bcc88d2a66674f1bcb0aaab65f321ff60")
    version("2.0.2", sha256="68444fd641363388d0d06528ce7d9d0b33df3ae6103df122973d9963476e3319")
    version("2.0.1", sha256="0a4006fd6f2ce03acbe0f69726cedb32bc1e0dfb5e170e9f8d7201c1125dbc99")
    version("2.0.0", sha256="d82d0c5db34b4d83de0d40130340ad286432b00764d27f4694626e44c525ea80")
    version("1.9.3", sha256="dfa3b4141c41ddaabc24ebe89660bfdf7db9fd5daea98e1b02224448fe363316")
    version("1.9.2", sha256="d1dafd5a62b6b8ef9c325db686cecf825478dffb9d648d970a6258f903dcc251")
    version("1.9.1", sha256="b26c9bde4b041e706b81a83fca30d12c3708d2fe89058eab81611ad38cf0c74f")
    version("1.9.0", sha256="76373ee65f4bc562b8e52acc5d22cc725f36b9a3a679f7ee413a38ee25d6b2b9")
    version("1.8.2", sha256="1acafe152482d1c083dec0e3fea9484f844e5ac1e67065cbd02d31aff5e740ff")

    def cmake_args(self):
        args = super().cmake_args()
        if self.spec["fortran"].name == "cce":
            # force lowercase fortran modules
            args.append(self.define("CMAKE_Fortran_FLAGS", "-em -ef"))
        return args
