$user     = 'vagrant'
$group    = 'vagrant'
$homedir  = "/home/$user"
$wgetdir  = '/opt'
$instdir  = '/opt'
$sdkfile  = 'android-sdk_r22.3-linux.tgz'
$ndkfile  = 'android-ndk-r9c-linux-x86.tar.bz2'
$sdkpath  = "$wgetdir/$sdkfile"
$ndkpath  = "$wgetdir/$ndkfile"
$sdkhome  = "$instdir/android-sdk-linux"
$ndkhome  = "$instdir/android-ndk-r9c"
$apiver   = 'android-19'
$filter   = "build-tools-19.0.1,$apiver,platform-tool,tool,extra-android-support"
$sdkfonts = "$sdkhome/platforms/$apiver/data/fonts"

Exec {
    timeout     => 0,
    user        => $user,
    cwd         => $homedir,
    environment => ["ANDROID_SDK=$sdkhome", "ANDROID_NDK=$ndkhome", "ANDROID_API=$apiver"],
}

class samba {

    Exec {
        user    => 'root',
    }

    exec {
      'apt-get update':
        command => '/usr/bin/apt-get update';
    }

    package {
      'samba':
        ensure  => latest,
        require => Exec['apt-get update'];
	}

    file {
      '/etc/samba/smb.conf':
        require => Package['samba'],
        source  => '/vagrant/smb.conf',
        owner   => 'root',
        group   => 'root',
        mode    => '0644';
    }

    exec {
      'samba user':
        require => Package['samba'],
        command => "/bin/echo -e '$user\\n$user\\n' | /usr/bin/pdbedit -a $user";
    }

}

include 'samba'

class packages {

    Package {
        ensure  => latest,
#        require => Exec['apt-get update'],
        require => Class['samba'],
    }

    package {
      'ant': ;
      'g++': ;
      'make': ;
      'python': ;
      'subversion': ;
      'openjdk-6-jdk': ;

      'pkg-config': ;
      'libqt4-dev': ;
      'libzinnia-dev': ;

      'python-cairo': ;
#      'apache2': ;
    }

}

include 'packages'

class android {

    Exec {
        user    => 'root',
    }

    exec {
      'android-env':
        require => Class['packages'],
        command => "/bin/echo 'export ANDROID_SDK=$sdkhome ANDROID_NDK=$ndkhome ANDROID_API=$apiver' >> .bashrc";

      'android-sdk get':
#        require => Package['openjdk-6-jdk'],
        require => Exec['android-env'],
        cwd     => $wgetdir,
        command => "/usr/bin/wget -N http://dl.google.com/android/$sdkfile";

      'android-ndk get':
        require => Exec['android update sdk'],
        cwd     => $wgetdir,
        command => "/usr/bin/wget -N http://dl.google.com/android/ndk/$ndkfile";
    }

    file {
      $sdkpath: notify => Exec['android-sdk extract'];
      $ndkpath: notify => Exec['android-ndk extract'];
#      "$sdkhome/tools/android": notify => Exec['android update sdk'];
    }

    exec {
      'android-sdk extract':
        require => Exec['android-sdk get'],
        command => "/bin/tar -x -z -f $sdkpath -C $instdir",
        notify  => Exec['android-sdk chown'],
        creates => $sdkhome;

      'android-ndk extract':
        require => Exec['android-ndk get'],
        command => "/bin/tar -x -j -f $ndkpath -C $instdir",
        notify  => Exec['android-ndk chown'],
        creates => $ndkhome;

      'android update sdk':
        require => Exec['android-sdk extract'],
        notify  => Exec['android-sdk chown'],
#        command => "/bin/echo -e 'y\\n' | $sdkhome/tools/android update sdk -u",
        command => "/bin/echo -e 'y\\n' | $sdkhome/tools/android update sdk -u -a -t $filter",
        creates => $sdkfonts;

      'android-sdk chown':
        command => "/bin/chown -R $user.$group $sdkhome";

      'android-ndk chown':
        command => "/bin/chown -R $user.$group $ndkhome";
    }

    file {
      '/usr/share/fonts/DroidSansFallbackFull.ttf': require => Exec['android update sdk'], source => "$sdkfonts/DroidSansFallbackFull.ttf";
      '/usr/share/fonts/MTLmr3m.ttf':               require => Exec['android update sdk'], source => "$sdkfonts/MTLmr3m.ttf";
      '/usr/share/fonts/MTLc3m.ttf':                require => Exec['android update sdk'], source => "$sdkfonts/MTLc3m.ttf";
    }

}

include 'android'

exec {
  'scripts':    require => Class['android'],   command => "/bin/cp -a /vagrant/scripts/* $homedir";
  'sync.sh':    require => Exec['scripts'],    command => "/bin/sh $homedir/sync.sh";
  'default.sh': require => Exec['sync.sh'],    command => "/bin/sh $homedir/default.sh";
  'custom.sh':  require => Exec['default.sh'], command => "/bin/sh $homedir/custom.sh";
# 'build.sh':   require => Exec['sync.sh'],    command => "/bin/sh $homedir/build.sh";
}

