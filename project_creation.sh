#!bin/bash
cd /
cd workspaces/$1
git init
git remote set-url origin $2
git pull