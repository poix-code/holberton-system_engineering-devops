# The user 'holberton' must be available to login and open files correctly.

# Change the soft value to increase the amounth of open files
exec { 'increase-user-soft-limit':
  command => 'sed -i s/4/5000/ /etc/security/limits.conf',
  path    => '/bin/:/usr/local/bin/'
} ->

# Increase the value of hard nofile, must be above the
# soft value
exec { 'increase-user-hard-limit':
  command => 'sed -i s/5/6000/ /etc/security/limits.conf',
  path    => '/bin/:/usr/local/bin/'
}
