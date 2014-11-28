cd /home/vagrant
sudo apt-get -y update
sudo apt-get -y install ant g++ make python subversion openjdk-6-jdk pkg-config libqt4-dev libzinnia-dev python-cairo
wget -N http://dl.google.com/android/android-sdk_r22.0.5-linux.tgz
wget -N http://dl.google.com/android/ndk/android-ndk-r9-linux-x86.tar.bz2
sudo tar -x -z -f android-sdk_r22.0.5-linux.tgz -C /opt
sudo tar -x -j -f android-ndk-r9-linux-x86.tar.bz2 -C /opt
export PATH=/opt/android-ndk-r9:/opt/android-sdk-linux/tools:/opt/android-sdk-linux/platform-tools:"$PATH"
echo -e "y\n" | sudo android update sdk -u -t build-tools-18.0.1,android-18,platform-tool,tool,extra-android-support
sudo chown -R vagrant.vagrant /opt/android-*
#sudo chown -R vagrant.vagrant ~/.android
sudo cp -a /opt/android-sdk-linux/platforms/android-18/data/fonts/DroidSansFallbackFull.ttf /usr/share/fonts/
sudo cp -a /opt/android-sdk-linux/platforms/android-18/data/fonts/MTLc3m.ttf /usr/share/fonts/
sudo cp -a /opt/android-sdk-linux/platforms/android-18/data/fonts/MTLmr3m.ttf /usr/share/fonts/
svn co http://src.chromium.org/svn/trunk/tools/depot_tools
export PATH="$PATH":`pwd`/depot_tools
gclient config http://mozc.googlecode.com/svn/trunk/src
gclient sync
cp -a /vagrant/scripts/* /home/vagrant/
