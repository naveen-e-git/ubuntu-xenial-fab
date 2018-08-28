from fabric.api import *
env.hosts= ['127.0.0.1']
env.user= "vagrant"
env.password= "vagrant"

def if_condition():
    if sudo("uname -a | awk '{print $4}' | cut -b 5-10") == "ubuntu":
       print "THIS IS UBUNTU SERVER"
       ubuntu()
    else:
       print "THIS IS CENTOS SERVER" 
       centos()

   
def ubuntu():
    ci_u()
    app_u()
    db_u()
    lb_u()
    memchace_u()
    rabbitmq_u()

def centos():
    ci_c()
    app_c()
    db_c()
    lb_c()
    memchace_c()
    rabbitmq_c()



def ci_u():
     sudo("apt-get update -y")
     sudo("add-apt-repository ppa:openjdk-r/ppa -y")
     #sudo("apt-get install java* -y")
     sudo("apt-get update")
     sudo("apt-get install openjdk-8-jdk -y ")
     sudo("apt-get  install git -y")
     with cd("/root"):
         sudo("git clone -b vp-rem https://github.com/wkhanvisualpathit/VProfile.git")
         sudo("apt-get install maven -y")
     with cd("/root/VProfile"):
         sudo("sed -i 's/password=password/password=root/g' src/main/resources/application.properties")
         sudo("sed -i 's/newuser/root/g' src/main/resources/application.properties")
         sudo("sed -i 's/localhost:3306/db.com:3306/' src/main/resources/application.properties")
         sudo("sed -i 's/address=127.0.0.1/address='rmq.com'/' src/main/resources/application.properties")
         sudo("sed -i 's/active.host=127.0.0.1/active.host='memcache.com'/' src/main/resources/application.properties")
         sudo("mvn clean install")


def ci_c():
     sudo("yum update")
     sudo("yum install epel-release git -y")
     sudo("yum install  java-1.8.0-openjdk-devel.x86_64 -y")
     sudo("yum update -y")

     with cd("/root"):
       sudo("git clone -b vp-rem https://github.com/wkhanvisualpathit/VProfile.git")
       sudo("yum install maven -y")
       sudo("mvn -version")
     with cd("/root/VProfile"):
       sudo("sed -i 's/password=password/password=root/g' src/main/resources/application.properties")
       sudo("sed -i 's/newuser/root/g' src/main/resources/application.properties")
       sudo("sed -i 's/localhost:3306/db.com:3306/' src/main/resources/application.properties")
       sudo("sed -i 's/address=127.0.0.1/address='rmq.com'/' src/main/resources/application.properties")
       sudo("sed -i 's/active.host=127.0.0.1/active.host='memcache.com'/' src/main/resources/application.properties")
       sudo("mvn clean install")



def app_c():
     sudo("yum update -y")
     sudo("yum install  java-1.8.0-openjdk -y")
     sudo("yum install wget -y")
     with cd("/root"):
         sudo("wget http://www-eu.apache.org/dist/tomcat/tomcat-8/v8.5.33/bin/apache-tomcat-8.5.33.tar.gz")
         sudo("mv apache-tomcat-8.5.33.tar.gz /opt/apache-tomcat-8.5.33.tar.gz")
     with cd("/opt"):
          sudo("tar -xvzf apache-tomcat-8.5.33.tar.gz")
          sudo("rm -rf /opt/apache-tomcat-8.5.33/webapps/ROOT")
          sudo("cp /root/VProfile/target/vprofile-v1.war /opt/apache-tomcat-8.5.33/webapps/ROOT.war")
          sudo("systemctl stop firewalld")
          sudo("systemctl disable firewalld")
          sudo("/opt/apache-tomcat-8.5.33/bin/startup.sh")

def app_u():
     sudo("apt update -y")
     sudo("apt install openjdk-8-jdk -y")
     sudo("apt install wget -y")
     with cd("/root"):
         sudo("wget http://www-eu.apache.org/dist/tomcat/tomcat-8/v8.5.33/bin/apache-tomcat-8.5.33.tar.gz")
         sudo("mv apache-tomcat-8.5.33.tar.gz /opt/apache-tomcat-8.5.33.tar.gz")
     with cd("/opt"):
          sudo("tar -xvzf apache-tomcat-8.5.33.tar.gz")
          sudo("rm -rf /opt/apache-tomcat-8.5.33/webapps/ROOT")
          sudo("cp /root/VProfile/target/vprofile-v1.war /opt/apache-tomcat-8.5.33/webapps/ROOT.war")
          sudo("systemctl stop ufw")
          sudo("ufw disable")
          sudo("/opt/apache-tomcat-8.5.33/bin/startup.sh")



def db_c():
     sudo("yum update -y")
     sudo("yum install mariadb-server -y")
     sudo("systemctl start mariadb")
     sudo("echo \"bind-address = 0.0.0.0\" >> /etc/my.cnf")
     sudo("mysql -u root -e \"create database accounts\" --password='';")
     sudo("mysql -u root -e  \"grant all privileges on *.* TO 'root'@'app.com' identified by 'root'\" --password='';")
     sudo("mysql -u root --password=''  accounts < /root/VProfile/src/main/resources/db_backup.sql;")
     sudo("mysql -u root -e \"FLUSH PRIVILEGES\" --password='';")
     sudo("systemctl start mariadb")

def db_u():
     sudo("debconf-set-selections <<< 'mqsql-server mysql-server/root_password password root'")
     sudo("debconf-set-selections <<< 'mqsql-server mysql-server/root_password_again password root'")
     sudo("apt update -y")
     sudo("apt install mysql-server -y")
     sudo("systemctl start mysql")
     sudo("sed -i 's/127.0.0.1/0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf")
     sudo("mysql -u root -e \"create database accounts\" --password='root';")
     sudo("mysql -u root -e  \"grant all privileges on *.* TO 'root'@'app.com' identified by 'root'\" --password='root';")
     sudo("mysql -u root --password='root' accounts < /root/VProfile/src/main/resources/db_backup.sql;")
     sudo("mysql -u root -e \"FLUSH PRIVILEGES\" --password='root';")
     sudo("systemctl restart mysql")



def lb_c():
     sudo("yum install epel-release -y")
     sudo("yum install nginx -y")
     sudo("cat /root/vproapp  > /etc/nginx/conf.d/vproapp.conf")
     sudo("systemctl stop firewalld")
     sudo("systemctl start nginx")


def lb_u():
     sudo("apt install nginx -y")
     sudo("cp /root/vproapp /etc/nginx/site-available/vproapp")
     sudo("rm -rf /etc/nginx/site-enabled/default")
     sudo("ln -s /etc/nginx/site-available/vproapp /etc/nginx/site-enabled/")
     sudo("sudo systemctl restart nginx")

def memcache_c():
    sudo("yum install memcached -y")
    sudo("memcached -p 11111 -U 11111 -u memcached -d")

def memcache_u():
    sudo("apt install memcached -y")
    sudo("memcached -p 11111 -U 11111 -u memcache -d")

def rabbitmq_u():
    sudo("echo 'deb http://www.rabbitmq.com/debaian/ testing main' | sudo tee /etc/apt/source.list.d/rabbitmq.list")
    sudo("wget -O- https://wwww.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -")
    sudo("wget -O- https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc| sudo apt-key add -")
    sudo("apt-get install rabbitmq-server -y")
    sudo("echo '[{rabbit, [{loopback_users,[]}]}].'> /etc/rabbitmq/rabbitmq.config")
    sudo("rabbitmqctl add_user test test")
    sudo("rabbitmqctl set_user_tags test administrator")


def rabbitmq_c():
    sudo("yum install epel-release -y")
    sudo("yum install wget -y")
    sudo("wget https://github.com/rabbitmq/erlang-rpm/releases/download/v19.3.6.8/erlang-19.3.6.8-1.el7.centos.x86_64.rpm")
    sudo("rpm -ivh erlang-19.3.6.8-1.el7.centos.x86_64.rpm")
    sudo("yum install socat -y")
    sudo("wget https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.10/rabbitmq-server-3.6.10-1.el7.noarch.rpm")
    sudo("rpm --import https://www.rabbitmq.com/rabbitmq-release-signing-key.asc")
    sudo("yum update -y")
    sudo("rpm -ivh rabbitmq-server-3.6.10-1.el7.noarch.rpm")
    sudo("service rabbitmq-server start")
    sudo("service rabbitmq-server status")
    sudo("echo '[{rabbit, [{loopback_users, []}]}].' > /etc/rabbitmq/rabbitmq.config")
    sudo("rabbitmqctl add_user test test")
    sudo("rabbitmqctl set_user_tags test administrator")
