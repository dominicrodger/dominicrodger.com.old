Date: 2012-06-10 07:11
Title: Faster Django Tests
Slug: faster-django-tests

A [long while ago][tdd-django], I discovered that running Django tests
is much faster if you use SQLite, and if you turn off South (this now
seems pretty obvious, but at the time was a bit of a revelation to
me).

Since then, I've come across a better way of setting this up, to avoid
having a `test_settings.py`:

    ::python
    # If manage.py test was called, use SQLite
    import sys
    if 'test' in sys.argv:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': j('test_sqlite.db')
            }
        }

That pretty well does what my old approach with `test_settings.py`, but
instead of having to type:

    ::bash
    python manage.py test --settings=test_settings
    
I can now just type:

    ::bash
    python manage.py test
    
and the faster settings get loaded.

This morning I was perusing
[commits to Django on GitHub][django-commits][^1], when I came across
[this one][faster-test-commit]:

> Documented that setting `PASSWORD_HASHERS` can speed up tests.

Turns out there's another way to speed up tests if you're
authenticating users. Now my extra settings that I set if I'm running
tests look like this:

    ::python
    # If manage.py test was called, use SQLite
    import sys
    if 'test' in sys.argv:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': j('test_sqlite.db')
            }
        }

        PASSWORD_HASHERS = (
            'django.contrib.auth.hashers.MD5PasswordHasher',
        )

Doing that took a sample run of the tests for my [new project][kanisa]
down from 3.6s to 1.0s, which is pretty good for 3 lines of code.

[^1]: This is probably something everyone who works with Django should
      do, it's a great way of finding out what's coming up, and also
      for stumbling across random tips like the one I've not quite got
      to yet.

[tdd-django]: http://www.dominicrodger.com/tdd-django-south.html "Read my original post on making test runs in Django faster"
[django-commits]: https://github.com/django/django/commits/master "View recent commits to Django"
[faster-test-commit]: https://github.com/django/django/commit/17d6cd90299e39823e80a005e7a04bc24ee8af4c "View the commit on GitHub"
[kanisa]: https://github.com/dominicrodger/kanisa "View Kanisa on GitHub"
