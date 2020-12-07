# Using Puppet to install 'puppet-lint'
package {'install-puppet-lint':
  name     => 'puppet-lint',
  ensure   => '2.1.1',
  provider => gem,
}