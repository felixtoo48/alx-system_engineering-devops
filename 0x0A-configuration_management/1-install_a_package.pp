# Using puppet, install flask of version 2.1.0

exec { 'install python packages':
  ensure  => '2.1.0',
  command => 'pip3 install flask==2.1.0',
  path    => ['/usr/bin/'],
  unless  => '/usr/bin/test -f /usr/local/lib/python3.8/dist-packages/flask/app.py',
  }
