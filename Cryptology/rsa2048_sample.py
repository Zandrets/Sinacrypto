#LIBRARIES
import os
import rsa
import time

#BIT SIZE FOR ENCRYPTION (MORE REDUCE THE PACKAGE CUANTITY BUT ALSO TAKE MORE TIME TO ENCRYPT)
bits_cnty=2048
(pubkey, privkey) = rsa.newkeys(bits_cnty)

#SIZE OF THE FILE
org_file=open('test_file.rar', 'rb')
org_file.seek(0, os.SEEK_END) #READ FILE SIZE
file_size=org_file.tell() #FILE SIZE
org_file.close
print(file_size)

#ENCRYPT A FILE
inicio_de_encrypt = time.time()
loops=(int(file_size/212)+1)
newfile=open('Topocrypt.rar', 'wb+')
org_file=open('test_file.rar', 'rb')
for partition in range(0, loops):
    crypto=rsa.encrypt(org_file.read(212), pubkey)
    newfile.write(crypto)
newfile.close
org_file.close
final_de_encrypt=time.time()
print('tiempo de encriptado: ', final_de_encrypt - inicio_de_encrypt)

inicio_unencrypt=time.time()
#DECRYPT A FILE
loops=(int(file_size/212)+1)
newfile=open('Topodecrypt.rar', 'wb+')
org_file=open('Topocrypt.rar', 'rb')
for partition in range(0, loops):
    decrypto = rsa.decrypt(org_file.read(256), privkey)
    newfile.write(decrypto)
newfile.close
org_file.close
final_unencrypt=time.time()
print('tiempo de desencriptado: ', final_unencrypt - inicio_unencrypt)
