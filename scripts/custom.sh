export PATH=$ANDROID_NDK:$ANDROID_SDK/tools:$ANDROID_SDK/platform-tools:"$PATH"
cd /home/vagrant
python replace.py fix_myapp 2>&1 | tee custom.log
cd /home/vagrant/src
python build_mozc.py clean --target_platform=Android
python build_mozc.py gyp --target_platform=Android --android_application_id mozc.android.yourname.yourappname
python build_mozc.py build_tools -c Release
python build_mozc.py build android/android.gyp:android_manifest
android update project -s -p android --target $ANDROID_API
python build_mozc.py build android/android.gyp:apk -c Debug_Android 2>&1 | tee /home/vagrant/build.log
cd /home/vagrant
python gen_svg.py
python gen_kbd.py
python replace.py fix_myapp fix_tilde fix_flick fix_layout add_kbd2 add_kbd3 add_flick 2>&1 | tee -a custom.log
cd /home/vagrant/src
python build_mozc.py build android/android.gyp:apk -c Debug_Android 2>&1 | tee /home/vagrant/build.log
mkdir -p /vagrant/build/
cp -a /home/vagrant/backup /vagrant/build/
cp -a /home/vagrant/custom /vagrant/build/
cp -a /home/vagrant/custom.log /vagrant/build/
cp -a /home/vagrant/build.log /vagrant/build/
cp -a /home/vagrant/src/android/bin/*-debug.apk /vagrant/build/
