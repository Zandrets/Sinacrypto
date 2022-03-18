import os
import rsa
import time

#print(int(randint(54,200)))
#org_file=open('GNS3 Topology-20220202T182024Z-001.zip', 'rb')
#file=open('test_file.rar','wb+')
#for fill in range(0,1048576):
#    fill_bit=org_file.read(1)
#    file.write(fill_bit)
bits_cnty=512
#(bob_pub, bob_priv) = rsa.newkeys(bits_cnty)
(pubkey, privkey) = rsa.newkeys(bits_cnty)
#message ='hello Bob !'.encode('utf-8')
#crypto = rsa.encrypt(message, bob_pub)
#print (crypto)
#crypto = rsa.decrypt(crypto, bob_priv)
#print (type(crypto))

#SIZE OF THE FILE
org_file=open('test_file.rar', 'rb')
org_file.seek(0, os.SEEK_END)
file_size=org_file.tell() #FILE SIZE
org_file.close
print(file_size)

#COPY OF THE FILE
#org_file=open('GNS3 Topology-20220202T182024Z-001.zip', 'rb')
#newfile=open('test_file.rar', 'wb+')
#newfile.write(org_file.read(file_size))
#newfile.close
#org_file.close

#ENCRYPT A FILE

inicio_de_encrypt = time.time()
loops=(int(file_size/53)+1)
newfile=open('Topocrypt.rar', 'wb+')
org_file=open('test_file.rar', 'rb')
for partition in range(0, loops):
    crypto=rsa.encrypt(org_file.read(53), pubkey)
    newfile.write(crypto)
newfile.close
org_file.close
final_de_encrypt=time.time()
print('tiempo de encriptado: ', final_de_encrypt - inicio_de_encrypt)

inicio_unencrypt=time.time()
#DECRYPT A FILE
loops=(int(file_size/53)+1)
newfile=open('Topodecrypt.rar', 'wb+')
org_file=open('Topocrypt.rar', 'rb')
for partition in range(0, loops):
    decrypto = rsa.decrypt(org_file.read(64), privkey)
    newfile.write(decrypto)
newfile.close
org_file.close
final_unencrypt=time.time()
print('tiempo de desencriptado: ', final_unencrypt - inicio_unencrypt)
