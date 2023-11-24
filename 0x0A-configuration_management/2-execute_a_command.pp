# Create a manifest that kills a process named killmenow

exec { 'Killmenow':
  command     => 'pkill -f killmenow',
  path        => '/bin:/usr/bin:/sbin:/usr/sbin',
} 
