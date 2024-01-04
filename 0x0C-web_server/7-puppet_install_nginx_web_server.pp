# Setup the nginx server using puppet manifest

class { 'nginx':
  ensure => 'installed',
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  notify  => Service['nginx'],
}

nginx::resource::vhost { 'redirect_me':
  www_root     => '/var/www/html',
  listen_port  => 80,
  server_name  => 'localhost',
  redirect_dest => 'https://www.youtube.com/watch?v=QH2-TGUlwu4',
  redirect_type => 'Permanent',
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  require   => [File['/etc/nginx/sites-available/default'], File['/var/www/html/index.html']],
}
