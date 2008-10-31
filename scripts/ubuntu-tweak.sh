#!/bin/bash
# -*- coding: utf-8 -*-
# Copyright (C) 2008 林哲瑋 Zhe-Wei Lin (bill3321,雨蒼) <bill3321 -AT- gmail.com>
# Date: 23 Oct 2008
# Released under GNU General Public License
# Add ubuntu tweak source into source.list and install ubuntu tweak from apt
# Please run as root.



#Check if source.list has source of ubuntu tweak
HAS_UBUNTU_TWEAK=`grep 'deb http://ppa.launchpad.net/tualatrix/ubuntu' /etc/apt/sources.list`
if [ -z "$HAS_UBUNTU_TWEAK" ]; then
    if [ "$DISTRIB_CODENAME" = 'intrepid' ];then
        echo -e "\n#the source of Ubuntu Tweak \ndeb http://ppa.launchpad.net/tualatrix/ubuntu intrepid main \ndeb-src http://ppa.launchpad.net/tualatrix/ubuntu intrepid main" >> /etc/apt/sources.list
    else
        echo -e "\n#the source of Ubuntu Tweak \ndeb http://ppa.launchpad.net/tualatrix/ubuntu hardy main \ndeb-src http://ppa.launchpad.net/tualatrix/ubuntu hardy main" >> /etc/apt/sources.list
    fi
#    wget -q http://ppa.launchpad.net/tualatrix/??-key.gpg -O- | sudo apt-key add - 
     sudo apt-get update
else
    echo 'Ubuntu Tweak 套件庫已經存在'
fi


apt-get -y --force-yes install ubuntu-tweak
