
print("..............matching password and user for login............")

correct_user = "priyanshi"
correct_password = "8967pri"

login_success = False

for i in range(1, 4):
    try_user = input("Enter user: ")
    try_password = input("Enter password: ")

    if try_user == correct_user and try_password == correct_password:
        print("Congrats! Login successful.")
        login_success = True
        break
    else:
        remaining = 3 - i
        if remaining > 0:
            print(f"Wrong username or password. You have {remaining} attempt(s) left.")

if not login_success:
    print("Access denied. All login attempts used.")
