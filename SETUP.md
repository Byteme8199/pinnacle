# Ubuntu Server Setup Guide for Pinnacle Prospects

These instructions are modified from those found at [epicserve].

[epicserve]: https://epicserve-docs.readthedocs.org/en/latest/django/ubuntu-server-django-guide.html

##Step 1: Install Software


Before you begin it might be a good idea to update your system clock
```bash
$ sudo ntpdate time.nist.gov
```
Download lists of new/upgradable packages
```bash
$ sudo aptitude update
```