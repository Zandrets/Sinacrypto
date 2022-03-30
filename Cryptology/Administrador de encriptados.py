#import Functions as tools
import Functions as tools
import os
import re
from time import time, ctime, sleep
from random import randbytes as rng
import configparser
import AES_256_sample as AES256
import MD5_sample

#KEYS ALGORITHMS, you can add here your function
class AES_log_mode():
    def __init__(self, method, *args):
        if method == "encrypt":
            self.encrypt(args[0], args[1], args[2])
        if method == "decrypt":
            self.decrypt(args[0], args[1], args[2])
        #Log section
    def encrypt(self, msg, msg_type, mode):
        log_start_time=ctime(time())
        log="\n starting AES %d encrypt at %s" % (mode, log_start_time)
        open(os.path.dirname(__file__)+'/'+'encrypt_system.log', 'at').write(log)

        #Preconfig section
        configs=configparser.ConfigParser()
        configs.read(os.path.dirname(__file__)+'/'+'settings.ini')
        tag=bytes(configs['ENCRYPT']['TAG'], 'utf8')
        if mode == 256 or mode == 128 or mode == 64:
            start_time=time()                       #Start time
            key=AES256.generate_key(mode/8)         #Generates an aleatory key
        else:   return 1                            #Fail reason invalid mode or none one
        if msg_type == "file":
            name=os.path.basename(msg)
            path=os.path.dirname(msg)
            extension=configs['ENCRYPT']['FILE_TYPE']
            content=open(msg, 'rb').read()          #Open and read the file in binary mode
        elif msg_type == "text":
            name=MD5_sample.encrypt(rng(32))
            path=os.path.dirname(__file__)+'/tmp'
            extension=configs['ENCRYPT']['MES_TYPE']
            content=bytes(msg, 'utf-8')             #Change the message to binary
        else :  return 2                            #Fail reason, invalid message type or none one

        #Encrypt section
        print("encrypting...")
        encrypt=AES256.encrypt(key,content)                                                                   #Keep the encrypted data
        open(path+'/'+MD5_sample.encrypt(bytes(log, 'utf-8'))+extension, '+wb').write(name)                   #Overwrite the file with the encrypted data
        open(path+'/'+MD5_sample.encrypt(bytes(log, 'utf-8'))+extension, 'ab').write(tag)
        open(path+'/'+MD5_sample.encrypt(bytes(log, 'utf-8'))+extension, 'ab').write(encrypt)

        #Export section
        log_end_time=ctime(time())
        if log_end_time == log_start_time: sleep(1); log_end_time=ctime(time())
        log="\n ending AES %d encrypt at %s" % (mode, log_end_time)
        os.remove(msg)
        print("exporting key...")
        open(os.path.dirname(__file__)+'/tmp/'+MD5_sample.encrypt(log, 'utf-8')+'.key', '+wb').write(key)
        #End section
        open(os.path.dirname(__file__)+'/'+'encrypt_system.log', 'at').write(log)
        return 0

    def decrypt(self, msg, msg_type, raw_data):
        configs=configparser.ConfigParser()
        tag=bytes(configs['ENCRYPT']['TAG'], 'utf-8')
        configs.read(os.path.dirname(__file__)+'/'+'settings.ini')
        raw_data=open(msg, 'rb').read()
        if msg_type == '':
            if re.search(configs['ENCRYPT']['FILE_TYPE'], msg):
                msg_type='file'
            if re.search(configs['ENCRYPT']['MES_TYPE'], msg):
                msg_type='text'
        open('tmp_file.rar', '+wb').write(bytes('nombre_de_prueba.rar', 'utf-8')+tag+open('test_file.rar', 'rb').read())
        raw_content=open(msg, 'rb').read()
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
                print((i+len(tag)), new_size)
                break
            name=name+chr(raw_content[i])
        open(os.path.dirname(msg)+'/'+name, '+wb').write(content)
        os.remove(msg)


        if msg_type == 'file':
            a=1
        if msg_type == 'text':
            b=1

if __name__ == '__main__':
    #FILE MANAGEMENT
    path=os.getcwd()
    file="Topodecrypt.rar"
    #ENCRYPT USAGE
#    print(AES(str(path)+'\\'+file,'encrypt','file',256))      #for files
#    print(AES('text to be encrypted', 'encrypt','text',256))  #for text
#    print(AES(''))
