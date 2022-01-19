# Alias

If you find some useful aliases, write them in `~/.zshrc`.

## Basic

### Customize and colorize PROMPT
```
PS1="%F{082}%n%f %F{051}%~%f %# "
```

### puts a blank line before every prompt except the first one.
```
precmd() { precmd() { echo } }
```

### Frequently used commands
```
# https://www.cyberciti.biz/faq/apple-mac-osx-terminal-color-ls-output-option/
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced

alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'

alias b='brew'
alias h='cd ~'
alias p='pwd'
# --color=auto does not work for terminal, but for iterm2
#alias l='ls -CF --color=auto'
#alias ls='ls -CF --color=auto'
alias l='ls -CGF'
alias ls='ls -CGF'
alias la='l -a'
alias ll='l -ahlS'
alias his='history'
alias tre='tree'
alias tl='tree -La 2'

alias cp='cp -iv'
alias mv='mv -iv'
alias rm='rm -iv'
alias rmf='rm -vf'
alias rmr='rm -ir'
alias rmrf='rm -rvf'

alias v='vi'
alias vz='vi ~/.'
alias sz='source ~/.'
```


## Related to GitHub
```
alias g='git'
alias ga='git add'
alias gb='git branch'
alias gc='git commit'
alias gch='git checkout'
alias gcl='git clone'
alias gd='git diff'
alias gf='git fetch'
alias gi='git init'
alias gm='git merge'
alias gps='git push'
alias gpl='git pull'
alias gpom='git push origin main'
alias gs='git status'
```
### 2 ways to define aliases
#### Non-interactive
```
alias gcm='git commit -m '
# usage: gcm "add"

Or

gcm(){ git commit -m "$1" }
# usage: gcm add
```

#### Interactive
```
gcm() {
	echo "Comment: " && read comment
	git commit -m "${comment}"
}
```


### define an alias of several commands
```
gacp(){
	git add .
	git commit -m "$1"
	git push origin main
}
```

### gitignore.io enable us to make .gitignore file easily
```
function gi() { curl -sLw n https://www.toptal.com/developers/gitignore/api/$@ ;}
```

### make a new repository based on your current directory
```
ginit() {
	git init
	git add .
	git commit -m "Initial commit"
	gh repo create --private --source=. --push'
}
```
you need to install GiHub CLI

## Related to Python
```
alias py='python'
alias py2='python2'
alias py3='python3'

alias pin='pip install'
alias p3in='pip3 install'
alias wpy='which python'
```

### venv activate
```
alias acv='source venv/bin/activate'
alias deac='deactivate'
```


### make venv and create jupyter-book
```
mkvjb() {
	mkdir -p ~/jupyter-book/$1
	cd ~/jupyter-book/$1
	python3 -m venv venv
	source venv/bin/activate
	/Users/Username/jupyter-book/$1/venv/bin/python3 -m pip install --upgrade pip
	pip install -U jupyter-book
	jb create $1
	cd $1
	jb build .
	open /Applications/Safari.app _build/html/index.html
}
```

```
~/jupyter-book
	└── test-book
	    ├── .venv
	    └── test-book
```
(jbgh)=
### build and publish jupyter-book
```
jbgh(){
	cd ~/jupyter-book/$1/$1
	jb build --all .
	git add .
	git commit -m add
	git push origin main
	ghp-import -n -p -f _build/html
}
```


## Related to Latex
### copy latex-template directory;
```
mklt(){
	cd ~/Report
	cp -r latex_template ~/Report/$1
}
```
