---
title: GitHub
summary: 
description: Usage of GitHub
author: kk564
date: 2020-01-23
some_url: 
tags:
  - 
  - 
---
# GitHub

```{image} ./img/GitHub-flow.png
:name: flow
:width: 600px
:align: center
```

## VCS (version control system)
When developing source code or documentation, VCS(version control system) is a system that not only saves the latest state but also saves the state at every moments so that it can be referred back to or restored later.
Program development does not necessarily proceed in a straight line from ver1 to ver2.
Sometimes a program is divided into two or more branches: a stable version that maintains the current state and only fixes problems, and a development versions that actively adds new functions.
Git has a branching mechanism that allows you to branch projects and develop each branches, and also allows you to merge the branched projects.

## Local repository and remote repository
There are two types of repositories: `local repositories` on your PC and `remote repositories` on a shared server. Each repository stores the history of changes and other information. This type of management is called distributed version control.

## Basic commands
### Create a new repository
First, make a repository on the [GitHub website](https://github.com/) without initializing.
Second, execute the commands below on the local computer

```
[mkdir project_name]
[cd project_name]
echo "# test" >> README.md

# initialize the repository
git init

# add all files in the current directory to working tree
git add .

# commit the changes to the local repository
git commit -m "first commit"

git branch -M main
git remote add origin https://github.com/<Username>/<repository>.git

# push the changes to the remote repository
git push -u origin main
```

`git init` makes repository, or `.git`, in the current directory.

`git init project_name` makes a directory named project_name and `.git` in it. 


### push an existing repository from the command line
If you have already made (or initialized) a local repository, you just need to use the following commands after making a remote repository.
```
git remote add origin https://github.com/<Username>/<repository>.git
git branch -M main
git push -u origin main
```

### Clone
In an arbitrary directory,
```
$ git clone [branch, or you can omit here for main] https://github.com/<Username>/<repository>.git
$ cd <repository>
```

After you add or modify files:
```
$ git add <file>
($ git add .  # add current directory)
($ git status)
$ git commit -m "<comment>"
$ git push origin main
($ git status)
```

<!--
### Defference between fork and clone
#### clone
リモートリポジトリをローカルリポジトリに複製すること
#### fork
他人のリポジトリを自分のアカウントのリモートリポジトリにコピーすること
* オリジナルのリポジトリへの貢献が前提
* forkした場合そのリポジトリを所有する開発者に通知される

1. リポジトリAをfork2. forkしたリポジトリBをローカルにclone3. cloneしたリポジトリCで開発し、リポジトリBに反映4. リポジトリAの管理者にPull Requestを送信
-->

### take new changes of the remote repository into the local repository
```
$ git pull origin main
```

````{tip}
This is equivalent to
```
$ git fetch
$ git merge origin main
```
````

### make a branch and change branches at local

When you make a repository, the only main branch exists at first.
So, you are in the main branch by default. 

You can check the current branch by
```
$ git branch
```

You can see all branches including the remote branches by
```
$ git checkout -a
```

1, Making new branch at local (branch not in remote)

Let's make a new branch!
```
# make a branch
$ git branch <branch>
# switch to <branch> from main
$ git checkout <branch>
```

````{tip}
These two lines are equivalent to
```
$ git checkout -b <branch>
```
````

Then reflect the new branch to the remote repository.
```
$ git push origin <branch>
```

2, when remote/branch already exists
```
# create a new local branch pointing to the remote branch
$ git branch <branch> origin/<branch>
# check out that branch
$ git checkout <branch>
```

````{tip}
These two lines are equivalent to
```
$ git checkout -b <branch> origin/<branch>
```
````




### .gitignore

You can configure Git to ignore files you don't want to check in to GitHub.
All you have to do is write down filenames in `.gitignore` in the same directory as `.git`.

However, making `.gitignore` and writing filenames in each directory in the control of Git is troublesome. You can make `.gitignore` easily with [gitignore.io website](https://www.toptal.com/developers/gitignore) or [gitignore.io CLI](https://docs.gitignore.io)

As to some files, you will append their filenames in every `.gitignore`.
To avoid it, making `~/.gitignore_global` is a solution. `~/` represents the home directory.

```{note}
First, make `~/.gitignore_global` if you haven't made it yet
```
install .gitignore.io from https://docs.gitignore.io/install/command-line

for macOS :

- one time
```
$ git config --global core.excludesfile ~/.gitignore_global       
$ echo "function gi() { curl -sLw "\n" https://www.toptal.com/developers/gitignore/api/\$@ ;}" >> \
~/.rc && source ~/.rc
```

- make `.gitignore`
```
$ gi macos,python,visualstudiocode >> ~/.gitignore_global
```
Refer to https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files for details.


### When you want to rename a repository
First, rename on GitHub website.
Second, open the corresponding [.git->config], and [url = https://~.<rename_here>.git]


### quit Git administration

All you have to do is remove the `.git` directory.


### remove files
1, remove files from the repository and local directory
2, remove files from the repository

```
$ git rm FILENAME 1
$ git rm --cached FILENAME 2
$ git commit -m "delete"; git push origin main
```


### Invite people to my Private repository





## GitHub CLI
### install
```
$ brew install gh
```
### make a new repository based on the current directory
```
$ git init; git add .
$ git commit -m "Initial commit"
$ gh repo create --private --source=. --push'
```
### make an alias to delete remote repository
#### register
```
$ gh alias set repo-delete 'api -X DELETE repos/$1'
$ gh auth refresh -h github.com -s delete_repo
```
#### usage (WARNING: no confirmation!)
```
$ gh repo-delete user/myrepo
```

#### comfirm
```
$ gh alias list
```


## Reference
[What is Git?](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F)

[Bitbucket](https://www.atlassian.com/git/tutorials).
