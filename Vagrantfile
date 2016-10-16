Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.synced_folder ".", "/vagrant"  #, type: "rsync", rsync__exclude: ".git/", rsync__args: ["--rsync-path='sudo rsync'"]
  config.vm.provision :shell, :path => "setup.sh"
end
