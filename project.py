from ImageEncryption import ImgEncryption
from ImageDecryption import ImgDecryption

print('\nWelcome to Program illustrating Encryption and Decryption of file\n')
while True:
    print('Choose one of the following:')
    print('1. Encrypt\t2. Decrypt\t3. Exit')
    choice = int(input("Enter the Choice: "))  
    if choice == 1:
        ImgEncryption()
    elif choice == 2:
        ImgDecryption()
    elif choice == 3: break
    else:
        print('Invalid choice!')