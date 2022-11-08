from cryptography.fernet import Fernet


def write_key():
    '''
    -> Creates the cryptographic key (key.key file) the first time the program is run.
    Use only the first time you run the program, if the key is changed, 
    it will not be possible to decrypt the passwords.
    For security, after creating the key, comment/disable this function.
    '''
    key = Fernet.generate_key()
    with open('Password_Manager\key.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    '''
    -> Load and return the cryptographic key.
    '''
    file = open('Password_Manager\key.key', 'rb')
    key = file.read()
    file.close()
    return key


def view():
    '''
    -> Decrypt the files and format the output display.
    '''
    print('=' * 50)
    with open('Password_Manager\passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())
    print('=' * 50)


def add():
    '''
    -> Adds new passwords to the 'passowords.txt' file by encrypting the passwords.
    '''
    print('=' * 50)
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('Password_Manager\passwords.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')
    print('=' * 50)


key = load_key()
fer = Fernet(key)

print('=' * 40)
print(f'{"PASSWORD MANAGER":^40}')
print('=' * 40)

while True:
    mode = int(input(
    '''Options:

1 - Add new password
2 - View saved passwords
3 - Quit

Select the option: '''))
    if mode == 3:
        break
    elif mode == 2:
        view()
    elif mode == 1:
        add()
    else:
        print('Invalid Mode')
        continue
