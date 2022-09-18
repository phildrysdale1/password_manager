from cryptography.fernet import Fernet

# set encryption key
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''
# load encryption key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

## Need to read up on Fernet on how to fully impliment this master password section - currently is not relevant.
master_pwd = input ("What is the master password? ")

# set variables
key = load_key() + master_pwd.encode()
fer = Fernet(key)

# function for managing viewing passwords
def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            data = (line.rstrip())
            user, passw = data.split ("|")
            print('User: ', user, " | Password: ", fer.decrypt(passw.encode()).decode())

# function for managing adding passwords
def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as file:
        file.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')

# loop for managing app
while True:
    mode = input("Would you like to add a new password or view existing ones? (view/add) ")
    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid selection.")
        continue