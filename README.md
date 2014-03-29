salad-bar-showcase
==================

A simple website built using a full suite of open source technologies


#Setup:
* Download vagrant and virtualbox
* Clone this repo
* From the root of this repo, create and provision the virtual machine `vagrant up`
* The website will be available from a browser on the host computer at `http://127.0.0.1:8080/`


##Notable tools:
* [Puppet](http://puppetlabs.com/) - provision applications and configurations
* [Django](http://www.djangoproject.com/) - Python application framwork
* [Jenkins](http://jenkins-ci.org/) - Continuous integration server

##Other contributing tools:
* [Vagrant](http://www.vagrantup.com/) - create virtualbox servers
* [Gunicorn](http://gunicorn.org/) - WSGI application server
* [Nginx](http://wiki.nginx.org/Main) - HTTP server
* [Supervisor](http://supervisord.org/) - process monitoring
* [JQuery](http://jquery.com/) - Javascript library
* [Librarian-puppet](https://github.com/rodjek/librarian-puppet) - puppet module manager
