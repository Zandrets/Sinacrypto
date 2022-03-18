from Crypto.Cipher import DES
import os
from time import time
org_file=open('test_file.tmp', 'rb')
org_file.seek(0, os.SEEK_END)
file_size=org_file.tell() #FILE SIZE
org_file.close
print(file_size)

org_file=open('test_file.tmp', 'rb')
new_file=open('encrypt.tmp', 'wb+')
#fill_bit=org_file.read(1048576)
#new_file.write(fill_bit)
#exit()
#def pad(text):
#    n = len(text) % 8
#    return text + (b' ' * n)

#key = b'hello123'
#des = DES.new(key, DES.MODE_ECB)
#padded_text = pad(org_file.read(64))
#encrypted_text = des.encrypt(padded_text)
#print(encrypted_text)

#exit()
key = b'hello123'
start_time_crypt=time()
loops=int((file_size/64)+1)
des = DES.new(key, DES.MODE_OFB)
for loop in range(0,(loops)):
    encrypted_text = des.encrypt(org_file.read(64))
    new_file.write(encrypted_text)
end_time_crypt=time()
org_file.close
new_file.close
#print(encrypted_text)
org_file=open('encrypt.tmp', 'rb')
org_file.seek(0, os.SEEK_END)
actual_size=org_file.tell() #FILE SIZE
org_file.close
print(actual_size)


org_file=open('encrypt.tmp', 'rb')
new_file=open('dencrypt.tmp', 'wb+')
loops=int((file_size/64)+1)

for loop in range(0,(loops)):
    if actual_size >= 64:
        decrypted_text = des.decrypt(org_file.read(64))
        new_file.write(decrypted_text)
end_time_crypt=time()
org_file.close
new_file.close

#file1=open('test_file.tmp', 'rb')
#file2=open('encrypt.tmp', 'rb')
#file3=open('dencrypt.tmp', 'rb')
#print(file1.read())
#print() 
#print(file2.read())
#print()
#print(file3.read())

#        new_file.write(decrypted_text)
#        actual_size=actual_size-64
#    else:
#        decrypted_text = des.decrypt(org_file.read(actual_size), padding=True)
#        print(actual_size)
#        print(decrypted_text)
#        new_file.write(decrypted_text)
