# Alias

If you are using command line, there must be commands you repeatedly use.
Some commands are long and you would think that copying them every time is a waste of time. In such case, you can use `alias` for a command. If you want to use `h` as an alias for `cd ~`, you define `alias h='cd ~'` in `~/.zshrc` (or `~/.bashrc`). If you can't find such files in your home directory, you need to make it with `touch ~/.zshrc`.

If you find some useful aliases below, write them in `~/.zshrc`.

## Basic

### Customize and colorize PROMPT
```
PS1="%F{082}%n%f %F{051}%~%f %# "
```

### Put a blank line before every prompt except the first one.
```
precmd() { precmd() { echo } }
```

### Frequently used commands

```
# change directory
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias cb='cd -'
alias d='cd ~/Desktop'
alias dl="cd ~/Downloads"
alias h='cd ~'
alias /='cd /'


# show files
# --color=auto does not work for terminal, but for iterm2
#alias l='ls -CF --color=auto'
#alias ls='ls -CF --color=auto'
alias l='ls -CFG'
alias ls='ls -CFG'
alias la='l -a'
alias ll='l -ahlS'
alias tree='tree -ah'
alias tr='tree'
alias tl='tree -ahfL'
alias p='pwd'


# edit files
alias cp='cp -iv'
alias mv='mv -iv'
alias rm='rm -iv'
alias rmf='rm -vf'
alias rmr='rm -ir'
alias rmrf='rm -rvf'


# others
alias b='brew'
alias his='history'
alias grep='grep --color'
alias ner='2>/dev/null'
alias rl="exec ${SHELL} -l" #reload


# vim
alias v='vi'
alias vz='vi ~/.zshrc'
alias so='source'
alias sz='source ~/.zshrc'


# open apps
alias opc='open /Applications/CotEditor.app'
alias opfire='open /Applications/Firefox.app'
alias opgo='open /Applications/Google\ Chrome.app '
alias opsafari='open /Applications/Safari.app'
``` 

## Mac OS settings
### Show/hide hidden files in Finder
```
alias show="defaults write com.apple.finder AppleShowAllFiles -bool true && killall Finder"
alias hide="defaults write com.apple.finder AppleShowAllFiles -bool false && killall Finder"
``` 

### Hide/show all desktop icons
```
alias dhide="defaults write com.apple.finder CreateDesktop -bool false && killall Finder"
alias dshow="defaults write com.apple.finder CreateDesktop -bool true && killall Finder"
```

### Screenshot
```
alias dwl='defaults write com.apple.screencapture location'
alias ddl='defaults delete com.apple.screencapture location'
alias drl='defaults read com.apple.screencapture location'
``` 


## GitHub
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

# use alias as a function
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


### Define an alias of several commands
```
gacp(){
	git add .
	git commit -m "$1"
	git push origin main
}
```

For example, you can define an alias of making a repository with just one command.
```
ginit() {
	git init
	git add .
	git commit -m "Initial commit"
	gh repo create --private --source=. --push'
}
```
You need to install [GitHub CLI](https://cli.github.com/) to use `gh` command.

### gitignore.io
gitignore.io enable us to make .gitignore file easily
```
function gi() { curl -sLw n https://www.toptal.com/developers/gitignore/api/$@ ;}
```

## Python
```
alias python="/usr/bin/python3"
alias py='python'
alias py2='python2'
alias py3='python3'

alias pip='pip3'
alias pin='pip install'
alias wpy='which python'
alias pf='pip list --format=freeze'
alias pfr='pip list --format=freeze > requirements.txt'
```

### Activate a venv
```
alias acv='source venv/bin/activate'
alias deac='deactivate'
```

## Latex
### Copy latex-template directory to somewhere;
```
mklt(){
	cp -r ~/github/physics/report/latex-template ./$1
}
```
