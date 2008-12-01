#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import aptsources
from aptsources.sourceslist import SourcesList
import aptsources.distro

def main ():
    comps = []
    sourceslist = SourcesList ()
    distro = aptsources.distro.get_distro ()
    security_uri = ""
    security_dist = ""

    if distro.id == "Debian":
        comps = ["main", "contrib", "non-free"]
        security_uri = "http://security.debian.org/"
        security_dist = "%s/updates" % distro.codename
    elif distro.id == "Ubuntu":
        comps = ["main", "universe", "restricted", "multiverse"]
        security_uri = "http://security.ubuntu.com/ubuntu/"
        security_dist = "%s-security" % distro.codename
    else:
        print "can't identify distribution"
        return -1

    try:
        distro.get_sources (sourceslist)
    except:
        print "your distribution is remix release!"
        return -1

    [entry.set_enabled (False) for entry in sourceslist if entry.invalid == False]

    if distro.country_code == "tw" and distro.id == "Ubuntu":
        twaren_uri = "ftp://ftp.twaren.net.tw/ubuntu"
        distro.change_server (uri=twaren_uri)
        distro.add_source (uri=twaren_uri, comps=comps, comment="國網中心伺服器 (Lazybuntu 新增)")
        distro.add_source (type="deb-src", uri=twaren_uri, comps=comps, comment="國網中心伺服器 (Lazybuntu 新增)")
    else:
        distro.add_source (uri=distro.nearest_server, comps=comps, comment="地區性伺服器 (Lazybuntu 新增)")
        distro.add_source (type="deb-src", uri=distro.nearest_server, comps=comps, comment="地區性伺服器 (Lazybuntu 新增)")

    distro.add_source (uri=security_uri, dist=security_dist, comps=comps, comment="安全性更新伺服器 (Lazybuntu 新增)")
    distro.add_source (type="deb-src", uri=security_uri, dist=security_dist, comps=comps, comment="安全性更新伺服器 (Lazybuntu 新增)")

    sourceslist.backup ()
    sourceslist.save ()

    return 0

if __name__ == "__main__":
    main ()

