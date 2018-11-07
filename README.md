## Set User/ directory (Use GHQ)

```
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
rm -rf User/
ghq get git@github.com:usagizmo/sublime-user.git
ln -s ~/.ghq/github.com/usagizmo/sublime-user User
```

### Install Package Control

via: https://packagecontrol.io/installation

### Set `subl` command

```
ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl
```