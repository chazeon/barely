# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
- nothing

## [1.0.4] - 2021-09-06
### Added
- "--desktop" flag for lighthouse (default is mobile)

### Fixed
- autoSEO: no longer crashes when no image can be found; ignores modular subpages
- pixelizer: save original image without blowing up its size
- minify: configuring minify no longer disables it
- toc: don't generate tocs for modular subpages
- highlight: regex non-greedy, previously wrong behaviour when multiple code blocks on a page; eliminated duplicate stylesheet generation

### Changed
- enabled git plugin by default
- higher resilience against errors (non-critical errors get logged instead of excepted)
- autoSEO: use site_name as fallback for title
- highlight: accepts more conventional / markdown-style lexer notation; un-escape code before highlighting
- collections: category & overview pages now passed through enabled plugins; use summary as preview, if it exists; preview-image does no longer have to be in the same directory

## [1.0.3] - 2021-09-01
### Fixed
- faulty system blueprints path made barely unable to find any bleuprints

### Changed
- to ensure at least somewhat "unique" alt-tags in galleries, include the number-position of the image in the gallery
- original/fallback images will no longer be processed by PIL in the Pixelizer plugin, but rather just be copied; their filesizes got blown up before, and the step was needless anyways

## [1.0.2] - 2021-08-27
### Changed
- clean up raw_content before AutoSummary consumes it

### Fixed
- robots.txt no longer weirdly indented
- sitemap generation now works after fixing a typo (hmtl -> html)

## [1.0.0] - 2021-08-26
### Added
- lighthouse CLI integration
- AutoSEO plugin
- AutoSummary plugin
- Gallery plugin
- Minify plugin
- Pixelizer plugin
- global `-d` debugging-flag
- this changelog!

### Changed
- moved from BETA to STABLE
- switched version numbering scheme from `v_095` to more readable `v1.0.0`
- proper logging instead of print()
- simplified the default blueprint to make it more usable

### Fixed
- various small performance improvements, largely due to eliminating duplicate function calls

### Removed
- Minimizer plugin, obsolete thanks to Minify and Pixelizer

## [0.9.5] - 2021-07-19
### Added
- `-l` flag for light rebuilds (no re-rendering of images, preserves webroot)
- `-s` flag to start the live server after a rebuild

### Fixed
- bugs preventing forms and collections from being compiled correctly
- unability to render an item no longer crashes barely

## [0.9.0] - 2021-06-19
Initial beta release

[Unreleased]: https://github.com/charludo/barely/compare/v1.0.4...HEAD
[1.0.4]: https://github.com/charludo/barely/compare/v1.0.3...v1.0.4
[1.0.3]: https://github.com/charludo/barely/compare/v1.0.2...v1.0.3
[1.0.2]: https://github.com/charludo/barely/compare/v1.0.0...v1.0.2
[1.0.0]: https://github.com/charludo/barely/compare/v_095...v1.0.0
[0.9.5]: https://github.com/charludo/barely/compare/v_090...v_095
[0.9.0]: https://github.com/charludo/barely/releases/tag/v_090
