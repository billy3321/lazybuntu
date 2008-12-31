#!/bin/sh
VERSION="0.1.6"

# build tarball
mkdir -p build/Lazybuntu
cp -r Lazybuntu ui scripts build/Lazybuntu
rm -rf `find build/Lazybuntu/* -name .svn*`
cd build
tar -czf Lazybuntu.tar.gz Lazybuntu
rm -rf Lazybuntu

# build self-extracting file from tarball
gcc `pkg-config gtk+-2.0 --cflags --libs` -o sfx ../sfx.c
strip sfx
echo '_DATA_BEGIN_' | cat sfx - Lazybuntu.tar.gz > Lazybuntu
chmod +x Lazybuntu
rm -f *.tar.gz
tar -czf "Lazybuntu-$VERSION.tar.gz" Lazybuntu
mv *.tar.gz ../
cd ..
rm -rf build
