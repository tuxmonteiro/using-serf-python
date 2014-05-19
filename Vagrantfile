# -*- mode: ruby -*-
# vi: set ft=ruby :
$script = <<SCRIPT

echo Installing depedencies...
sudo apt-get update
sudo apt-get install -y unzip python python-pip g++ build-essential python-dev git

echo Fetching Serf...
cd /tmp/
wget https://dl.bintray.com/mitchellh/serf/0.6.0_linux_amd64.zip -O serf.zip

echo Installing Serf...
unzip serf.zip
sudo chmod +x serf
sudo mv serf /usr/bin/serf
serf agent -bind=$(ip addr | grep 172.20.20 | awk '{ print $2 }' | cut -d'/' -f1) < /dev/null > /tmp/serf.log 2>&1 &

echo Installing serf-python and examples
pip install serf-python
cp -v /vagrant/example?.py ~vagrant/

echo Executing serf-python example
python ~vagrant/example1.py

SCRIPT

# Vagrantfile API/syntax version. Don"t touch unless you know what you"re doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "hashicorp/precise64"

  config.vm.provision "shell", inline: $script

  config.vm.define "n1" do |n1|
      n1.vm.hostname = "n1.localdomain"
      n1.vm.network "private_network", ip: "172.20.20.10"
  end

  config.vm.define "n2" do |n2|
      n2.vm.hostname = "n2.localdomain"
      n2.vm.network "private_network", ip: "172.20.20.11"
  end

  config.vm.define "n3" do |n3|
      n3.vm.hostname = "n3.localdomain"
      n3.vm.network "private_network", ip: "172.20.20.12"
  end

end
