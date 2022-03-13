import time
import atgparse
import logging
import sys
import signal
import os
from pid import pid_process

logger = logging.getLogger('weather_daemon')
logger.setLevel(logging.INFO)
formatstr = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(formatstr)

def terminate(signalNumber, frame):
	"""
	Здесь мы можем обработать завершение нашего приложения
	Главное не забыть в конце выполнить выход sys.exit()
	"""
	pid = pid_process("/opt/mygits/Sinoptok/start.py")
	os.system("sudo kill pid")
	logger.info(f'Recieved {signalNumber}')
	sys.exit()

def do_something():
	"""
	Здесь мы только лишь пишем сообщение в Log, но можем реализовать
	абсолютно любые задачи выполняемые в фоне.
	"""
	while True:
		if len(pid_process("/opt/mygits/Sinoptik/start.py"))>0:
			logger.info("Всё чики-брики")
		else: 
			os.system("sudo python3 /opt/mygits/Sinoptik/start.py &")
			logger.info("Бот запущен")
		time.sleep(30)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Example daemon in Python")
	# Мы можем заменить default или запускать приложение с указанием нахождения 
	# log файла, через параметр -l /путь_к_файлу/файл.log
	parser.add_argument('-l', '--log-file', default='/home/ubuntu/weather_daemon.log')
	args = parser.parse_args()
	
	signal.signal(signal.SIGTERM, terminate)

	fh = logging.FileHandler(args.log_file)
	fh.setLevel(logging.INFO)
	fh.setFormatter(formatter)
	logger.addHandler(fh)
    
	do_something()

