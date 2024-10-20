#!/bin/sh -e

export LANG=jp_JP.UTF-8

apt-get update -y
apt-get upgrade -y

update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 30
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-12 30

cp .bash_profile ~/.bash_profile
/bin/sh ~/.bash_profile

git config --global user.name sugawa197203
git config --global user.email 96975428+sugawa197203@users.noreply.github.com

npm install -g atcoder-cli

curl -sSf https://rye.astral.sh/get | bash

# rye init

# rye add numpy==1.24.1
# rye add scipy==1.10.1
# rye add scikit-learn==1.30
# rye add numba==0.48.0
# rye add sortedcontainers==2.4.0
# rye add PuLP==2.7.0
# rye add networkx==3.0

npm install -g atcoder-cli
pip install online-judge-tools -y
