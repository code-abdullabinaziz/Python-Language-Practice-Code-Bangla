text = "Dhaka-Chittagong-Sylhet-Khulna"

result = text.split("-", maxsplit=2)

print(result)



numbers = [10, 20, 30, 40, 50]


user_number = int(input("Enter a number to check if it is in the list: "))


if user_number in numbers:
    print(f"{user_number} is in the list.")
else:
    print(f"{user_number} is not in the list.")


