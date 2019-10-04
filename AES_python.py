from Crypto.Cipher import AES
import random
import string
import time
key = b'Sixteen byte key'
data=b'himynameisjackie'

stt = time.time()
for x in range(1000):
    cipher = AES.new(key, AES.MODE_ECB, use_aesni=True)
    ciphertext= cipher.encrypt(data)

    cipher = AES.new(key, AES.MODE_ECB, use_aesni=True)
    plaintext = cipher.decrypt(ciphertext)
    #print("The encrypted messageis: ", ciphertext)
ett = time.time()

dif = ett-stt
print("time for AES_NI :", dif)


fstt = time.time()
for x in range(1000):
    cipher = AES.new(key, AES.MODE_ECB, use_aesni=False)
    ciphertext= cipher.encrypt(data)
    cipher = AES.new(key, AES.MODE_ECB, use_aesni=False)
    plaintext = cipher.decrypt(ciphertext)
    
fett = time.time()

fdif = fett-fstt
print("time for AES:", fdif)
   
   
#     #print("The message is authentic:", plaintext)       

# #cipher = AES.new(key, AES.MODE_ECB, use_aesni=True)

# #ciphertext= cipher.encrypt(data)
# #print("The encrypted messageis: ", ciphertext)

# ##/key = b'Sixteen byte key'
# cipher = AES.new(key, AES.MODE_ECB, use_aesni=True)
# plaintext = cipher.decrypt(ciphertext)
# #print("The message is authentic:", plaintext
