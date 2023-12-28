# Puppet file for managing the SSH Client configuration

class ssh_config {
    $ssh_config_file = "/etc/ssh/ssh_config"

    file { $ssh_config_file:
        ensure  => present,
    }

    file_line { 'IdentityFile':
        path    => $ssh_config_file,
        line    => '    IdentityFile ~/.ssh/school',
        match   => '^#? *IdentityFile',
        ensure  => present,
    }

    file_line { 'PasswordAuthentication':
        path    => $ssh_config_file,
        line    => '    PasswordAuthentication no',
        match   => '^#? *PasswordAuthentication',
        ensure  => present,
    }

}

include ssh_config
