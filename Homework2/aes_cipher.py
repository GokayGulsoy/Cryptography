"""""
ENCRYPTION WITH AES 
Student no: 270201072
"""""
import sys
import json

from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES

def encrypt(argv):
    # generating key from random salt
    salt = get_random_bytes(16)      
    print(type(salt))
    key = scrypt(argv[5],salt,argv[7],2**14,16,1) 
    # padding message to length with PKCS7 algorithm
    padded_message = pad(argv[3],16)
    # randomly generating 128-bit initialization vector
    iv = get_random_bytes(16)
    # encrypting the padded message
    aes_cipher = AES.new(argv[7],AES.MODE_CBC,iv)
    ciphertext =  aes_cipher.encrypt(padded_message)
    print("Encryption result: ")
    print("{'salt':",salt,"iv:",iv,"ciphertext:",ciphertext,"}")
    
    # writing salt,iv, and ciphertext to JSON file
    json_dict = {"salt":salt,"iv":iv,"ciphertext:":ciphertext}
    json_format = json.dumps(json_dict)         
    json_file = open(argv[9],"w")
    json_file.write(json_format)
    json_file.close()
           

def decrypt(argv):
    # reading the JSON file
    json_file = open(argv[5],"r")
    json_file_content = json_file.read()
    json_dict =  json.loads(json_file_content) 
    
    # reading salt 
    salt = json_dict["salt"]
    # reading initialization vector
    iv = json_dict["iv"]
    # reading ciphertext
    ciphertext = json_dict["ciphertext"]
    key = scrypt(argv[3],salt,argv[7],2**14,16,1) 
    cipher  =  AES.new(key,AES.MODE_CBC,iv)
    plaintext =  cipher.decrypt(ciphertext)
    print("Plaintext")
    print(plaintext)
    
 
if (sys.argv[1] == "enc"):  
   if (sys.argv[2] != "-m" or sys.argv[4] != "-p" or sys.argv[6] != "-k" or sys.argv[8] != "-f"):
        print("Positional arguments are not given in correct order") 
    
   encrypt(sys.argv)
 
elif (sys.argv[1] == "dec"):
     
     if (sys.argv[2] != "-m" or sys.argv[4] != "-p" or sys.argv[6] != "-k" or sys.argv[8] != "-f"):
         print("Positional arguments are not given in correct order") 
            
     decrypt(sys.argv)  

else:
    print("Invalid type of operation!!!")