#!bin/bash
cd /
cd workspaces/$1
gradle build --refresh-dependencies
