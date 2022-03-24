import os
import configparser
from time import time, ctime
import random
import MD5_sample
mode=256
print(os.path.dirname(os.path.abspath('ECC_sample.py')))
print(open('c:\\users\\MC17060010.WMX/Downloads\\Sinacrypto-main\\Cryptology/texto de leer.txt', 'rt').read())
configs=configparser.ConfigParser()
configs.read('settings.ini')
tag=configs['ENCRYPT']['TAG']
print(__file__)
print(tag)
name=a=1
print(MD5_sample.encrypt(random.randbytes(32)))
#log_start_time=ctime(time())
#log="\n starting AES %d encrypt at %s" % (mode, log_start_time)
#open(os.getcwd()+'/'+'encrypt_system.log', 'at').write(log)
print(os.getcwd()+'/tmp')
#open('asdf.tmp', '+wt').write('123')
print(ctime(os.path.getctime('asdf.tmp')))

#print()
#if 'abcde' ~= 'abc':
    