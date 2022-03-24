#import Functions as tools
import os
from time import time, ctime, sleep
from random import randbytes as rng
import configparser
import AES_256_sample as AES256
import MD5_sample

#KEYS ALGORITHMS, you can add here your function
def AES(msg, method, msg_type, mode):
    if method == "encrypt":
        #Log section
        log_start_time=ctime(time())
        log="\n starting AES %d encrypt at %s" % (mode, log_start_time)
        open(os.getcwd()+'//'+'encrypt_system.log', 'at').write(log)

        #Preconfig section
        configs=configparser.ConfigParser()
        configs.read('settings.ini')
        tag=configs['ENCRYPT']['TAG']
        if mode == 256 or mode == 128 or mode == 64:
            start_time=time()                       #Start time
            key=AES256.generate_key(mode/8)         #Generates an aleatory key
        else:   return 1                            #Fail reason invalid mode or none one
        if msg_type == "file":
            name=os.path.basename(msg)
            path=os.path.dirname(msg)
            content=open(msg, 'rb').read()          #Open and read the file in binary mode
        elif msg_type == "text":
            name=MD5_sample.encrypt(rng(32))
            path=os.getcwd()+'/tmp'
            content=bytes(msg, 'utf-8')             #Change the message to binary
        else :  return 2                            #Fail reason, invalid message type or none one

        #Encrypt section
        print("encrypting...")
        encrypt=AES256.encrypt(key,content)                                                          #Keep the encrypted data
        open(path+'/'+MD5_sample.encrypt(bytes(log, 'utf-8')), '+wb').write(name)                   #Overwrite the file with the encrypted data
        open(path+'/'+MD5_sample.encrypt(bytes(log, 'utf-8')), 'ab').write(tag)
        open(path+'/'+MD5_sample.encrypt(bytes(log, 'utf-8')), 'ab').write(encrypt)

        #Export section
        log_end_time=ctime(time())
        if log_end_time == log_start_time: sleep(1); log_end_time=ctime(time())
        log="\n ending AES %d encrypt at %s" % (mode, log_end_time)
        os.remove(msg)
        print("exporting key...")
        open(os.getcwd()+'/tmp/'+MD5_sample.encrypt(log, 'utf-8')+'.key', '+wb').write(key)

        #End section
        open(os.getcwd()+'//'+'encrypt_system.log', 'at').write(log)
        return 0

        #CAMBIA EL NOMBRE DEL ARCHIVO CON UN HASH DEL MISMO, BUSCA COMO GUARDAR DICHO NOMBRE Y USA COMO PUNTO ORIGEN EL TIEMPO DE INICIO Y EL TAMANO EN EL LOG

    elif method== "decrypt":
        print(1)
if __name__ == '__main__':
    #FILE MANAGEMENT
    path=os.getcwd()
    file="Topodecrypt.rar"
    #ENCRYPT USAGE
#    print(AES(str(path)+'\\'+file,'encrypt','file',256))      #for files
#    print(AES('text to be encrypted', 'encrypt','text',256))  #for text
#    print(AES(''))