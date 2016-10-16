#!/bin/bash

# need to update repoes
sudo yum update -y
# and install upgrades
sudo yum upgrade

# then get python stuff and vim
sudo yum install vim python python-pip python-virtualenv epel-release wget git gcc yasm

# get ffmpeg sources from the web
wget https://ffmpeg.org/releases/ffmpeg-snapshot-git.tar.bz2

# untar sources
tar -xvjf ffmpeg-snapshot-git.tar.bz2
