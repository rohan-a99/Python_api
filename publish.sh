#!bin/bash
cd /
cd $1
git remote rm origin
git remote add origin $2
