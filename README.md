mattwillsher.mysql
==================

This role installs MySQL or its forked upstream version MariaDB. 

It can use two types of repository source - `native`, from the OS default
repositories, and `mariadb`, which uses the repositories at
`http://www.mariadb.org`

Dev/Test environment was created as:

```
virtualenv .venv
. .venv/bin/activate
pip install molecule ansible docker-py
```

The following tests are configured:

* CentOS 7 running upstream MariaDB 10.1 (centos_mariadb)
* CentOS 7 running its default MariaDB version (centos_native)
* Ubuntu 18.04 running its default MySQL version (ubuntu_native)
* Ubuntu 18.04 runnings its native MariaDB verson (ubuntu_native_mariadb)

The can be run with `molecule test --all`

Issues/Todo
-----------

Ubuntu 16.04 is supported by there are issues with molecule test environment
starting the services.

MySQL CE code exists as an alterative source but isn't tested due to issues
with the OS provided MySQL Python libraries not working correctly with it.

Due to https://github.com/ansible/ansible/issues/43255, MariaDB 10.2+ is not
idempotent.

It is assumed the service should run and there are no options to control the
service state beyond starting it at installation. Custom facts are written
for use for service control, package removal.

Requirements
------------

Ubuntu 18.04 CentOS 7 are supported and have automated tests
Ubuntu 16.04, CentOS 6 are supported but don't have tests

For tests, docker is required. See `molecule/README.md`


Role Variables
--------------

### version

Version of MySQL/MariaDB to install.
Optional for `native` installations, if not provided will install the default
OS version of MySQL if available, or MariaDB otherwise. 
On Ubuntu18.04 both MariaDB and MySQL ship. If version is 10.1, MariaDB will
be installed.

Required for MariaDB installation.

### root_password

Optional Password to set for root MySQL user.

### mysql_dbs

Optional databases to be created in the form of a list of dicts:
`[{ name: 'adb'}, {name: 'anotherdb' }]`


### mysql_installation_source

Default: native

Either `native` to install OS provided version of MySQL/MariaDB or
`mariadb` to install from the upstream http://www.mariadb.org repositories

### mysql_mariadb_mirror

Default: https://mirror.sax.uk.as61049.net/mariadb/repo

URL of a mirror of the MariaDB repository without a trailing /

### mysql_native_package_name

Not used by support OSs.

Package name for MySQL from the OS repository. Overridden by OS specific var/
values, but can be used where there are no OS specific var values.

Defaults to `mysql-server`

### mysql_native_service_name

Not used by support OSs.

Name of the service that starts/stops the DB service.

### mysql_skip_preset_vars

Default: false

Skip the support OS values. Useful for overriding values.

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```
---
- hosts: dbservers
  roles:
	  - {
	  role: mattwillsher.mysql,
	  version: 10.1,
	  mysql_installation_source: 'mariadb',
	  root_password: 'mysuperpassword',
	  mysql_databases: [{ name: 'mydb1'}, {name: 'mydb2' }]
	  }
```

License
-------

BSD

Author Information
------------------

Matt Willsher <matt@monki.org.uk>
