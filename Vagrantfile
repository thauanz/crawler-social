# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"
  end

  config.vm.define :master do |cf|
    cf.vm.box = "ubuntu/trusty64"
    cf.vm.network "private_network", ip: "192.168.33.10"
    cf.vm.hostname = "master"
  end

  config.vm.define :node1 do |cf|
    cf.vm.box = "ubuntu/trusty64"
    cf.vm.network "private_network", ip: "192.168.33.11"
    cf.vm.hostname = "node1"
  end

  config.vm.define :node2 do |cf|
    cf.vm.box = "ubuntu/trusty64"
    cf.vm.network "private_network", ip: "192.168.33.12"
    cf.vm.hostname = "node2"
  end

  config.vm.provision "chef_solo" do |chef|
    chef.cookbooks_path = "recipes-chef"
  end
end
