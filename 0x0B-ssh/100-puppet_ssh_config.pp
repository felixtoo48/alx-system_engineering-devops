#!/usr/bin/env bash
# connect with puppet
exec { 'ssh_config':
  path    => '/bin',
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config; echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
}
