# Homebrew and Virtual Environment for python

What is a package manager?
> A package manager or package-management system is a collection of software tools that automates the process of installing, upgrading, configuring, and removing computer programs for a computer in a consistent manner. - wikipedia


There are various package managers.

For OS level, 
- Windows: vcpkg
- Mac: Homebrew
- Ubuntu: apt

For application level,
- PHP: composer
- JavaScript(node): npm, Yarn
- Ruby: gem
- Java: Maven, Gradle
- Python: pip, conda
- R: conda, CRAN

In this page, we (install homebrew and) make a venv (virtual environment) to manage python packages.

## [Homebrew](https://docs.brew.sh/Installation)
Homebrew is the Missing Package Manager for macOS (or Linux).
To install it, input next code in the Terminal (you should check the newest code);
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

you will get next output:
```zsh
==> Next steps:
- Run these two commands in your terminal to add Homebrew to your PATH:
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/kensuke/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
- Run brew help to get started
- Further documentation:
    https://docs.brew.sh
```

So input next to add Homebrew to your PATH (change Username below):
```zsh
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/Username/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Let's check whether you succeeded!
```zsh
brew --version
```

if you get: `Your system is ready to brew.`, you succeeded.
you can also check by;
```zsh
brew doctor
```
If you succeed, you get; `Homebrew 3.3.8`.

(venv)=
## [Venv](https://docs.python.org/3/library/venv.html)
To make a virtual environment for python, venv is the easiest tool! Although there are pyenv or anaconda for python, they are not necessary for beginners.
Let's make a virtual env.
Making a virtual environment by venv and deleting it is really easy. Let's make a test virtual env in the home directory (below for zsh).

```zsh
python3 -m venv ~/test
```
then activate the virtual env:
```zsh
source test/bin/activate
```
or 
```zsh
. test/bin/activate
```

Now your virtual environment is activated. You can see the name of virtual env on the left side of your user name in the terminal.
Let's check the version of python:
```zsh
python -V
```
and you get `Python 3.x.x`.

Now you made a new virtual env and activated it, but actually there is no package in it.
pip freeze shows the packages in your virtual env and there is no output for now. 
Before installing something, you might have to upgrade `pip`, which is a python package manager(change Username below):
```zsh
/Users/Username/test/bin/python3 -m pip install --upgrade pip
```
then let's install a package (here numpy)!
```zsh
pip install numpy
```
and let's check:
```zsh
pip list --format=freeze
```
and you get `numpy==x.xx.x`.

If you want to use python as a beginner, you should install matplotlib, pandas, and jupyter-lab;
```zsh
pip install matplotlib
pip install pandas
pip install jupyterlab
```

Matplotlib is a library for visualization, pandas for data analysis and manipulation, and jupyter-lab for web-based user interface for running python code. Jupyter-lab is the web-based user interface for python.
Scipy, which is for scientific computing, is also a useful package for some people.
Now you can see many packages in your test virtual environment; try `pip list --format=freeze`, though you installed apparently just 4 or 5 packages. Actually, you installed many packages with jupyter-lab.
To deactivate the virtual env, just input: `deactivate` in the terminal. To activate again; `source test/bin/activate`.

````{warning}
If you want to delete the virtual env, you input 
```zsh
rm -rf ~/test
```
in the terminal.
````

## Let's use jupyter-lab!
You installed jupyter-lab, so let's try to use it !!

```zsh
jupyter-lab
```
Your default browser will show up and open jupyter-lab.

To deactivate juypter-lab (not virtual env), in the Terminal; Control + c and you will be asked whether to quit, so enter y [yes]. 
For more details, see [Jupyter Book](../jb/jb.md) page.

You can also use jupyter notebook.
```zsh
jupyter notebook
```

```{note}
- Renaming venv
- Renaming the parent directories of venv
- Changing the location of venv<br>
are not recommended. 
```


