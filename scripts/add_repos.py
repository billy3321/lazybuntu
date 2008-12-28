#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright (C) 2007 朱昱任 (Yuren Ju) <yurenju -AT- gmail.com>
# Add source into source.list through arguments.
# Released under GNU General Public License

import aptsources
from aptsources.sourceslist import SourcesList
import aptsources.distro
import sys

def main ():
    uri = sys.argv[1].strip ()
    dist = sys.argv[2].strip ()
    comps = sys.argv[3].split (' ')
    comment = sys.argv[4].strip ()

    distro = aptsources.distro.get_distro ()
    sourceslist = SourcesList ()

    distro.get_sources (sourceslist)
    distro.add_source (uri=uri, dist=dist, comps=comps, comment=comment)

    sourceslist.backup ()
    sourceslist.save ()

    return 0

if __name__ == "__main__":
    main ()

