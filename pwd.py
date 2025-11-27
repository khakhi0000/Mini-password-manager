passwords = []

while True:
    print("1:Add password ")
    print("2:Remove password ")
    print("3:Update password ")
    print("4:View all password ")
    print("5:Exit ")

    choice = input("Enter your choice(1-4): ")
    if choice == "1":
        pwd = input("Enter your password: ")
        passwords.append(pwd)
        print("Password added successfully! ")
    elif choice == "2":
        pwd = input("Enter your password: ")
        if pwd in passwords:
            passwords.remove(pwd)
            print("Password removed successfully! ")
        else:
            print("Password not found! ")
    elif choice == "3":
        old = input("Enter current password: ")
        if old in passwords:
            new = input("Enter new password: ")
            index = passwords.index(old)
            passwords[index] = new
            print("Password updated successfully! ")
    elif choice == "4":
        print(" Your passwords are Shown below!\n")
        for p in passwords:
            print(p)
    elif choice == "5":
        print("Exiting....")
        break
    else:
        print("Invalid choice! ")

