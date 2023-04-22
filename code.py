from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)                              # 32*8 =  256 bits
buffer_size = 65536                                     # 64kb


#---Encryption---

def ImageEncryption():
    file_to_encrypt = input("Input the file to encrypt : ")
    # open the input and output files in binary format
    inFile = open(file_to_encrypt, 'rb')
    outFile = open('encrypted_' + file_to_encrypt, 'wb')

    # create cipher object and encrypt
    cipher = AES.new(key, AES.MODE_CFB) #auto generates iv

    # write the iv to the output file
    outFile.write(cipher.iv)

    # keep reading the file into the buffer, encrypting then writing to the new file
    buffer = inFile.read(buffer_size)
    while len(buffer) > 0:
        cipher_data = cipher.encrypt(buffer)
        outFile.write(cipher_data)
        buffer = inFile.read(buffer_size)

    # close the files
    inFile.close()
    outFile.close()

#---Decryption---

def ImageDecryption():
    file_to_decrypt = input("Input the file to decrypt : ")
    # open the input and output files in binary format
    inFile = open('encrypted_' + file_to_decrypt, 'rb')
    outFile = open('decrypted_' + file_to_decrypt, 'wb')

    # read in the iv from the input file
    iv = inFile.read(16)

    # create cipher object and decrypt
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

print('\nWelcome to Program illustrating Encryption and Decryption of file\n')
while True:
    print('Choose one of the following:')
    print('1. Encrypt\t2. Decrypt\t3. Exit')
    choice = int(input("Enter the Choice:"))  
    
    if choice == 1:
        ImageEncryption()
    elif choice == 2:
        ImageDecryption()
    elif choice == 3: break
    else:
        print('Invalid choice!')