#!/usr/bin/env python3

import os, sys, argparse, subprocess
from os.path import expanduser

basedir = os.path.dirname(os.path.abspath(__file__))

def run(cmd, cwd=None):
    if cwd is None:
        cwd = basedir
    print('\n\x1b[6;30;47m%s\x1b[0m $ %s' % (cwd, cmd))
    subprocess.call(cmd, cwd=cwd, shell=True)

def main():
    parser = argparse.ArgumentParser(description='Deploy cryptoexchange.')
    parser.add_argument('--profile', nargs=1, required=True)
    parser.add_argument('apps', nargs='+')
    args = parser.parse_args()
    profile = args.profile[0]
    apps = args.apps
    print('set basedir to: %s' % basedir)
    print('profile: %s' % profile)
    print('will deploy %s...' % ', '.join(apps))
    run('ansible-playbook --version')
    for app in apps:
        run('ansible-playbook -i environments/%s/hosts.yml playbook.yml --extra-vars "profile=%s app=%s"' % (profile, profile, app))

if __name__ == '__main__':
    main()