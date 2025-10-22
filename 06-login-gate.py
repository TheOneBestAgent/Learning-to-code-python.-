username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username == "admin" and password == "1234":
    print("Access Granted")
elif username == "guest":
    print("Welcome Guest")
else: 
    print("Access Denied")
