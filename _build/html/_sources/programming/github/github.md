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

## Basic

```{image} ./img/GitHub-flow.png
:name: flow
:width: 600px
:align: center
```

You can learn Git/GitHub at https://www.atlassian.com/git/tutorials


<!--
VCS (version control system)
プログラムのソースコードやドキュメントを開発する際に，最新の状態を保存するだけでなく，様々なタイミングの状態を保存しておき，
後から遡って参照したり，元に戻せるようにする仕組みをVCSという．プログラムの開発は，ver1, ver2と一本道で進むとは限りません．
現状を維持して問題点の修正のみを行う安定板と新子機能を積極的に追加する開発版など，複数に枝分かれさせることがあります．
Gitにはブラン位という仕組みがあり，プロジェクトを分岐させてそれぞれの開発を進めたり，また，分岐させたプロジェクトを合流させる機能があります．

local repo and remote repo
　本章ではパッケージ管理ようのリポジトリという言葉が何度も登場しますが，Gitでもソースコードや変更履歴，コメントなどを一括して保管する場所として，リポジトリが使われています．Gitのリポジトリは自分のPC状に作るローカルリポジトリと共有するサーバー状に作るリモートリポジトリの二つがあります．変更履歴などの情報は，それぞれのリポジトリに保存されています．このような管理方法を分散型バージョン管理(distributed version control)と言います．



-->


<!--
解説
保管場所であるリポジトリに対し、ファイルの編集などを行う場所を「ワークツリー」あるいは「ワーキングエリア」などと呼びます。「git clone」や「git pull」で取得した最新版のファイルはワークツリーに配置されます。つまり「作業ディレクトリ」です。

ワークツリー（作業ディレクトリ）で編集した結果をリポジトリに反映する操作を「コミット」と呼びます。「git add」コマンドでコミットしたいファイルを「インデックス」あるいは「ステージングエリア」と呼ばれる領域に追加します。インデックスにはファイルの変更箇所などが記録されます。

インデックスの内容は「git commit」コマンドでローカルリポジトリにコミットされ、「git push」コマンドでローカルリポジトリの内容をリモートリポジトリに反映します。従って、「git add」や「git commit」などを行わなければ、自分の環境で編集した内容がリポジトリに影響を与えることはありません。自由に編集し、テストできます。なお、ワークツリーのファイルを過去の任意のコミット状態に戻すことも可能です。

### git add

```
git add FILENAME
git add .
git add -A
```

```
```
-->

### Create a new repository
First, make a repository on the GitHub website without initializing.
Second, execute the commands below on the local computer

```
[mkdir project_name]
[cd project_name]
echo "# test" >> README.md
git init
git add .
(git add README.md)
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/<Username>/<repository>.git
git push -u origin main
```

`git init` makes repository, or `.git`, in the current directory.

`git init project_name` makes a directory named project_name and `.git` in it. 

### push an existing repository from the command line
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

This is equivalent to
```
$ git fetch
$ git merge origin main
```


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
# switch to branch1 from main
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
### usage (WARNING: no confirmation!)
```
$ gh repo-delete user/myrepo
```

#### comfirm
```
$ gh alias list
```








