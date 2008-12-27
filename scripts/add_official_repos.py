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

    for source in sourceslist:
     if source.disabled == False:
      if source.uri == "http://packages.medibuntu.org/":
       has_medibuntu_source = 1
      if source.uri == "http://ppa.launchpad.net/tualatrix/ubuntu":
       has_ubuntu_tweak_source = 1
      if source.uri == "http://getswiftfox.com/builds/debian":
       has_swiftfox_source = 1
      if source.uri == "http://wine.budgetdedicated.com/apt":
       has_winehq_source = 1

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

    if has_medibuntu_source:
       medibuntu_uri = "http://packages.medibuntu.org/"
       medibuntu_comps = ["free non-free"]
       distro.add_source (uri=medibuntu_uri, comps=medibuntu_comps, comment="Medibuntu Install Source")
    if has_ubuntu_tweak_source:
       ubuntu_tweak_uri = "http://ppa.launchpad.net/tualatrix/ubuntu"
       ubuntu_tweak_comps = ["main"]
       if distro.codename == 'intrepid':
          ubuntu_tweak_dist = distro.codename
       else:
          ubuntu_tweak_dist = 'hardy'
       distro.add_source (uri=ubuntu_tweak_uri, dist=ubuntu_tweak_dist, comps=ubuntu_tweak_comps, comment="Ubuntu Tweak Install Source")
       distro.add_source (type="deb-src", uri=ubuntu_tweak_uri, dist=ubuntu_tweak_dist, comps=ubuntu_tweak_comps, comment="Ubuntu Tweak Install Source")
    if has_swiftfox_source:
       swiftfox_uri = "http://getswiftfox.com/builds/debian"
       swiftfox_comps = ["non-free"]
       swiftfox_dist = "unstable"
       distro.add_source (uri=swiftfox_uri, dist=swiftfox_dist, comps=swiftfox_comps, comment="Swiftfox Install Source")
    if has_winehq_source:
       winehq_uri = "http://wine.budgetdedicated.com/apt"
       winehq_comps = ["main"]
       distro.add_source (uri=winehq_uri, comps=winehq_comps, comment="WineHQ Install Source")


    sourceslist.backup ()
    sourceslist.save ()

    return 0

if __name__ == "__main__":
    main ()

