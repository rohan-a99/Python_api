#!bin/bash
cd /
cd workspaces/$1
git remote remove origin
git remote add origin $2
