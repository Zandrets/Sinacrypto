import hashlib
import time
def encrypt(data):
    return hashlib.md5(data).hexdigest()

if __name__ == "__main__":    
    print(type(encrypt(bytes('text to encrypt', 'utf8'))))
#    inicio_de_encrypt = time.time()
#    org_file=open('test_file.rar', 'rb')
#    fill_bit=org_file.read()
#    salida = hashlib.md5(fill_bit).hexdigest()
#    final_de_encrypt=time.time()
#    print('tiempo de encriptado: ', final_de_encrypt - inicio_de_encrypt)
#    salida = hashlib.sha256(b"1234").hexdigest()
#    print(type(salida))