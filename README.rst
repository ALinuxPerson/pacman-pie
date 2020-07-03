Description
===========
**pacman-pie** is a pythonic implementation of **pyalpm**.

**pacman-pie** aims to be a better-looking alternative of Arch Linux's **pacman**.

**pacman-pie** does **not** intend to be a drop-in replacement for **pacman**.

Prerequisites
=============
* Python>=3.6
* Arch Linux
* pyalpm
* pipenv

Installation
============
1. Install ``pyalpm``.

.. code-block:: bash

    $ sudo pacman -S pyalpm

2. Instal ``pacman-pie`` as root.

.. code-block:: bash

    $ sudo pip install pacman-pie

Usage
=====
..
    TODO: Convert the stdout of ``sudo ppacman install packages vim`` to asciicinema stuff

* Installing packages (note: concept only)

.. code-block:: bash

    $ sudo ppacman install packages vim
    ::Preparation:
        Look for package 'vim'
            Package 'vim' exists.
        Resolve dependencies for package 'vim'
            Dependency resolution successful.

    ::Packages (2):
        vim         8.2.0814-3 (1.65 MiB)
        vim-runtime 8.2.0814-3 (6.26 MiB)

    ::Space Info:
        Download Size:   7.92 MiB
        Install Size:   32.98 MiB

    ::Your Input:
        Proceed? [Y/n]
        ⏎ y  # pretend to input (y)

    ::Package Retrieval:
        vim-runtime 8.2.0814-3
            Retrieved: 6.3 MiB
            Speed:  4.86 MiB/s
            Remaining:    100%
        vim 8.2.0814-3
            Retrieved: 1692.8 KiB
            Speed:     3.70 MiB/s
            Remaining:       100%

    ::Integrity Checks:
        Check keys in keyring
            Remaining: 100%
        Check package integrity
            Remaining: 100%
        Load package files
            Remaining: 100%
        Check file conflicts
            Remaining: 100%
        Check available disk space
            Remaining 100%

    ::Package Installation:
        Installing vim 8.2.0814-3
            Remaining: 100%
        Installing vim-runtime 8.2.0814-3
            Remaining: 100%

    ::Optional Dependencies:
        vim-runtime 8.2.0814-3
            python2: Python 2 language support
            python: Python 3 language support (installed)
            ruby: Ruby language support       (installed)
            lua: Lua language support         (installed)
            perl: Perl language support       (installed)
            tcl: Tcl language support
        vim 8.2.0814-3
            sh: Support for some tools and macros (installed)
            python: Demoserver example tool       (installed)
            gawk: Mve tools support               (installed)

    ::Pacman hooks:
        Arming ConditionNeedsUpdate...
        Updating icon theme caches...
        Updating the desktop file MIME type cache...

    ::Ppacman hooks:
        (Nothing to run!)

* Removing packages

.. code-block:: bash

    $ sudo ppacman remove packages vim

* Updating and upgrading

.. code-block:: bash

    $ sudo ppacman
