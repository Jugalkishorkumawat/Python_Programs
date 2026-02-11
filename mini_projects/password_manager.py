from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
write_key()
'''

def load_key():
    return open("key.key", "rb").read()      



key = load_key() 
fer = Fernet(key)
   
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Account: ", user, " | Password: ", 
                  fer.decrypt(passw.encode()))

def add():
    name = input("Account Name: ")
    password = input("Password: ")
    
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode()+ "\n") 
    print("Password added successfully!")


while True:
    mode= input("Would you like to add a new password or view existing passwords or q for Quit? (add/view/q) ")
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
