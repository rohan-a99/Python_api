cd /
cd workspaces/$1
chmod +x workspaces/$1/load.sh
chmod +x workspaces/$1/release.sh
chmod +x workspaces/$1/build.sh
chmod +x workspaces/$1/debug.sh
git init
git remote add origin $2
