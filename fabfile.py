from fabric.api import *
import fabric.contrib.project as project
import cgi
import datetime
import github
import json
import os
import re
import shutil
import SocketServer
import sys

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path
env.content_path = 'content'
CONTENT_PATH = env.content_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'

# Github Pages configuration
env.github_pages_branch = "master"

# Port for `serve`
PORT = 8000

def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)

def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')

def rebuild():
    """`build` with the delete switch"""
    local('pelican -d -s publishconf.py')

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')

def cf_upload():
    """Publish to Rackspace Cloud Files"""
    rebuild()
    with lcd(DEPLOY_PATH):
        local('swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
              '-U {cloudfiles_username} '
              '-K {cloudfiles_api_key} '
              'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    """Publish to production via rsync"""
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )

def gh_pages():
    """Publish to GitHub Pages"""
    rebuild()
    local("ghp-import -b {github_pages_branch} {deploy_path} -p".format(**env))

def _slugify(s):
    """Make a slug string"""
    s = re.sub(r'[^\w\s]', '', s)
    s = re.sub(r'\s+', '-', s)
    return s

def _create_comment_issue(title, url):
    with open('../.github.json') as jf:
        config = json.load(jf)
    gh = github.Github(config['token'])
    repo = gh.get_repo('bd808/bd808.github.com')
    issue = repo.create_issue(
        title=title,
        body='Reader comments on [{}]({})'.format(title, url),
        labels=['blog-post'],
    )
    print('Successfully opened issue #{}'.format(issue.number))
    return issue.number

def new_post(title):
    os.chdir(env.content_path)
    now = datetime.datetime.utcnow()
    pname = 'blog/{}-{}.md'.format(
        now.strftime('%Y-%m-%d'),
        _slugify(title))
    if os.path.exists(pname):
        print('{} exits!'.format(pname))
        exit(1)
    with open(pname, 'wb') as post:
        post.write("Title: {}\n".format(cgi.escape(title, quote=True)))
        post.write("Date: {}\n".format(now.strftime('%Y-%m-%dT%H:%M:%SZ')))
        post.write("Comments: True\n")
        post.write("Github_issue_id: {}\n".format(_create_comment_issue(
            title,
            'http://bd808.com/blog/{}/{}/'.format(
                now.strftime('%Y/%m/%d'),
                _slugify(title)
            )
        )))
        post.write("Tags: \n".format())
        post.write("\n")

