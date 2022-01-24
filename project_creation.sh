cd /
cd workspaces/$1
chmod +x load.sh
chmod +x release.sh
chmod +x build.sh
chmod +x debug.sh
git init
git remote add origin $2
