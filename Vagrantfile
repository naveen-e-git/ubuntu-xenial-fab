 Vagrant.configure("2") do |config|
   config.hostmanager.enabled = true
   config.vm.box = "ubuntu/xenial64"
   config.vm.synced_folder "vpro_app", "/root"
   config.vm.network 'public_network'
   config.vm.provision :shell, inline: <<-SHELL
   sudo apt update
   sudo apt install python2.7 -y
   sudo apt update 
   sudo apt install python-pip -y
   sudo pip install --upgrade pip
   sudo apt install fabric -y
   sudo pip install fabric 
   SHELL
 
############################################ INSTALLING CI SERVER ###############################################################################
   config.vm.define "ci" do |build|
     build.vm.hostname = 'build.com'
     build.vm.network "private_network", ip: "192.168.10.20"
     build.vm.provision :shell, inline: <<-SHELL
     sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
     sudo systemctl restart ssh
     sudo apt update
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
     fab app_u 
   SHELL
  end

   config.vm.define "db" do |db|
     db.vm.hostname = 'db.com'
     db.vm.network "private_network", ip: "192.168.10.22"
     db.vm.provision :shell, inline: <<-SHELL
     sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
     sudo systemctl restart ssh
     cd /root
     sudo apt update
     fab db_u
   SHELL
  end

   config.vm.define "lb" do |lb|
     lb.vm.hostname = 'lb.com'
     lb.vm.network "private_network", ip: "192.168.10.23"
     lb.vm.provision :shell, inline: <<-SHELL
     sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
     sudo systemctl restart ssh
     cd /root
     sudo apt update
     fab lb_u
   SHELL
  end

   config.vm.define "mem" do |mem|
     mem.vm.hostname = 'mem.com'
     mem.vm.network "private_network", ip: "192.168.10.24"
     mem.vm.provision :shell, inline: <<-SHELL
     sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
     sudo systemctl restart ssh
     cd /root
     sudo apt update
     fab memcache_u
   SHELL
  end

   config.vm.define "rmq" do |rmq|
     rmq.vm.hostname = 'rmq.com'
     rmq.vm.network "private_network", ip: "192.168.10.25"
     rmq.vm.provision :shell, inline: <<-SHELL
     sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes'/ /etc/ssh/sshd_config
     sudo systemctl restart ssh
     cd /root
     sudo apt update
     fab rabbitmq_u
   SHELL
  end
end
