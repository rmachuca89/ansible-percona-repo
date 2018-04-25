Ansible Percona Repo Role
=========================
[![Build Status](https://travis-ci.org/rmachuca89/ansible-repo-percona.svg?branch=master)](https://travis-ci.org/rmachuca89/ansible-repo-percona)

A simple ansible role to install the [Percona Repository](https://www.percona.com/doc/percona-repo-config/index.html) on RHEL/CentOS and Debian/Ubuntu based machines.

Requirements
------------

- A RHEL/CentOS or Debian/Ubuntu based OS target host.
- ansible >= 2.4

Role Variables
--------------

None.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: dbs
  roles:
      - repo-percona
```

License
-------

Apache 2.0

Author Information
------------------

Rodrigo Machuca
