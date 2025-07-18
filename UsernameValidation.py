username = input("Enter username: ")

if username.count(" ") > 0:
    print("Username cannot contain empty spaces")
if not username.isalpha():
    print("Username must not contain digits")
if len(username) > 12:
    print("Username should be no longer than 12 chars")
