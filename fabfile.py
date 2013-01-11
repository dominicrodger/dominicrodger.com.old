from fabric.api import env, hosts, run, cd, hide, prefix

env.use_ssh_config = True
env.hosts = ['dmr', ]

def deploy_blog_changes():
    with cd('~/dominicrodger.com'):
        run("git pull")
        with prefix('source .env/bin/activate'):
            run('pip install -r requirements.txt')
            run('make')
