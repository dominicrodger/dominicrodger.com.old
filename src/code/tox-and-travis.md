Date: 2013-07-26 07:20
Title: Easy testing with Travis and tox
Slug: tox-and-travis

I love [tox][tox] - it's a great tool for checking that your Python
packages are installable, and that you support all the various
configurations of Python versions and other package versions that you
think you do. It's also quite a neat way of checking your
documentation builds properly, and that your code remains PEP 8
compliant[^1].

I also [love Travis][i-love-travis], since it helps me accomplish much
the same thing as tox, but does so in an automated way, with every push.

A typical `tox.ini` file for one of my projects looks a bit like this:

    ::ini

    [tox]
    envlist = py33-1.6.X,docs,flake8

    [testenv]
    commands=python setup.py test

    [testenv:py33-1.6.X]
    basepython = python3.3
    deps = https://www.djangoproject.com/download/1.6b1/tarball/

    # Omitted for brevity

    [testenv:docs]
    basepython=python
    changedir=docs
    deps=sphinx
    commands=
        sphinx-build -W -b html -d {envtmpdir}/doctrees .  {envtmpdir}/html

    [testenv:flake8]
    basepython=python
    deps=flake8
    commands=
        flake8 djohno

Whilst my `.travis.yml` file looks a bit like this:

    language: python
    python: 2.7
    env:
      - TOX_ENV=py33-1.6.X
      - TOX_ENV=py33-1.5.X
      - TOX_ENV=py27-1.6.X
      - TOX_ENV=py27-1.5.X
      - TOX_ENV=py27-1.4.X
      - TOX_ENV=py26-1.5.X
      - TOX_ENV=py26-1.4.X
      - TOX_ENV=docs
      - TOX_ENV=flake8
    install:
      - pip install tox
    script:
      - tox -e $TOX_ENV

This `.travis.yml` file sets up an individual build job for each
environment I want to test with, which makes for slightly faster
builds (because they're parallelised), and for clearer build errors
(since the build status table will have red rows just for whichever
jobs failed).

However, it repeats a section (the list of available environments)
from my `tox.ini` file, which is sad. I could get around this by
giving up having individual build jobs, or by just saying that I'll
fix the file when I add an environment to tox to test.

Or, I could write a little script to generate a `.travis.yml` file
from a `tox.ini` file, like this:

    ::python
    from tox._config import parseconfig

    print "language: python"
    print "python: 2.7"
    print "env:"
    for env in parseconfig(None, 'tox').envlist:
        print "  - TOX_ENV=%s" % env
    print "install:"
    print "  - pip install tox"
    print "script:"
    print "  - tox -e $TOX_ENV"

You could even set this up to run in a git pre-commit hook or
something (piping the output to `.travis.yml`), but that's a job for
another day.

[^1]: I use [flake8][flake8] for the PEP 8 checking, since it also
      picks up things like unused variables and imports, which is
      handy.

[tox]: http://tox.readthedocs.org/en/latest/ "Read tox's documentation."
[i-love-travis]: /build-breaking.html "Read my first thoughts on Travis, from April 2012."
[flake8]: http://flake8.readthedocs.org/en/2.0/ "Read about flake8 - a wrapper around PyFlakes and pep8."
