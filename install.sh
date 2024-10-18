#!bin/bash

# Файл для уставновки програмнного обеспечения
# Перед запуском произведите команду: chmod +x install.sh
# После выполните команду: sh ./install.sh

#----------------------------------------------------------------#
#----------------Установка и наладка ftp сервера-----------------#
#----------------------------------------------------------------#

# Загрузка необходимых библиотек python
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install pyftpdlib

# Отключение старого ftp сервера
sudo systemctl stop proftpd.service
sudo systemctl disable proftpd.service
sudo systemctl status proftpd.service

# Создание собсвенного сервиса для ftp сервера
# Создание файла службы systemd
SERVICE_FILE="/etc/systemd/system/pyftpd.service"

echo "[Unit]
Description=My Python Script Daemon
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/rk3568-soft/ftp-server/ftp.py
Restart=always
User=root
WorkingDirectory=/home/rk3568-soft/ftp-server/

[Install]
WantedBy=multi-user.target" | sudo tee $SERVICE_FILE

# Перезагрузка конфигурации systemd
sudo systemctl daemon-reload

# Запуск и включение службы
sudo systemctl start pyftpd.service
sudo systemctl enable pyftpd.service
sudo systemctl status pyftpd.service

#----------------------------------------------------------------#
#----------------Установка и наладка ftp сервера-----------------#
#----------------------------------------------------------------#



#----------------------------------------------------------------#
#---------------Установка и наладка uart логгера-----------------#
#----------------------------------------------------------------#

# Загрузка необходимых библиотек python
sudo python3 -m pip install pyserial
sudo python3 -m pip install asyncio


#----------------------------------------------------------------#
#---------------Установка и наладка uart логгера-----------------#
#----------------------------------------------------------------#
