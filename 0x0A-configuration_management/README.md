# 0x0A. Configuration management
DevOps
SysAdmin
Scripting
CI/CD
# Resources
Read or watch:

Intro to Configuration Management
Puppet resource type: file (check “Resource types” for all manifest types in the left menu)
Puppet’s Declarative Language: Modeling Instead of Scripting
Puppet lint
Puppet emacs mode
# Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

# Install puppet
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet

#Puppet 5 Docs

Install puppet-lint
$ gem install puppet-lint

