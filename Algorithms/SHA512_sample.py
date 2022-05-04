import hashlib
import time
inicio_de_encrypt = time.time()
org_file=open('test_file.rar', 'rb')
fill_bit=org_file.read()
salida = hashlib.sha512(fill_bit).hexdigest()
final_de_encrypt=time.time()
print('tiempo de encriptado: ', final_de_encrypt - inicio_de_encrypt)

salida = hashlib.sha256(b"1234").hexdigest()
print(salida)