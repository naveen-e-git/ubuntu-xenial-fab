 Vagrant.configure("2") do |config|
   config.hostmanager.enabled = true
   config.vm.box = "ubuntu/xenial64"
   config.vm.synced_folder "vpro_app", "/root"
   config.vm.network 'public_network'
 
############################################ INSTALLING CI SERVER ###############################################################################
   config.vm.define "ci" do |build|
     build.vm.hostname = 'build.com'
     build.vm.network "private_network", ip: "192.168.10.20"
     build.vm.provision :shell, inline: <<-SHELL
     sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
     sudo systemctl restart ssh
     sudo apt update
     sudo apt install python2.7 -y
     sudo apt update 
     sudo apt install python-pip -y
     sudo pip install --upgrade pip
     sudo apt install fabric -y
     sudo pip install fabric 
     cd /root
     fab ci_u
   SHELL
  end

   config.vm.define "app" do |app|
     app.vm.hostname = 'app.com'
     app.vm.network "private_network", ip: "192.168.10.21"
     app.vm.provision :shell, inline: <<-SHELL
     sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
     sudo systemctl restart ssh
     cd /root
     sudo yum update
     sudo yum install epel-release -y
     sudo yum update
     echo "installing python"
     sudo yum install python2.7 -y
     sudo yum update
     sudo yum install python-pip -y
     sudo yum install --upgrade pip
     sudo yum install fabric -y
     #sudo pip install fabric
      fab app_c 
     #fab -f /vagrant/vpro_app/fabfile.py app_c
   SHELL
  end

   config.vm.define "db" do |db|
     db.vm.hostname = 'db.com'
     db.vm.network "private_network", ip: "192.168.10.22"
     db.vm.provision :shell, inline: <<-SHELL
     sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
     sudo service sshd restart
     cd /root
     sudo yum update
     sudo yum install epel-release -y
     sudo yum update
     echo "installing python"
     sudo yum install python2.7 -y
     sudo yum update
     sudo yum install python-pip -y
     sudo yum install --upgrade pip
     sudo yum install fabric -y
     #sudo pip install fabric
     fab -f /vagrant/vpro_app/fabfile.py db_c
   SHELL
  end

   config.vm.define "lb" do |lb|
     lb.vm.hostname = 'lb.com'
     lb.vm.network "private_network", ip: "192.168.10.23"
     lb.vm.provision :shell, inline: <<-SHELL
     sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
     sudo service sshd restart
     cd /root
     sudo yum update
     sudo yum install epel-release -y
     sudo yum update
     echo "installing python"
     sudo yum install python2.7 -y
     sudo yum update
     sudo yum install python-pip -y
     sudo yum install --upgrade pip
     sudo yum install fabric -y
     #sudo pip install fabric
     fab -f /vagrant/vpro_app/fabfile.py lb_c
   SHELL
  end

   config.vm.define "mem" do |mem|
     mem.vm.hostname = 'mem.com'
     mem.vm.network "private_network", ip: "192.168.10.24"
     mem.vm.provision :shell, inline: <<-SHELL
     sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
     sudo service sshd restart
     cd /root
     sudo yum update
     sudo yum install epel-release -y
     sudo yum update
     echo "installing python"
     sudo yum install python2.7 -y
     sudo yum update
     sudo yum install python-pip -y
     sudo yum install --upgrade pip
     sudo yum install fabric -y
     #sudo pip install fabric
     fab -f /vagrant/vpro_app/fabfile.py memcache_c
   SHELL
  end

   config.vm.define "rmq" do |rmq|
     rmq.vm.hostname = 'rmq.com'
     rmq.vm.network "private_network", ip: "192.168.10.25"
     rmq.vm.provision :shell, inline: <<-SHELL
     sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
     sudo service sshd restart
     cd /root
     sudo yum update
     sudo yum install epel-release -y
     sudo yum update
     echo "installing python"
     sudo yum install python2.7 -y
     sudo yum update
     sudo yum install python-pip -y
     sudo yum install --upgrade pip
     sudo yum install fabric -y
     #sudo pip install fabric
     fab -f /vagrant/vpro_app/fabfile.py rabbitmq_c
   SHELL
  end
end
