from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

print()
buffer_size = 65536                                     # 64kb

def GetKey():
    file_in = open("key_location.txt", 'rb') # Read bytes
    key_from_file = file_in.read() # This key should be the same
    file_in.close()
    return key_from_file

#---Decryption---

def ImgDecryption():
    file_to_decrypt = input("Input the file to decrypt : ")
    # open the input and output files in binary format
    inFile = open('encrypted_' + file_to_decrypt, 'rb')
    outFile = open('decrypted_' + file_to_decrypt, 'wb')

    # read in the iv from the input file
    iv = inFile.read(16)

    # create cipher object and decrypt
    key = GetKey()
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)

    # keep reading the file into the buffer, decrypting then writing to the new file
    buffer = inFile.read(buffer_size)
    while len(buffer) > 0:
        original_data = cipher.decrypt(buffer)
        outFile.write(original_data)
        buffer = inFile.read(buffer_size)

    # close the files
    inFile.close()
    outFile.close()