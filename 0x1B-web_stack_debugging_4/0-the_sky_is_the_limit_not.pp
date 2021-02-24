# Increase the 'ULIMIT' value of a server Nginx
exec { 'ulimit-nginx':
  command => 'sed -i s/15/4096/ /etc/default/nginx',
  path    => '/bin/:/usr/local/bin'
} ->

# Restart server
exec { 'restart-server':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
