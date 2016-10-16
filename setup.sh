#!/bin/bash

# need to update repoes
sudo apt-get update -y
# and install upgrades
sudo apt-get upgrade -y

# then get python stuff and vim
sudo apt-get install vim python python-pip python-virtualenv wget git gcc yasm dkms -y

# get developer tools
# sudo yum groupinstall "Development Tools" -y

# if ffmpeg command found, then just print 'already installed'
if which ffmpeg; then
  printf 'ffmpeg already installed\n'
else
  printf 'installing ffmpeg (this may take some time...)\n'
  # get ffmpeg sources from the web
  cd ~ && wget https://ffmpeg.org/releases/ffmpeg-snapshot-git.tar.bz2

  # untar sources
  cd ~ && tar -xvjf ffmpeg-snapshot-git.tar.bz2
  cd ~ && rm ffmpeg-snapshot-git.tar.bz2

  cd ~/ffmpeg && sudo configure
  cd ~/ffmpeg && sudo make install
fi
