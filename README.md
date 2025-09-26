```shell
sudo apt update; sudo apt upgrade
sudo apt install mysql-server libmysqlclient-dev pkg-config python3-pip
sudo mysql -e 'CREATE USER `manager`@`localhost` IDENTIFIED BY "aSQucwuVvu6hEwwF"; CREATE DATABASE `gallery`; GRANT ALL ON `gallery`.* TO `manager`@`localhost`;'
git clone https://github.com/JaydenKing32/gallerysite.git
cd gallerysite
sudo pip install -r requirements.txt
cp config_blank.json config.json
nano config.json # Add config info
python3 manage.py migrate
sudo python3 manage.py runserver 0.0.0.0:80
```
