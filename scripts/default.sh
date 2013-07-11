export PATH=/opt/android-ndk-r8e:/opt/android-sdk-linux/tools:/opt/android-sdk-linux/platform-tools:"$PATH"
cd /home/vagrant/src
python build_mozc.py clean --target_platform=Android
python build_mozc.py gyp --target_platform=Android
python build_mozc.py build_tools -c Release
python build_mozc.py build android/android.gyp:android_manifest
android update project -s -p android --target android-17
python build_mozc.py build android/android.gyp:apk -c Debug_Android 2>&1 | tee /home/vagrant/build.log
mkdir -p /vagrant/build/
cp -a /home/vagrant/build.log /vagrant/build/
cp -a /home/vagrant/src/android/bin/*-debug.apk /vagrant/build/
