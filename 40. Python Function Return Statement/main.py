def greet_user(user_name, greeting="Hello"):
    return f"{greeting}, {user_name}!"


user_name = input("Enter your user_name: ")
print(greet_user(user_name))
