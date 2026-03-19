import random 
import string 
string_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_num = '0123456789'
string_special = '!@#$%^&*()'
def userInput():
    length = int(input('Enter length of the password : '))
    use_numbers = input('Do you want to use digits in your password (yes/no) : ').lower()
    use_special_chars = input('Do you want to use special characters in your password (yes/no) : ').lower()
    use_numbers=True if use_numbers=='yes' else False 
    use_special_chars=True if use_special_chars=='yes' else False
    return (length, use_numbers, use_special_chars)
def generate_password(length, use_numbers, use_special_chars):
    password = ''
    for i in range(length-2):
        password += random.choice(string_char)
    if use_numbers:
        password += random.choice(string_num)
    else:
        password += random.choice(string_char)
    if use_special_chars:
        password += random.choice(string_special)
    else:
        password += random.choice(string_char)
    return password
if __name__ == '__main__':
    length, use_numbers, use_special_chars = userInput()
    generated_password = generate_password(length, use_special_chars, use_numbers)
    print("\nGenerated Password:", generated_password)