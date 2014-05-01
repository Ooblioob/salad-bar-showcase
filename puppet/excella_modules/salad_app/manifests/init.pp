class salad_app {

  package { "python":
    ensure => installed,
  }

  package { "git": 
    ensure => latest,
  }

  package { "python-pip":
    ensure => installed,
    require => Package['python'],
  }

  exec { "install python packages":
    command => "/usr/bin/pip install -r /www/requirements.txt",
    require => Package['python-pip'],
    before => Class["jenkins::package"],
  }

  exec { "django syncdb":
    command => "/www/manage.py syncdb --noinput",
    require => Exec['install python packages'],
  }

  supervisor::program { 'saladbar':
    ensure => present,
    enable => true,
    command => '/usr/bin/gunicorn saladbar.wsgi:application',
    directory => '/www',
    user => 'vagrant',
    group => 'vagrant',
    require => Exec['django syncdb'],
  }

  file { "/var/static":
    ensure => directory,
    owner => 'vagrant',
    group => 'vagrant',
  }

  exec { "collectstatic":
    command => "/www/manage.py collectstatic --noinput",
    user => vagrant,
    require => [File['/var/static'],
                Exec['install python packages']],
  }

  class { 'nginx':
    require => File['/var/static'],
  }

  nginx::resource::upstream { 'saladbar':
    members => [
      'localhost:8000',
    ],
  }

  nginx::resource::upstream { 'jenkins':
    members => [
      'localhost:8001',
    ],
  }

  nginx::resource::vhost { 'saladbar-host':
    ensure => present,
    use_default_location => false,
    proxy_set_header => [ 'X-Forwarded-For $proxy_add_x_forwarded_for', 'Host $http_host' ],
  } 

  nginx::resource::location { "/":
    ensure => present,
    vhost => 'saladbar-host',
    proxy  => 'http://saladbar',
  }

  nginx::resource::location { "saladbar-static":
    ensure => present,
    vhost => 'saladbar-host',
    location => '/static',
    www_root => '/var/',
  }

  nginx::resource::location { "/jenkins":
    ensure => present,
    vhost => 'saladbar-host',
    proxy  => 'http://jenkins',
  }

  class { 'jenkins':
    config_hash => {
      'JENKINS_PORT' => { 'value' => '8001' },
      'JENKINS_ARGS' => { 'value' => '--prefix="/jenkins"' }
    }
  }

  jenkins::plugin {
    "git-client" : ;
    "multiple-scms" : ;
    "scm-api": ;
    "git" : ;
    "violations" : ;
    "cobertura" : ;
    "dashboard-view" : ;
    "startup-trigger-plugin" : ;
  }

  jenkins_config::load { "saladbar":
    import_source => 'modules/salad_app/saladbar_config.xml',
    jenkins_url => 'http://127.0.0.1:8001/jenkins',
  }
}
