# passpy --  ZX2C4's pass compatible library and cli

passpy has been written to be a platform independent library and cli
that is compatible with [ZX2C4's pass](http://www.passwordstore.org).

passpy saves your passwords in gpg encrypted files and optionally uses
git as a revision tool.  All files are stored inside
`~/.password-store` (or any other location) and can be organised into
folders.  You can also just copy the whole store to have your
passwords available where ever you like.

## Documentation

The latest documentation is available at
[readthedocs](https://passpy.readthedocs.org).

## Installation

### PyPI

Just do

```
$ [sudo] pip install passpy
```

### Arch Linux

The package `python-passpy` is available in the AUR for you to install
however you like.

### Manually

Either clone the git repository using

```
$ git clone https://github.com/bfrascher/passpy.git
```

or download the source from the releases tab and extract it.
Afterwards change into the new folder and do

```
$ [sudo] python setup.py install
```

## Dependencies

passpy depends on Python 3.3 or later (it has mostly been tested using
Python 3.5).  The program makes use of [git](https://www.git-scm.com)
and [gpg2](https://gnupg.org) as well as either xclip or xsel on
Linux.

The following Python packages will be installed alongside passpy:

- [gitpython](https://github.com/gitpython-developers/GitPython)
- [python-gnupg](https://bitbucket.org/vinay.sajip/python-gnupg)
- [click](http://click.pocoo.org/)
- [pyperclip](https://github.com/asweigart/pyperclip)

If you are on Windows and want colourised output on the command line,
you will additionally need to install
[colorama](https://github.com/tartley/colorama).
