import pickle5 as pickle
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
# initializing data to be stored in db 
from Crypto.Random import get_random_bytes
key = get_random_bytes(24)

BLOCK_SIZE = 16
cipher = AES.new(key, AES.MODE_ECB)
print("enter plain text")
plaintext = input()
plaintext = plaintext.encode()
ciphertext = cipher.encrypt(pad(plaintext, BLOCK_SIZE))
print("The corresponding cipher text",ciphertext)

# data
db = {} 
db['key'] = key 
db['ciphertext'] = ciphertext
db['blocksize'] = BLOCK_SIZE

# Its important to use binary mode 
dbfile = open('project_2', 'wb') 
# source, destination 
pickle.dump(db, dbfile)                      
dbfile.close() 
  