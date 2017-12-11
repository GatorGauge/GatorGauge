""" github-clone-all.py
Modified from original version by Dan Wallach <dwallach@rice.edu>.
"""

import sys
import os
import subprocess
import time
import requests


# TODO: make keywords a list of keywords to search for in the name of the
# github repositories


def get_repositories(github_token, github_project, keywords, out_dir):
    #
    # local goodies (for my cron job)
    #
    from datetime import datetime
    from pytz import timezone

    print("")
    print(">>>>>>>>>>>>>>")
    print(
        ">>>>>>>>>>>>>> Running github-clone-all: " +
        datetime.now(
            timezone("US/Eastern")).strftime('%Y-%m-%d %H:%M:%S %Z%z'))
    print(">>>>>>>>>>>>>>")
    print("")

    request_headers = {
        "User-Agent": "GitHubCloneAll/1.0",
        "Authorization": "token " + github_token,
    }

    all_repos_list = []

    page_number = 1
    sys.stdout.write('Getting repo list from Github')

    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        repos_page = requests.get(
            'https://api.github.com/orgs/' +
            github_project +
            '/repos?page=' +
            str(page_number),
            headers=request_headers)
        page_number = page_number + 1

        if repos_page.status_code != 200:
            print("Failed to load repos from GitHub: " +
                  str(repos_page.content))
            return

        repos_page_json = repos_page.json()

        if not repos_page_json:
            print(" Done.")
            break

        all_repos_list = all_repos_list + repos_page.json()

    # Each repo in the list has the following fields that we care about:
    #
    # clone_url: starts with https, suitable for checking out from the command-line
    #     (e.g., 'https://github.com/RiceComp215/comp215-week01-intro-2017-dwallach.git')
    #
    # ssh_url: starts with git@github.com (e.g., 'git@github.com:RiceComp215/comp215-week01-intro-2017-dwallach.git')
    #
    # name: the name of the repo itself (e.g., 'comp215-week01-intro-2017-dwallach')
    #
    # full_name: the project and repo (e.g.,
    # 'RiceComp215/comp215-week01-intro-2017-dwallach')

<<<<<<< HEAD
    filteredRepoList = [x for x in allReposList if all(
        key in x['name'] for key in keywords)]  # attempt to check for all keywords in name
    print(str(len(filteredRepoList)) +
          " of " +
          str(len(allReposList)) +
          " repos start with " +
          str(keywords))
=======
    # attempt to check for all keywords in name
    filtered_repo_list = [
        x for x in all_repos_list
        if all(key in x['name']
               for key in keywords)]
    print(str(len(filtered_repo_list)) + " of " +
          str(len(all_repos_list)) + " repos start with " + str(keywords))
>>>>>>> origin/master
    time.sleep(2)
    # before we start getting any repos, we need a directory to get them
    if out_dir != ".":
        try:
            os.makedirs(out_dir)
        except OSError:
            # directory probably already exists
            print(
                "Directory '" +
                str(out_dir) +
                "' already exists, please wait while directory is deleted\n")
            # deletes out_dir folder if it already exists
            command = 'rm -r -f ./' + str(out_dir)
            os.system(command)
            os.makedirs(out_dir)
        os.chdir(out_dir)

    # specific clone instructions here:
    # https://github.com/blog/1270-easier-builds-and-deployments-using-git-over-https-and-oauth
    repo_num = 1
    for repo in filtered_repo_list:
        clone_url = 'https://' + \
            str(github_token) + '@github.com/' + \
            str(repo['full_name']) + '.git'

        # Steps to take, per docs above:
        #
        # mkdir foo
        # cd foo
        # git init
        # git pull https://<token>@github.com/username/bar.git

        # if repositories are not placed in seperate folder
        # each one must be deleted before it can be redownloaded
        if os.path.isdir(repo['name']):
            command = 'rm -r -f ' + repo['name']
            os.system(command)
        os.mkdir(repo['name'])
        os.chdir(repo['name'])
        subprocess.call(["git", "init"])
        print(">>>>>>>>>>>>>>")
        print(">>>>>>>>>>>>>> Downloading repository number " +
              str(repo_num) + " of " + str(len(filtered_repo_list)) +
              " repositories")
        print(">>>>>>>>>>>>>>")
        subprocess.call(["git", "pull", clone_url])
        os.chdir('..')
        repo_num += 1

    #
    # leftover from an earlier emergency: if you want to make a repo be private, here's the code to do it
    #
    #         response = requests.patch('https://api.github.com/repos' + github_project + '/' + name,
    #                                   headers = request_headers, json={ "private": True })
    #
