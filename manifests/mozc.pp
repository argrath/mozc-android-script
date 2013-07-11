$user    = 'vagrant'
$group   = 'vagrant'
$homedir = "/home/$user"
$wgetdir = '/opt'
$instdir = '/opt'
$sdkfile = 'android-sdk_r22.0.1-linux.tgz'
$ndkfile = 'android-ndk-r8e-linux-x86.tar.bz2'
$sdkpath = "$wgetdir/$sdkfile"
$ndkpath = "$wgetdir/$ndkfile"
$sdkhome = "$instdir/android-sdk-linux"
$ndkhome = "$instdir/android-ndk-r8e"

Exec {
    timeout => 0,
    user    => $user,
    cwd     => $homedir,
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
      'android-sdk get':
#        require => Package['openjdk-6-jdk'],
        require => Class['packages'],
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
        command => "/bin/echo -e 'y\\n' | $sdkhome/tools/android update sdk -u -t build-tools-17.0.0,extra-android-support,android-17,platform-tool,tool";

      'android-sdk chown':
        command => "/bin/chown -R $user.$group $sdkhome";

      'android-ndk chown':
        command => "/bin/chown -R $user.$group $ndkhome";
    }

    file {
      '/usr/share/fonts/DroidSansFallbackFull.ttf': require => Exec['android update sdk'], source => "$sdkhome/platforms/android-17/data/fonts/DroidSansFallbackFull.ttf";
      '/usr/share/fonts/MTLmr3m.ttf':               require => Exec['android update sdk'], source => "$sdkhome/platforms/android-17/data/fonts/MTLmr3m.ttf";
      '/usr/share/fonts/MTLc3m.ttf':                require => Exec['android update sdk'], source => "$sdkhome/platforms/android-17/data/fonts/MTLc3m.ttf";
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

