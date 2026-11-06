import random

numbers = ["1","2","3","4","5","6","7","8","9","0"]
specials = ["!","@","#","$","%","&","*"]
alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
             "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

number = input("Do you want numerical digits in your password (yes/no): ").strip().lower()
special = input("Do you want special character in your password (yes/no): ").strip().lower()
alphabet = input("Do you want alphabets in your password (yes/no): ").strip().lower()

length = int(input("How many digits long do you want this password to be: "))

box = []
guarantee_box = []

if number == "yes":
    box.extend(numbers)
    guarantee_box.append(random.choice(numbers))

if special == "yes":
    box.extend(specials)
    guarantee_box.append(random.choice(specials))

if alphabet == "yes":
    box.extend(alphabets)
    guarantee_box.append(random.choice(alphabets))

if box:
    if length < len(guarantee_box):
        password = "".join(random.choice(box) for i in range(length))
        print(password)

    else:
        normal_gen = length - len(guarantee_box)
        
        password_list = [random.choice(box) for i in range(normal_gen)] + guarantee_box
        
        random.shuffle(password_list)
        password = "".join(password_list)
        print(password)

else:
    print("You must select atleast one character type.")
