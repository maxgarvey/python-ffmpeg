# python-ffmpeg

This library is an effort to make some python wrappers for ffmpeg

### Environment Setup

To set up the development environment, use Vagrant:  
[https://www.vagrantup.com/](https://www.vagrantup.com/)

in the current directory, enter:  
```vagrant up```  
the first time, this will install the prerequisites, including the base box for the VM:  
```ubuntu/trusty64```  
as well as ffmpeg from source. This behavior is all governed by the "setup.sh" script in the base directory of the repository.

### Basic Development

once it's up, enter:  
```vagrant ssh```  
to start a session

After that, it's smooth sailing. To develop on the code:  

`cd /vagrant`  
`. ./ubuntu_env/bin/activate`  
`vim file_name.py`  

### Running Unit Tests

and to run tests:

`cd /vagrant`  
`. ./ubuntu_env/bin/activate`  
`./run_tests.sh`