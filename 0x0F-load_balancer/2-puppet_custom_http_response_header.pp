# Configure the server to return a custom header

package { 'nginx':
    ensure => 'installed',
}

file { '/etc/nginx/conf.d/custom_header.conf':
    ensure  => present,
    content => "add_header X-Served-By ${hostname};",
    notify  => Service['nginx'],
}

service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => File['/etc/nginx/conf.d/custom_header.conf'],
}
