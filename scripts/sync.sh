cd /home/vagrant
svn co http://src.chromium.org/svn/trunk/tools/depot_tools
export PATH="$PATH":`pwd`/depot_tools
#gclient config http://mozc.googlecode.com/svn/trunk/src
#gclient sync
gclient config --name src git+https://code.google.com/p/mocchi-mozc-android/ 
gclient sync
