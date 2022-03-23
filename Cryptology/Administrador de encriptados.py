import Functions as tools
import os
import AES_256_sample as AES256
from time import time, ctime, sleep
import MD5_sample

#KEYS ALGORITHMS, you can add here your function
def AES(msg, method, msg_type, mode):
    if method == "encrypt":
        #Log section
        log_start_time=ctime(time())
        log="\n starting AES %d encrypt at %s" % (mode, log_start_time)
        open(os.getcwd()+'//'+'encrypt_system.log', 'at').write(log)

        #Preconfig section
        if mode == 256 or mode == 128 or mode == 64:
            start_time=time()                       #Start time
            key=AES256.generate_key(mode/8)         #Generates an aleatory key
        else:   return 1                            #Fail reason invalid mode or none one
        if msg_type == "file":
            content=open(msg, 'rb').read()          #Open and read the file in binary mode
        elif msg_type == "text":
            content=bytes(msg, 'utf-8')             #Change the message to binary
        else :  return 2                            #Fail reason, invalid message type or none one

        #Encrypt section
        print("encrypting...")
        encrypt=AES256.encrypt(key,content)                                                          #Keep the encrypted data

        #Export section
        if msg_type == "file":
            output_file=msg
            open(msg, '+wb').write(encrypt)                                                          #Overwrite the file with the encrypted data
        elif msg_type == "text":
            output_file=os.getcwd()+'\\'+MD5_sample.encrypt(bytes(log_start_time, 'utf-8'))+'.tmp'   #Temporal solution, make a new file with the encrypted data, pending to update to multiple OS
            open(output_file, '+wb').write(encrypt)
        else :  return 3
        print("exporting key...")
        open(os.getcwd()+'\\'+MD5_sample.encrypt(bytes(os.path.getctime(output_file)), 'utf-8')+'.key', '+wb').write(key)

        #Log section
        log_end_time=ctime(time())
        if log_end_time == log_start_time: sleep(1); log_end_time=ctime(time())
        log="\n ending AES %d encrypt at %s" % (mode, log_end_time)
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
    print(AES(''))