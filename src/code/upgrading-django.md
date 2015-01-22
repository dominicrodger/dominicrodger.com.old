Date: 2013-03-30 10:32
Title: Bulk Upgrading Django Sites
Slug: upgrading-django

A [new version of Django][django-1-5-1] was released a couple of days
ago. I'm currently at 11 sites using Django, so upgrading them all
manually (which I did last time) is a pain.

To help me out, I wrote a tiny [Fabric][fabfile] script to spin
through my sites, check if they're using the version of Django that
was upgraded, and if they are, upgrade them.

# Simple Sites

It's worth noting that this only works because all of my sites are
fairly low traffic, and I don't mind too much just taking them offline
for a minute or two. Also, they're all hosted on
[Webfaction][webfaction], and have very similar setups[^1].

# The code

We'll start off by looking at the actual command I run,
`upgrade_django`, which I run across all my Webfaction accounts[^2]:


    ::python
    def upgrade_django(from_version, to_version):
        apps = django_apps[env.host_string]
        for app in apps:
            version = get_django_version(app)
            if version == from_version:
                print ("Current version of Django for %s "
                       "is %s, upgrading to %s..."
                       % (app, version, to_version))
                upgrade_django_install(app, to_version)
            else:
                print ("Current version of Django for %s "
                       "is %s, no upgrade needed."
                       % (app, version))

To upgrade all Django 1.5 sites I have to 1.5.1, I run
`upgrade_django` like this:

    ::bash
    fab upgrade_django:1.5,1.5.1

There are a few more bits you'll need to make this work - let's take a
look at the `get_django_version` code:

    ::python
    def get_django_version(app):
        with cd('~/webapps/%s/' % app):
            with hide('running', 'stdout'):
                with prefix('source env/bin/activate'):
                    result = run('pip freeze | grep "^Django=="')
                    django, version=result.split('==')
                    return version

If the version `get_django_version` returns matches the version I'm
looking to upgrade, then we run `upgrade_django_install`, which is
just this:

    ::python
    def upgrade_django_install(app, version):
        with cd('~/webapps/%s/' % app):
            with prefix('source env/bin/activate'):
                run('pip install Django==%s' % version)
                run('apache2/bin/restart')

Never again will I have to do a Django upgrade ["by hand"][stupid].

You can take a look at the full code on [GitHub][gist].

[django-1-5-1]: https://www.djangoproject.com/weblog/2013/mar/28/django-151/ "Read about the Django 1.5.1 release, on March 28th 2013"
[fabfile]: http://www.fabfile.org "Read about Fabric"
[webfaction]: http://www.webfaction.com/?affiliate=dominicrodger "Sign up for Webfaction and help me out a bit!"
[stupid]: https://twitter.com/dominicrodger/status/112520438617350145 "How I used to do this, to my shame"
[gist]: https://gist.github.com/dominicrodger/5276253 "View all the code for this blog post"

[^1]: They all have their virtualenv in `webapps/appname/env`, for
      example.
[^2]: Since I run sites for various organisations, most of them have
      their own Webfaction account.
