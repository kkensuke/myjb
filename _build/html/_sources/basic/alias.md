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
# https://www.cyberciti.biz/faq/apple-mac-osx-terminal-color-ls-output-option/
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced

alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'

alias b='brew'
alias cb='cd -'
alias d='cd ~/Desktop'
alias dl="cd ~/Downloads"
alias class='cd ~/My\ Drive/master/class/'
alias h='cd ~'
alias /='cd /'
alias cp='cp -iv'
alias grep='grep --color'
alias his='history'
# --color=auto does not work for terminal, but for iterm2
#alias l='ls -CF --color=auto'
#alias ls='ls -CF --color=auto'
alias l='ls -CFG'
alias ls='ls -CFG'
alias la='l -a'
alias ll='l -ahlS'
alias mv='mv -iv'
alias ner='2>/dev/null'
alias opc='open /Applications/CotEditor.app '
alias opz='s;open /Applications/CotEditor.app .zshrc'
alias opfire='open /Applications/Firefox.app '
alias opgoo='open /Applications/Google\ Chrome.app '
alias opsafari='open /Applications/Safari.app '
alias p='pwd'
alias rm='rm -iv'
alias rmf='rm -vf'
alias rmr='rm -ir'
alias rmrf='rm -rvf'
alias rl="exec ${SHELL} -l" #reload
alias so='source'
alias tree='tree -ah'
alias tre='tree -ah'
alias tl='tree -ahfL 2'

alias v='vi'
alias vz='vi ~/.zshrc'
alias sz='source ~/.zshrc'
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

### gitignore.io enable us to make .gitignore file easily
```
function gi() { curl -sLw n https://www.toptal.com/developers/gitignore/api/$@ ;}
```

### Make a new repository based on the current directory
```
ginit() {
	git init
	git add .
	git commit -m "Initial commit"
	gh repo create --private --source=. --push'
}
```
You need to install GitHub CLI

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

## Related to Latex
### Copy latex-template directory to somewhere;
```
mklt(){
	cp -r ~/github/physics/report/latex-template ./$1
}
```