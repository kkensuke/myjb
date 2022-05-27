# Let's make a Jupyter book

We are going to make the structure below.
```zsh
~/jupyter-book
	└── test-book
	    ├── .venv
	    └── test-book
```

## Make a jupyter book

### Make directories
At first, we make the structure and activate a venv(virtual environment).
```zsh
$ mkdir -p ~/jupyter-book/test-book
$ cd ~/jupyter-book/test-book
$ python3 -m venv venv
$ source venv/bin/activate
```

see which python is working:
```zsh
$ which python
```
You can see that you are using python in the venv.


### Update pip:
```zsh
$ /Users/<home>/jupyter-book/test-book/venv/bin/python3 -m pip install --upgrade pip
```

Install jupyter-book package
```zsh
(venv)$ pip install -U jupyter-book
```

### Create a new jupyter-book.
```zsh
$ jb create test-book
$ cd test-book
$ jb build .
$ open /Applications/Safari.app _build/html/index.html
```
(jb short for jupyter-book)

## Publish
First, we make a repository named `test-book` on GitHub website without initializing.
Second, we execute the commands below in the test-book directory on your local computer.
```zsh
echo "# test-book" >> README.md
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Username/test-book.git
git push -u origin main
```

One time
```zsh
$ pip install ghp-import
$ ghp-import -n -p -f _build/html
```

You can see the published website!
https://Username.github.io/test-book


## Update
Update source code
```zsh
$ cd test-book
$ jb build --all .
$ git add .
$ git commit -m "comment"
$ git push origin main
```

Update GitHub Pages
```zsh
$ ghp-import -n -p -f _build/html
```

Command `jbgh test-book` concludes all command needed for update. See [jbgh](../basic/alias#build-and-publish-a-jupyter-book)


## Other ways to create jb
### Create a more complete book from interactive prompts.

Jupyter Book also provides a Jupyter Book cookiecutter that can be used to interactively create a book directory structure.
```
jupyter-book create mynewbook/ --cookiecutter
```
https://github.com/executablebooks/cookiecutter-jupyter-book

### Create book files from a Table of Contents
It is possible to use a _toc.yml file in order to create the skeleton of a book automatically. This is useful if you wish to quickly generate empty files from a single structure, and then populate them with content yourselves.
```
jupyter-book toc to-project path/to/_toc.yml
```
