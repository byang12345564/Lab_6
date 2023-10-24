#this is the code of Billy Yang
def encode(password):
    encoded = ''
    for i in range(len(password)):
        encoded += str((int(password[i]) + 3) % 10)
    return encoded

if __name__ == '__main__':
    password_original = None
    password_encoded = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option: "))

        if option == 1:
            password_original = input("Please enter your password to encode:")
            password_encoded = encode(password_original)
            print("Your password has been encoded and stored!")
            continue

        if option == 2:
            print(f"The encoded password is {password_encoded}, and the original password is {password_original}.")
            continue

        if option == 3:
            break