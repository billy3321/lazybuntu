#!/bin/bash
# -*- coding: utf-8 -*-
# Copyright (C) 2008 林哲瑋 Zhe-Wei Lin (bill3321,雨蒼) <bill3321 -AT- gmail.com>
# Last Modified: 25 Nov 2008
# Released under GNU General Public License
# Download and install skype for i686 and x86_64
# Please run as root.

echo "下載並安裝skype網路電話..."

case "$ARCH_NAME" in
i686)
scripts/download-install skype 'http://www.skype.com/go/getskype-linux-ubuntu'
;;
x86_64)
scripts/download-install skype 'http://www.skype.com/go/getskype-linux-ubuntu-amd64'
;;
*)
echo "抱歉，Lazybuntu目前尚未支援$ARCH_NAME硬體架構。"
# 若仍有其他硬體架構請加於此
;;
esac
