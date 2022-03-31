#LIBRARIES
# import os
# import rsa
# import time
from Crypto.PublicKey import RSA
from random import randint
from Functions import switch
#BIT SIZE FOR ENCRYPTION (MORE REDUCE THE PACKAGE CUANTITY BUT ALSO TAKE MORE TIME TO ENCRYPT)
def generate_priv_key(bits, mode, *args):
    if bits > 1023 and (bits % 256) == 0:
        exp=randint(65537, 99999)
        if (exp%2)==0: exp+=1
        key= RSA.generate(bits, randfunc=None,e=exp)
        if mode == 'file':
            with switch(len(args)) as s:
                if s.case(1): open(args[0],'+wb').write(key.export_key('PEM'))
                if s.case(2): open(args[0],'+wb').write(key.export_key(format=args[1]))
                if s.case(3): open(args[0],'+wb').write(key.export_key(format=args[1], passphrase=args[2]))
                if s.case(4): open(args[0],'+wb').write(key.export_key(format=args[1], passphrase=args[2], pkcs=args[3]))
                if s.case(6): open(args[0],'+wb').write(key.export_key(format=args[1], passphrase=args[2], pkcs=args[3], protection=args[4]))
                if s.case(6): open(args[0],'+wb').write(key.export_key(format=args[1], passphrase=args[2], pkcs=args[3], protection=args[4], randfunc=[5]))
        if mode == 'var':
            return key
def import_key(file, password):

def generate_pub_key(priv_key, struct, mode, *args):
    if struct == 'file':
        if len(args)==1:
            open(args[0], '+wb')
    if struct == 'var':

        return priv_key.publicKey()
# #SIZE OF THE FILE
# org_file=open('test_file.rar', 'rb')
# org_file.seek(0, os.SEEK_END) #READ FILE SIZE
# file_size=org_file.tell() #FILE SIZE
# org_file.close
# print(file_size)
generate_priv_key()

#ENCRYPT A FILE
# inicio_de_encrypt = time.time()
# loops=(int(file_size/212)+1)
# newfile=open('Topocrypt.rar', 'wb+')
# org_file=open('test_file.rar', 'rb')
# # for partition in range(0, loops):
# crypto=rsa.encrypt(org_file.read(), pubkey)
# newfile.write(crypto)
# newfile.close
# org_file.close
# final_de_encrypt=time.time()
# print('tiempo de encriptado: ', final_de_encrypt - inicio_de_encrypt)

# inicio_unencrypt=time.time()
# #DECRYPT A FILE
# loops=(int(file_size/212)+1)
# newfile=open('Topodecrypt.rar', 'wb+')
# org_file=open('Topocrypt.rar', 'rb')
# for partition in range(0, loops):
#     decrypto = rsa.decrypt(org_file.read(256), privkey)
#     newfile.write(decrypto)
# newfile.close
# org_file.close
# final_unencrypt=time.time()
# print('tiempo de desencriptado: ', final_unencrypt - inicio_unencrypt)
