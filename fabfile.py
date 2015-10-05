from fabric.api import env, run, cd, prefix, local

env.use_ssh_config = True
env.hosts = ['study', ]

def deploy():
    local("git push")
    with cd('/var/www/dominicrodger.com'):
        run("git pull")
        with prefix('source .venv/bin/activate'):
            run('pip install -r requirements.txt')
            run('make')
