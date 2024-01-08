# Setup the nginx server using puppet manifest

package { 'nginx':
    ensure => 'installed',
}

service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
    ensure  => 'present',
    content => '# File: templates/default.erb
    server {
        listen 80;
        root /var/www/html;
        index index.html;

        location = /404.html {
            root /var/www/html;
            internal;
        }

        error_page 404 /404.html;

        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
    }',
    notify  => Service['nginx'],
}

file { '/var/www/html/index.html':
    ensure  => 'present',
    content => 'Hello World!',
}

file { '/var/www/html/404.html':
    ensure  => 'present',
    content => "Ceci n'est pas une page",
}
