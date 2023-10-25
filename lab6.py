#this is the code of Billy Yang
def encode(password):
    encoded = ''
    for i in range(len(password)):
        encoded += str((int(password[i]) + 3) % 10)
    return encoded


def decode(code):
    decoded_password = ""  # creates empty string to hold decoded password
    for i in code:  # iterates through code
        decoded_digit = (int(i) - 3) % 10  # subtracts 3 from each digit
        decoded_password += str(decoded_digit)  # adds decoded digit to string
    return decoded_password  # returns decoded password


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
            password_decoded = decode(password_encoded)
            print(f"The encoded password is {password_encoded}, and the original password is {password_decoded}.")
            continue

        if option == 3:
            break
