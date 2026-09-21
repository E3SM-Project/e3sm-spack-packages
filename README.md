# e3sm-spack-packages

A [Spack](https://spack.io) package repository (namespace `e3sm`) with the
packages that E3SM tools need beyond what the `builtin` repository from
[spack/spack-packages](https://github.com/spack/spack-packages) provides.
[mache](https://github.com/E3SM-Project/mache) registers it ahead of `builtin`
when it builds Spack environments, so a package here shadows the upstream
package of the same name.

## Using it

Register the repository ahead of `builtin` in a Spack 1.x instance:

```bash
git clone https://github.com/E3SM-Project/e3sm-spack-packages.git
spack repo add --scope site e3sm-spack-packages/repos/spack_repo/e3sm
spack repo list   # e3sm must be listed before builtin
```

## Packages

Packages that exist upstream subclass the upstream recipe and carry only the
E3SM delta. Each is deleted here once the pinned `builtin` release provides it.

| Package | Why it is here | Upstream |
|---------|----------------|----------|
| `albany` | E3SM-only: Albany land-ice model with compass tags and variants | not upstream |
| `trilinos-for-albany` | E3SM-only: Trilinos configured for Albany | not upstream |
| `e3sm-scorpio` | versions 1.8.2–2.0.3; lowercase Fortran modules with `cce` | PR pending |
| `esmf` | drops the run-time `python`/`py-pyyaml` dependencies (ESMX), which would put a Spack python in the view; NetCDF `split` mode on Perlmutter, Chicoma and Frontier; `libstdc++` link path with oneAPI | E3SM-specific |
| `moab` | constrains `eigen` to 3.x; MOAB 5.6.0 does not build against Eigen 5 (C++14) | PR pending |
| `netcdf-c` | version 4.10.1 | PR pending |
| `netcdf-fortran` | version 4.6.3 | PR pending |
| `parallel-netcdf` | version 1.15.0 | PR pending |
| `tempestextremes` | versions 2.4, 2.4.1, 2.4.2 | PR pending |
| `tempestremap` | grid-element tolerance patch for high-resolution meshes in mbtempest; missing `c` build dependency | patch E3SM-specific; `c` dependency PR pending |

Not carried over from the retired `E3SM-Project/spack` fork: `nco`,
`netcdf-fortran` 4.6.2, `hdf5`, `visit` and the `trilinos` cmake bump are
upstream at the versions E3SM uses; the `boost` and `rhash` patches were for
Intel classic compilers, which mache no longer supports; `superlu` shared
libraries were only needed for Albany `+optimization`, which E3SM does not
build.

## Tested against

The `concretize` job in CI concretizes every package and every spec in
[`ci/specs.txt`](ci/specs.txt), which mirrors what E3SM-Unified, compass and
polaris request, for each pair in [`ci/versions.yaml`](ci/versions.yaml):

| Spack | spack-packages (`builtin`) |
|-------|----------------------------|
| v1.2.2 | v2026.06.0 |

The `install` job builds the cheaper packages weekly and on request.

## Tags

Tags are `vYYYY.MM.N`, where `YYYY.MM` is the oldest `builtin` release in
`ci/versions.yaml` at the time of tagging and `N` counts tags for that era
from zero. Tags are independent of mache releases; each mache release records
the tag it uses in its own `pins.yaml`.

## Contributing

- Directory names use the v2 convention (`trilinos_for_albany`).
- Import build systems from `spack_repo.builtin.build_systems` and upstream
  packages from `spack_repo.builtin.packages.<name>.package`; import nothing
  else from `spack.*` other than `spack.package`.
- Extend an upstream package by subclassing it, not by copying it. A change
  inside a builder is made with a builder subclass named after the build
  system in the same module.
- Every package lists `maintainers("xylar", "andrewdnolan")` plus the
  package's upstream owner.
- A version or fix that is not E3SM-specific is submitted upstream when it is
  added here.
- Style follows spack-packages: `ruff format` and `ruff check` with the
  configuration in `pyproject.toml` (`pip install -r ci/requirements.txt`).

## License

This repository is licensed under the BSD 3-Clause License (see
[LICENSE](LICENSE)). Files derived from spack-packages, including subclass
modules that reuse upstream code, keep their upstream header and are
`SPDX-License-Identifier: (Apache-2.0 OR MIT)`; E3SM-authored files carry a
BSD 3-Clause header.
