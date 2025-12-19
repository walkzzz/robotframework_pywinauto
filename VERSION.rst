VERSION.rst
==========

Version History
==============

This document describes the version history and versioning policy of robotframework-pywinauto.

Versioning Policy
================

robotframework-pywinauto follows `Semantic Versioning <https://semver.org/>`_ (SemVer 2.0.0),
which means that version numbers are in the format ``MAJOR.MINOR.PATCH``:

- **MAJOR version**: Incremented for incompatible API changes
- **MINOR version**: Incremented for backwards compatible new features
- **PATCH version**: Incremented for backwards compatible bug fixes

Release Types
=============

- **Stable Release**: Version numbers like ``1.0.0`` - ready for production use
- **Release Candidate (RC)**: Version numbers like ``1.0.0rc1`` - almost ready for production, intended for final testing
- **Beta Release**: Version numbers like ``1.0.0b1`` - feature complete but may have bugs
- **Alpha Release**: Version numbers like ``1.0.0a1`` - early release with incomplete features

Supported Versions
==================

We typically support the latest stable release and the previous major release.
For each supported release, we provide:

- Bug fixes
- Security updates
- Documentation updates

End of Life (EOL) Policy
========================

A release reaches EOL when:

1. A new major version is released, and we stop supporting the previous major release
2. The release has been superseded by multiple minor releases

When a release reaches EOL, we:

- Stop accepting bug reports
- Stop providing security updates
- Stop updating documentation

Version History
===============

Version 0.x (Current Development)
--------------------------------

- **0.1.0** (2025-12-19): Initial stable release
- **0.1.0rc1** (2025-12-25): Release candidate 1
- **0.1.0b1** (2025-12-20): First beta release
- **0.1.0a2** (2025-12-15): Second alpha release
- **0.1.0a1** (2025-11-30): First alpha release

Version 1.x (Future)
--------------------

- **1.0.0** (TBD): First major stable release with API stability guarantees

Upgrade Guide
=============

From 0.1.0a1 to 0.1.0a2
------------------------

- **Breaking Changes**: None
- **New Features**: Enhanced application management, improved window switching, better control finding
- **Deprecations**: None
- **Migration**: No changes required to existing test cases

From 0.1.0a2 to 0.1.0b1
------------------------

- **Breaking Changes**: None
- **New Features**: Complete keyword set, support for all major control types, advanced waiting mechanisms
- **Deprecations**: None
- **Migration**: No changes required to existing test cases

From 0.1.0b1 to 0.1.0rc1
------------------------

- **Breaking Changes**: None
- **New Features**: Performance improvements, enhanced error messages
- **Deprecations**: None
- **Migration**: No changes required to existing test cases

From 0.1.0rc1 to 0.1.0
----------------------

- **Breaking Changes**: None
- **New Features**: Final bug fixes, documentation improvements
- **Deprecations**: None
- **Migration**: No changes required to existing test cases

Future Major Releases
====================

Version 1.0.0 (TBD)
-------------------

- **Breaking Changes**: Possible API changes to improve consistency and usability
- **New Features**: Enhanced performance, additional functionality, improved documentation
- **Deprecations**: Some legacy keywords may be deprecated
- **Migration**: Detailed migration guide will be provided

Version 2.0.0 (TBD)
-------------------

- **Breaking Changes**: Significant API changes to support new Windows features
- **New Features**: Support for UWP apps, improved accessibility, better integration with other tools
- **Deprecations**: Legacy backend support may be removed
- **Migration**: Detailed migration guide will be provided

Release Schedule
================

We aim to release new versions according to the following schedule:

- **Alpha Releases**: Every 2 weeks during active development
- **Beta Releases**: Every 4 weeks after feature freeze
- **Release Candidates**: Every 1-2 weeks after beta
- **Stable Releases**: When ready, typically every 1-3 months

Contributing to Releases
=======================

If you want to contribute to a release, please:

1. Check the GitHub issues for open issues
2. Look for issues with the "help wanted" label
3. Contribute to the development branch
4. Test the latest release candidates
5. Provide feedback on the release process

Reporting Issues
===============

If you encounter any issues with a specific version, please:

1. Check the GitHub issues to see if it's already reported
2. If not, create a new issue with:
   - The exact version number
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Environment information
   - Any relevant logs or screenshots

Contact Information
==================

For questions about versions or releases, please contact the maintainers through:

- GitHub issues: https://github.com/robotframework/robotframework-pywinauto/issues
- Robot Framework Slack: https://robotframework.slack.com
- Robot Framework Forum: https://forum.robotframework.org/