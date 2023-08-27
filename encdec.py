import time



time.sleep(2)
print("""
 _  __   _       ____  _   _  ___  _____ _   _ _____  __
| |/ /  | |     |  _ \| | | |/ _ \| ____| \ | |_ _\ \/ /
| ' /_  | |_____| |_) | |_| | | | |  _| |  \| || | \  / 
| . \ |_| |_____|  __/|  _  | |_| | |___| |\  || | /  \ 
|_|\_\___/      |_|   |_| |_|\___/|_____|_| \_|___/_/\_\
                                                        
""")
print("\n\nENCRYPTION AND DECRYPTION\n                  -by NIX")
print("\n\n1.Encrypt text\n2.Decrypt text")
a = int(input("\nEnter your option 1 or 2 :"))

time.sleep(2)

if a == 1:
    msg = input("Enter your message :")
    al = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+{}|:<>?-=[]\;',./~`"
    key = input("Enter key atleast 10 number:")
    encrypt = ""

    for i in msg:
        position = al.find(i)
        newposition = (position + int(key)) % 93
        encrypt +=al[newposition]
        output = (encrypt)
    print("Encrypted message :",output)


if a == 2:
    msg1 = input("Enter your Decrypted message :")
    al1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+{}|:<>?-=[]\;',./~`"
    key1 = input("Enter your key:")
    decrypt = ""

    for i in msg1:
        position1 = al1.find(i)
        newposition1 = (position1+ -int(key1) )%93
        decrypt +=al1 [newposition1]
        output1 = (decrypt)
    print("decrypted message :",output1)
    









