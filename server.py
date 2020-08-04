import pickle5 as pickle
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
dbfile = open('project_2', 'rb')      
db = pickle.load(dbfile) 
key_decrypt = db['key']
cipher_text = db['ciphertext']
BLOCK_SIZE = db['blocksize']

decipher = AES.new(key_decrypt, AES.MODE_ECB)
msg_dec = decipher.decrypt(cipher_text)
msg_dec = unpad(msg_dec, BLOCK_SIZE)
msg_dec = msg_dec.decode("utf-8")
print(msg_dec)



dbfile.close() 