#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2007 朱昱任 (Yuren Ju) <yurenju -AT- gmail.com>
# Copyright (C) 2007 洪任諭(PCMan) <pcman.tw -AT- gmail.com>
# Released under GNU General Public License

import os
from string import Template

def main():
    apt_cmd = "apt-get -y install "

    gcin_text = "gcin \"由台灣網友開發的輸入法，有許多在地化的調校，\n是在臺灣相當受到歡迎的中文輸入法。\n有許多方便的功能，穩定而強大，內建多種輸入法，\n包括功能類似微軟新注音的詞音輸入法、並「可支援無蝦米」。\n但和 Windows 下常見的操作習慣相差不少，新手可能會很不習慣。\n\""
    scim_text = "scim \"Ubuntu 預設的中文輸入法，可以輸入多國文字，功能強大，\n操作和 Windows 上接近，內含類似新注音，相當知名的新酷音輸入法，\n但是比較龐大，目前穩定性也不及 gcin\n\""
    dialog_text = "--text=下列是最常見的二種中文輸入法，'請選擇您喜好的輸入法，\n若您無法決擇，建議可以考慮 gcin：\n'"
    zenity_cmd = Template("zenity --width=512 --height=480 --list --title='選擇輸入法' --column='名稱' --column='敘述' $dialog_text $gcin $scim").substitute(gcin=gcin_text, scim=scim_text, dialog_text=dialog_text)

    fin, fout = os.popen2(zenity_cmd)
    selected_cin = fout.read().strip()

    os.system(apt_cmd + "im-switch")

    if selected_cin == 'gcin' or selected_cin == 'scim':
        os.system(apt_cmd + selected_cin)

        if selected_cin == "scim":
            os.system(apt_cmd + "scim-qtimm scim-chewing")
        elif selected_cin == 'gcin':
            os.system(apt_cmd +'gcin-qt3-immodule' );
            # install noseeing
            # FIXME: 使用者應該可以選擇不要安裝無蝦米
            os.system( 'scripts/noseeing-inst' );

        ims_cmd = "su -c \"im-switch -s %s\" %s" % (selected_cin, os.environ['REAL_USER']) 
        os.system(ims_cmd)

if __name__ == '__main__':
    main()
