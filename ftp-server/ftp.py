import logging
import threading
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

class FtpThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.killswitch = threading.Event()
        self.daemon = True  # Установка потока как демона

    def run(self):
        # Настройка авторизатора
        authorizer = DummyAuthorizer()
        authorizer.add_user("horizont", "root", ".", perm="elradfmw")
        authorizer.add_anonymous(".", perm="elradfmw")

        # Настройка обработчика
        handler = FTPHandler
        handler.authorizer = authorizer

        # Настройка логирования
        logging.basicConfig(filename='pyftpd.log', level=logging.INFO)

        # Настройка сервера
        address = ("", 21)
        while(True):
            try:
                self.server = FTPServer(address, handler)
                break
            except:
                print("Waiting while network booting...")
        self.server.max_cons = 256
        self.server.max_cons_per_ip = 5

        # Запуск сервера
        while not self.killswitch.is_set():
            self.server.serve_forever(timeout=1)

    def stop(self):
        # Остановка сервера
        self.killswitch.set()
        self.server.close_all()

def main():
    ftp_server = FtpThread()
    ftp_server.start()  # Запуск сервера в фоновом режиме
    try:
        # Основной поток может выполнять другие задачи
        while True:	
            pass
    except KeyboardInterrupt:
        # Остановка сервера при прерывании
        ftp_server.stop()
        ftp_server.join()  # Дождитесь завершения потока

if __name__ == '__main__':
    main()


