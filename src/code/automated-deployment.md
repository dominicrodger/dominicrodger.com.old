Date: 2013-02-03 20:43
Title: Automated Deployment of Django Sites
Slug: automated-deployment

I tried out [Fabric][fabric] a while ago, but never really got
anywhere with it.

Time passed, and I forgot it existed, and wrote my simple scripts for
automating deployment of my various sites, using
[Paramiko][paramiko]. It was incredibly tedious, but meant I could
deploy my sites from whatever computer I was on, provided I had a
checkout of my code.

Then I re-discovered Fabric, and realised I was about to throw away a
lot of code.

Deploying my sites now generally involves having Fabric installed in
my virtual environment, and a `fabfile.py` file locally which looks
something like this:

    ::python
    from fabric.api import env, run, cd, prefix, local
    from fabric.colors import green

    env.use_ssh_config = True # So I can use stuff from ~/.ssh/config
    env.hosts = ['myhostname', ] # Hosts I want to run it on


    def deploy():
        local('git push')
        with cd('~/webapps/cbm'), prefix('source env/bin/activate'):
            print(green("Updating code..."))
            run("git pull")

            print(green("Updating the database..."))
            run("python manage.py syncdb")
            run("python manage.py migrate")

            print(green("Collecting static files..."))
            run("python manage.py collectstatic --noinput")

            print(green("Restarting the server..."))
            run("apache2/bin/restart")

Now, when I get home after my [train journey][train], I can just run
`fab deploy`, and changes I've made on my way home are automatically
deployed. Best of all, on sites which use the same codebase (of which
I've got a few), I can just add a list of hostnames to deploy to, and
all the sites stay in sync.

I've also got Fabric files set up for Django upgrades, so whenever
there's a new version of Django out, I can now update all my sites
with one command[^1].

Now I've written this, I'll publish this post with this site's
[fabfile][fabfile].

[^1]: This is generally most useful for point releases, such as for
      going from 1.4.2 to 1.4.3. Major upgrades (e.g. from 1.3 to 1.4)
      might require a bit more work, but I'd still do it all with
      Fabric.

[fabric]: http://fabfile.org "Fabric is a Python library for application deployment over SSH"
[paramiko]: http://www.lag.net/paramiko/ "Paramiko is a Python module that implements the SSH2 protocol"
[train]: ubuntu-netbook.html "Read a bit about my train journey"
[fabfile]: https://github.com/dominicrodger/dominicrodger.com/blob/master/fabfile.py "fabfile.py for dominicrodger.com"
