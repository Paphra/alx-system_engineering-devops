# Install flask from pip3

package { 'python3-pip':
    ensure  => installed,
}

exec { 'install_flask':
    command => '/usr/bin/pip3 install Flask==2.1.0',
    path    => ['/usr/bin'],
    creates => '/usr/local/bin/flask',
    require => Package['python3-pip'],
}