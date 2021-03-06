# Commit Masssages with emoji

When you commit files with git/github, you add some commit-messages. In the code of comduct of some project, it is recommended to use `emoji` to easily represent what the commit is all about. However, it is difficult to input `emoji` in command line. Here, we introduce 2 ways to do that.

## Use aliases
put code below in `.zshrc`.
```
## Using EMOJI-LOG (https://github.com/ahmadawais/Emoji-Log) ##
# Git Commit, Add all and Push โ in one step.
gacp() { git add . && git commit -m "$*" && git push origin main }

gini() { gacp "๐ Initial commit"}
gnew() { gacp "โจ NEW: $@" }
gimp() { gacp "๐ IMPROVE: $@" }
gprg() { gacp "๐ง PROGRESS: $@" }

gmtn() { gacp "๐ง MAINTAIN: $@" }
gfix() { gacp "๐ FIX: $@" }
ghot() { gacp "๐ HOTFIX: $@" }
gbrk() { gacp "โผ๏ธ BREAKING: $@" }
grem() { gacp "๐๏ธ REMOVE: $@" }

gmrg() { gacp "๐ MERGE: $@" }
gref() { gacp "โป๏ธ REFACTOR: $@" }
gtst() { gacp "๐งช TEST: $@" }
gdoc() { gacp "๐ DOC: $@" }
grls() { gacp "๐ RELEASE: $@" }
gsec() { gacp "๐ฎ SECURITY: $@" }

# See more in .gitmessage

# Show commit type
gtyp() {
NORMAL='\033[0;39m'
GREEN='\033[0;32m'
echo "$GREEN gini$NORMAL โ ๐ Initial commit
$GREEN gnew$NORMAL โ โจ NEW
$GREEN gimp$NORMAL โ ๐ IMPROVE
$GREEN gprg$NORMAL โ ๐ง PROGRESS
$GREEN gmtn$NORMAL โ ๐ง MAINTAIN
$GREEN gfix$NORMAL โ ๐ FIX
$GREEN ghot$NORMAL โ ๐ HOTFIX
$GREEN gbrk$NORMAL โ โผ๏ธ  BREAKING
$GREEN grem$NORMAL โ ๐๏ธ  REMOVE
$GREEN gmrg$NORMAL โ ๐ MERGE
$GREEN gref$NORMAL โ โป๏ธ  REFACTOR
$GREEN gtst$NORMAL โ ๐งช TEST
$GREEN gdoc$NORMAL โ ๐ DOC
$GREEN grls$NORMAL โ ๐ RELEASE
$GREEN gsec$NORMAL โ ๐ฎ SECURITY"
}

```


## Use commit.template
put code below in `.gitmessage`(filename does not matter).
```
# ==== Emojis ====                      description
# ๐ :tada:Initial commit             -
# โจ :sparkles:New                    โ
# ๐ :ok_hand:Improve                 โ
# ๐ :bug:Fix                         โ
# ๐ :apple:Fix on MacOS              -
# ๐ง :penguin:Fix on Linux            -
# ๐ :checkered_flag:Fix on Windows   -
# ๐ :ambulance:Hotfix                -
# ๐ง :construction:In progress        -
# ๐ :books:Docs                      โ
# ๐ง :wrench:Maintain                 โ
# ๐ฅ :boom:Breaking                   โ
# ๐งช :test_tube:Test                  โ
# ๐ :rocket:Release                  โ
# โฌ๏ธ :arrow_up:Upgrade                โ
# โป๏ธ :recycle:Refactor                โ
# ๐๏ธ :wastebasket:Deprecate           โ
# ๐ :twisted_rightwards_arrows:Merge โ
# ๐ฎ :cop:Security                    -
# โฟ :wheelchair:Accessibility        -
# โ :question:Other                  โ
# ๐ฆ :package:.json in JS             -
# ๐ณ :whale:Docker                    -

# ==== Write below ====
# Title: Summary, imperative, start upper case, don't end with a period
# Format ':emoji: Subject #issue No.'
# |<----   Preferably using up to 50 chars   --->|<------------------->|

# Remember blank line between title and body.

# (Optional) Body: Explain *what* and *why* (not *how*).
# |<----   Try To Limit Each Line to a Maximum Of 72 Characters   ---->|


# At the end: Include Co-authored-by for all contributors. 
# Include at least one empty line before it. Format: 
# Co-authored-by: name <user@users.noreply.github.com>
#
# 1. Separate subject from body with a blank line
# 2. Limit the subject line to 50 characters
# 3. Capitalize the subject line
# 4. Do not end the subject line with a period
# 5. Use the imperative mood in the subject line
# 6. Wrap the body at 72 characters
# 7. Use the body to explain what and why vs. how
# See https://chris.beams.io/posts/git-commit/
#     https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733
```

and run next code
```
git config --global commit.template ~/.gitmessage
```


## Reference

[jupyterbook Development Conventions](https://github.com/executablebooks/.github/blob/master/CONTRIBUTING.md#commit-messages)

[How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)\
https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733\
https://gist.github.com/rxaviers/7360908

https://github.com/ahmadawais/Emoji-Log\
https://github.com/carloscuesta/gitmoji-cli\
https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md

[Commit message examples](https://gist.github.com/mono0926/e6ffd032c384ee4c1cef5a2aa4f778d7)