import os
import configparser
import pandas as pd
import Functions as tools
from time import time, ctime
import random
import MD5_sample
import re
import AES_256_sample as AES
# mode=256
# print(os.path.dirname(os.path.abspath('ECC_sample.py')))
# #print(open('c:\\users\\MC17060010.WMX/Downloads\\Sinacrypto-main\\Cryptology/texto de leer.txt', 'rt').read())
configs=configparser.ConfigParser()
configs.read(os.path.dirname(__file__)+'/'+'settings.ini')
tag=bytes(configs['ENCRYPT']['TAG'], 'utf-8')
# print(__file__)
# print(tag)
# name=a=1
# print(MD5_sample.encrypt(random.randbytes(32)))
# #log_start_time=ctime(time())
# #log="\n starting AES %d encrypt at %s" % (mode, log_start_time)
# #open(os.getcwd()+'/'+'encrypt_system.log', 'at').write(log)
# #print(os.getcwd()+'/tmp')
# #open('asdf.tmp', '+wt').write('123')
# #print(ctime(os.path.getctime('asdf.tmp')))
# axy='abcde'
# key=AES.generate_key(256/8)
# # text=open(os.path.dirname(__file__)+'/'+'test_file.rar', 'rb').read()
# encrypt=AES.encrypt(key, text)
# decrypt=AES.decrypt(key, encrypt)
# open(os.path.dirname(__file__)+'/'+'result.rar', '+wb').write(decrypt)
# exit()
# print(type(configs['ENCRYPT']['FILE_TYPE']))
# if re.search('axc', axy):
#     print('encontrado')
# #llaves=pd.DataFrame(pd.read_csv(os.path.dirname(os.path.dirname(__file__))+'/'+'sistemas_llaves.csv'))
#print(llaves)
#for i in range(1, 3):
#    print(i)

#class TEST():
#    def __init__(self, *args):
#        print(args[0])
#TEST('a', 'b', 'c')

open('tmp_file.rar', '+wb').write(bytes('nombre_de_prueba.rar', 'utf-8')+tag+open('test_file.rar', 'rb').read())
raw_content=open('tmp_file.rar', 'rb').read()
size=tools.file_reader('./','test_file.rar')
new_size=tools.file_reader('./','tmp_file.rar')
name=''
for i in range(0, new_size):
    s_tag=''
    if chr(raw_content[i]) == chr(tag[0]):
        for j in range(0, len(tag)):
            s_tag=s_tag+chr(raw_content[i+j])
    if s_tag==tag.decode('utf-8'):
        content=b''
        print(chr(raw_content[i+len(tag)]))
        for k in range((i+len(tag)), new_size):
            content=content+bytes([raw_content[k]])
        print((i+len(tag)), size)
        break
    name=name+chr(raw_content[i])
open(name, '+wb').write(content)
print(tools.file_reader('./','test_file.rar') )
print(tools.file_reader('./',name))
#print(name)
