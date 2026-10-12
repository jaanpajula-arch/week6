#logging form with three attempts only

password = "python123"
logged_in = False
attempts = 0


while logged_in == False and attempts < 3:
    user_input = input("Enter the password: ")
    attempts = attempts + 1

    if user_input == password: 
        print("Login successful.")
        logged_in = True
    else:
        print("Login failed. Try again.")

if logged_in == False:
    print("Too many failed attempts. Access denied.")