# Puppet file for managing the SSH Client configuration

$ssh_config_file = '/etc/ssh/ssh_config'
file { $ssh_config_file:
    ensure  => present,
}
file_line { 'IdentityFile':
    ensure => present,
    path   => $ssh_config_file,
    line   => '	IdentityFile ~/.ssh/school',
    match  => '^#? *IdentityFile',
}
file_line { 'PasswordAuthentication':
    ensure => present,
    path   => $ssh_config_file,
    line   => '    PasswordAuthentication no',
    match  => '^#? *PasswordAuthentication',
}
