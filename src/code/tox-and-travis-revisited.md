Date: 2015-04-14 07:00
Title: Travis and tox revisited
Slug: tox-and-travis-revisited

Two years on, and I still love the combination of [tox][tox] and
[Travis][travis]. I still write changes to my `tox.ini` and
`.travis.yml` files separately, despite having
[written a tool for this][old-tox2travis]. This tool was used a bit
like this:

    ::bash

    python tox2travis.py > .travis.yml

It occurred to me yesterday that there was a better way of writing
this now - since tox now has a command for listing out what
environments are set up (something which I think didn't exist when I
wrote the original Python script).

Rewritten in bash, it now looks like this:

    ::bash

    #!/bin/bash
    set -o nounset
    set -o errexit

    command -v tox >/dev/null 2>&1 || { echo >&2 "tox2travis requires tox but it's not installed. Aborting."; exit 1; }

    if [ ! -f tox.ini ]; then
        echo "tox.ini not found. Aborting."
        exit 1
    fi

    echo "language: python"
    echo "python: 2.7"
    echo "env:"

    for env in $(tox -l); do
        echo "  - TOX_ENV=${env}"
    done

    echo "install:"
    echo "  - pip install tox"

    echo "script:"
    echo "  - tox -e \$TOX_ENV"

This is functionally pretty identical (though a little better at
error checking) to my previous effort, but is a good deal neater, and
doesn't depend on tox internals.

I've also set it up so that it's on my path, which is the main
(stupid) reason why I never really got used to using the old version.

[tox]: http://tox.readthedocs.org/en/latest/ "Read tox's documentation."
[travis]: /build-breaking.html "Read my first thoughts on Travis, from April 2012."
[old-tox2travis]: /tox-and-travis.html "Read about the original version of tox2travis."
