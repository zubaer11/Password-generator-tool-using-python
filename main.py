import string
import random
from datetime import datetime
import time
import os.path

# in order to save the passsword as a file.txt
def log_file(password):
    user_save_path = input("Do you want to specify your own file path and name(yes/no): ").lower()
    if user_save_path == "yes":
        save_path = input("Enter your path name: ")
        file_name = input("Enter the name of the file: ")
        name_and_save = os.path.join(save_path, file_name+'.txt')
        with open(name_and_save, "a") as f:
            f.write(f"{password}\n Do not share this with anyone\n Save date: {datetime.now()}")
            f.close()
            #print(f"Your nfile path {os.path.abspath('Password')}")
    else:
        with open("Password", "a") as f:
            f.write(f"{password}\n Do not share this with anyone\n Save date: {datetime.now()}")
            f.close()
            print(f"Your nfile path {os.path.abspath('Password')}")



if __name__ == '__main__':
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    password_len = int(input("Enter the password length: ")) # the size of password
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    password = ("".join(s[0:password_len]))
    x = f'Your password is: {password}'
    print(x)

user_input = input("Do you want to save this password?(yes/no) > ").lower()

if user_input == 'yes':
    log_file(x)
    time.sleep(3)
    print("Your file file is successfully saved")

else:
    print("Thank you")
