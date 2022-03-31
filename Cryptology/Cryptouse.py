#import Functions as tools
import Functions as tools
import os
import re
from time import time, ctime, sleep
from random import randbytes as rng
import configparser
import Algorithms.AES_sc as AES
import MD5_sample



#SYMETRIC ALGORITHMS, you can add here your function
class AES_log_mode():
    def __init__(self, method, *args):
        if method == "encrypt":
            print(self.encrypt(args[0], args[1], args[2]))
        if method == "decrypt":
            print(self.decrypt(args[0], args[1], args[2]))

    def encrypt(self, msg, msg_type, mode):
        #Preconfig section
        configs=configparser.ConfigParser()
        configs.read(os.path.dirname(__file__)+'/'+'settings.ini')
        tag=bytes(configs['ENCRYPT']['TAG'], 'utf8')
        if mode == 256 or mode == 128 or mode == 64:
            start_time=time()                       #Start time
            key=AES.generate_key(mode/8)            #Generates an aleatory key
        else:   return 1                            #Fail reason invalid mode or none one
        if msg_type == "file":
            name=os.path.basename(msg)
            if os.path.dirname(msg) ==  '':
                path=os.getcwd()
            else:
                path=os.path.dirname(msg)
            size=tools.file_reader(path+'/', name)
            extension=configs['ENCRYPT']['FILE_TYPE']
            content=open(msg, 'rb').read()          #Open and read the file in binary mode
        elif msg_type == "text":
            name=MD5_sample.encrypt(rng(32))
            path=os.path.dirname(__file__)+'/tmp'
            extension=configs['ENCRYPT']['MES_TYPE']
            content=bytes(msg, 'utf-8')             #Change the message to binary
            size=len(content)
        else :  return 2                            #Fail reason, invalid message type or none one

        #Log section
        log_start_time=ctime(time())
        log="starting AES %d encrypt of %d bytes at %s\n" % (mode, size, log_start_time)
        open(os.path.dirname(__file__)+'/'+'encrypt_system.log', 'at').write(log)

        #Encrypt section
        for line in open(os.path.dirname(__file__)+'/'+'encrypt_system.log', 'rt').readlines():
            if re.search(log, line):
                log=line
                break
        print("encrypting...")
        encrypt=AES.encrypt(key,content)                                                                                           #Keep the encrypted data
        open(path+'/'+MD5_sample.encrypt(bytes(str(log), 'utf-8'))+extension, '+wb').write(bytes(name, 'utf-8'))                   #Overwrite the file with the encrypted data
        open(path+'/'+MD5_sample.encrypt(bytes(str(log), 'utf-8'))+extension, 'ab').write(tag)
        open(path+'/'+MD5_sample.encrypt(bytes(str(log), 'utf-8'))+extension, 'ab').write(encrypt)

        #Export section
        log_end_time=ctime(time())
        if log_end_time == log_start_time: sleep(1); log_end_time=ctime(time())
        log="ending AES %d encrypt of %d bytes at %s\n" % (mode, size, log_end_time)
        if msg_type == 'file': os.remove(msg)
        print("exporting key...")
        open(os.path.dirname(__file__)+'/tmp/'+MD5_sample.encrypt(bytes(log, 'utf-8'))+'.key', '+wb').write(key)
        #End section
        open(os.path.dirname(__file__)+'/'+'encrypt_system.log', 'at').write(log)
        return 0

    def decrypt(self, msg, msg_type, raw_log):
        configs=configparser.ConfigParser()
        configs.read(os.path.dirname(__file__)+'/'+'settings.ini')
        tag=bytes(configs['ENCRYPT']['TAG'], 'utf-8')
        configs.read(os.path.dirname(__file__)+'/'+'settings.ini')
        raw_data=open(msg, 'rb').read()
        if msg_type == '':
            if re.search(configs['ENCRYPT']['FILE_TYPE'], msg):
                msg_type='file'
                if os.path.dirname(msg) == '':
                    path=os.getcwd()
                else:
                    path=os.path.dirname(msg)
            if re.search(configs['ENCRYPT']['MES_TYPE'], msg):
                msg_type='text'
                path=os.path.dirname(msg)
        raw_content=open(msg, 'rb').read()
        new_size=tools.file_reader(path+'/',os.path.basename(msg))
        name=''
        for i in range(0, new_size):
            s_tag=''
            if chr(raw_content[i]) == chr(tag[0]):
                for j in range(0, len(tag)):
                    s_tag=s_tag+chr(raw_content[i+j])
            if s_tag==tag.decode('utf-8'):
                content=b''
                for k in range((i+len(tag)), new_size):
                    content=content+bytes([raw_content[k]])
                break
            name=name+chr(raw_content[i])
        part=1
        size=len(content)
        key_file=''
        for line in raw_log.readlines():

            if part==1:
                if re.search(ctime(os.path.getctime(msg)), line):
                    if re.search('starting AES', line):
                        if re.search(str(size-8), line) or re.search(str(size-16), line) or re.search(str(size-32), line):
                            if MD5_sample.encrypt(bytes(line, 'utf-8'))+configs['ENCRYPT']['MES_TYPE'] == os.path.basename(msg) or MD5_sample.encrypt(bytes(line, 'utf-8'))+configs['ENCRYPT']['FILE_TYPE'] == os.path.basename(msg):
                                part=2
            if part==2:
                if re.search('ending AES', line):
                    if re.search(str(size-8), line) or re.search(str(size-16), line) or re.search(str(size-32), line):
                        key_file=MD5_sample.encrypt(bytes(line, 'utf-8'))+'.key'
        if key_file=='': return 3
        if msg_type == 'file':
            open(path+'/'+name, '+wb').write(AES.decrypt(open(os.path.dirname(__file__)+'/tmp/'+key_file, 'rb').read(),content))
        if msg_type == 'text':
            print(str(AES.decrypt(open(os.path.dirname(__file__)+'/tmp/'+key_file, 'rb').read(),content), 'utf-8'))
        os.remove(os.path.dirname(__file__)+'/tmp/'+key_file)
        os.remove(msg)
        return 0

if __name__ == '__main__':
    #USAGE FOR AES_log_mode
    #THE FILE MODE MUST NEED TO HAVE A PATH
    file="test_file.rar"
#    print(AES_log_mode('encrypt',file,'file',256))                      #for files
#    print(AES_log_mode('encrypt','text to be encrypted','text',256))   #for text
    print(AES_log_mode('decrypt', os.path.dirname(__file__)+'/tmp/'+'6804e5bbd180a032f7f3e8d0be867262.pqr', '', open(os.path.dirname(__file__)+'/'+'encrypt_system.log', 'rt')))
#    print(AES_log_mode('decrypt', '171325ec01f2c3c40420a1d069626d90.nmo', '', open(os.path.dirname(__file__)+'/'+'encrypt_system.log', 'rt')))