# Commit Masssages with emoji

When you commit files with git/github, you add some commit-messages. In the code of comduct of some project, it is recommended to use `emoji` to easily represent what the commit is all about. However, it is difficult to input `emoji` in command line. Here, we introduce 2 ways to do that.

## Use aliases
put code below in `.zshrc`.
```
## Using EMOJI-LOG (https://github.com/ahmadawais/Emoji-Log) ##
# Git Commit, Add all and Push — in one step.
gacp() { git add . && git commit -m "$*" && git push origin main }

gini() { gacp "🎉 Initial commit"}
gnew() { gacp "✨ NEW: $@" }
gimp() { gacp "👌 IMPROVE: $@" }
gprg() { gacp "🚧 PROGRESS: $@" }

gmtn() { gacp "🔧 MAINTAIN: $@" }
gfix() { gacp "🐛 FIX: $@" }
ghot() { gacp "🚑 HOTFIX: $@" }
gbrk() { gacp "‼️ BREAKING: $@" }
grem() { gacp "🗑️ REMOVE: $@" }

gmrg() { gacp "🔀 MERGE: $@" }
gref() { gacp "♻️ REFACTOR: $@" }
gtst() { gacp "🧪 TEST: $@" }
gdoc() { gacp "📚 DOC: $@" }
grls() { gacp "🚀 RELEASE: $@" }
gsec() { gacp "👮 SECURITY: $@" }

# See more in .gitmessage

# Show commit type
gtyp() {
NORMAL='\033[0;39m'
GREEN='\033[0;32m'
echo "$GREEN gini$NORMAL — 🎉 Initial commit
$GREEN gnew$NORMAL — ✨ NEW
$GREEN gimp$NORMAL — 👌 IMPROVE
$GREEN gprg$NORMAL — 🚧 PROGRESS
$GREEN gmtn$NORMAL — 🔧 MAINTAIN
$GREEN gfix$NORMAL — 🐛 FIX
$GREEN ghot$NORMAL — 🚑 HOTFIX
$GREEN gbrk$NORMAL — ‼️  BREAKING
$GREEN grem$NORMAL — 🗑️  REMOVE
$GREEN gmrg$NORMAL — 🔀 MERGE
$GREEN gref$NORMAL — ♻️  REFACTOR
$GREEN gtst$NORMAL — 🧪 TEST
$GREEN gdoc$NORMAL — 📚 DOC
$GREEN grls$NORMAL — 🚀 RELEASE
$GREEN gsec$NORMAL — 👮 SECURITY"
}

```


## Use commit.template
put code below in `.gitmessage`(filename does not matter).
```
# ==== Emojis ====                      description
# 🎉 :tada:Initial commit             -
# ✨ :sparkles:New                    —
# 👌 :ok_hand:Improve                 —
# 🐛 :bug:Fix                         —
# 🍎 :apple:Fix on MacOS              -
# 🐧 :penguin:Fix on Linux            -
# 🏁 :checkered_flag:Fix on Windows   -
# 🚑 :ambulance:Hotfix                -
# 🚧 :construction:In progress        -
# 📚 :books:Docs                      —
# 🔧 :wrench:Maintain                 —
# 💥 :boom:Breaking                   —
# 🧪 :test_tube:Test                  —
# 🚀 :rocket:Release                  —
# ⬆️ :arrow_up:Upgrade                —
# ♻️ :recycle:Refactor                —
# 🗑️ :wastebasket:Deprecate           —
# 🔀 :twisted_rightwards_arrows:Merge —
# 👮 :cop:Security                    -
# ♿ :wheelchair:Accessibility        -
# ❓ :question:Other                  —
# 📦 :package:.json in JS             -
# 🐳 :whale:Docker                    -

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


Reference

[jupyterbook Development Conventions](https://github.com/executablebooks/.github/blob/master/CONTRIBUTING.md#commit-messages)

[How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)\
https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733\
https://gist.github.com/rxaviers/7360908

https://github.com/ahmadawais/Emoji-Log\
https://github.com/carloscuesta/gitmoji-cli\
https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md

[Commit message examples](https://gist.github.com/mono0926/e6ffd032c384ee4c1cef5a2aa4f778d7)