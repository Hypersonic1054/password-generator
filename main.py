import random as rd
import os

def get_character_sets():   # gets all the characters the password needs
    char_sets = {
        "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "lowercase": "abcdefghijklmnopqrstuvwxyz",
        "numbers": "0123456789",
        "symbols": "!@#$%^&*()_+"
    }
    return char_sets

def get_password_length(): # makes the passwrod 9-14 characters long  
    return rd.randint(9, 14)

def generate_password(): #creates the password
    char_sets = get_character_sets()
    total_length = get_password_length()
    
    password_chars = [
        rd.choice(char_sets["uppercase"]),
        rd.choice(char_sets["lowercase"]),
        rd.choice(char_sets["numbers"]),
        rd.choice(char_sets["symbols"])
    ]# randomly choses the char_sets and it will always have atleast an uppercase letter, lowercase letter, numbers, and symbols
    
    remaining_length = total_length - 4 #the -4 is because the password will always start with the password_chars
    while remaining_length > 0:
        password_chars.append(
            rd.choice(
                char_sets["uppercase"] + char_sets["lowercase"] + char_sets["numbers"] + char_sets["symbols"]
            )
        )
        remaining_length -= 1
    
    rd.shuffle(password_chars) #shuffles the characters so it can be different
    
    final_password = ""
    for char in password_chars:
        final_password += char

    return final_password

if __name__ == "__main__":  #the main function which creates the passwords
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        password = generate_password()
        print("Your password is:", password)
        
        again = input("Do you want another password? (y/n): ").lower()
        if again != 'y':
            break
