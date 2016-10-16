#!/bin/bash

# need to update repoes
sudo yum update -y
# and install upgrades
sudo yum upgrade

# then get python stuff and vim
sudo yum install vim python python-pip python-virtualenv epel-release wget git gcc yasm -y

# if ffmpeg command found, then just print 'already installed'
if which ffmpeg; then
  printf 'ffmpeg already installed\n'
else
  printf 'installing ffmpeg (this may take some time...)\n'
  # get ffmpeg sources from the web
  wget https://ffmpeg.org/releases/ffmpeg-snapshot-git.tar.bz2

  # untar sources
  tar -xvjf ffmpeg-snapshot-git.tar.bz2
  rm ffmpeg-snapshot-git.tar.bz2

  sudo ffmpeg/configure
  sudo cd ffmpeg && make install
fi