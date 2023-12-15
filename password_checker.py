"""
INST326 Final Project: Password Strength Checker
Members: Stephen V. Thang, Bryan Wright

The module contains functions to check and rank password strength based on a given criteria: specified length, complexity, and characteristics such as uppercase, lowercase, special character, and a number. 
---------------------------------------------------------
"""

# A constant
MAX_COMPLEXITY = 4 # Maxium complexity level for a password


"""
Is password long enough function that check if password meets the length requirements (8 characters)

Parameters(str): password

Return: (Bool) True is password meets requirement, False otherwise
"""

def is_password_long_enough(password):
    
    min_length = 8 

    return len(password) >= min_length
        

"""
Password complexity verification: checks for necessary characteristics such as uppercase, lowercase, numbers, and special characters.

return: message that indicates which characteristics the password contains. Count. 

"""

# Critera of complexity level
def password_complexity_level(password): 
    upper_case = False
    lower_case = False
    number = False
    special = False
    # Rank by levels, based on how many of the criteria it has met. 

    for char in password:
        if char.isupper():
            upper_case = True
        elif char.islower():
            lower_case = True
        elif char.isdigit():
            number = True
        elif char in "!@#$%^&*()_+}{[]|\:;<>.?/":
            special = True 

    # Count how many trues in the values
    num_trues = 0

    for value in locals().values():
        if value:
            num_trues += 1
    return num_trues

def is_password_complex(password):
    return password_complexity_level(password) == MAX_COMPLEXITY 
         

"""
Generates suggestions for stronger passwords based on the input password

returns: a list of suggestions for password improvement.
"""

def password_suggestion_generator(password):
    suggestions = []

    if not is_password_long_enough(password):
        suggestions.append("Try a longer password")

    has_number = False
    has_lowercase = False
    has_uppercase = False
    has_specialchar = False

    for p in password:
        if p.isdigit():
            has_number = True
        elif p.islower():
            has_lowercase = True
        elif p.isupper():
            has_uppercase = True
        elif p in "!@#$%^&*()_+}{[]|\:;<>.?/":
            has_specialchar = True 
            
    template = "Try adding {} to increase complexity of password"

    if not has_number:
        suggestions.append(template.format('numbers'))
    if not has_lowercase:
        suggestions.append(template.format('lower case letters'))
    if not has_uppercase:
        suggestions.append(template.format('upper case letters')) 
    if not has_specialchar:
        suggestions.append(template.format('special characters'))   

    return suggestions    

"""
Parse text files to check if they meet the criteria

Parameters: filename

Returns: two lists indicating strong and weak passwords. 
"""

def text_file_analyzer(filename):
    strong_passwords = []
    weak_passwords = []

    with open(filename, 'r') as file:
        for line in file:
            password = line.strip()
            if is_password_long_enough(password) and is_password_complex(password):
                strong_passwords.append(password)
            else:
                weak_passwords.append(password)
    return strong_passwords, weak_passwords

"""
Ranks lists of passwords based on their length and complexity

Parameters: passwords

Returns: list of passwords from strongest to least strong. 
"""

def password_ranker(passwords):
    def password_ranker_key(password):

        return password_complexity_level(password), len(password)

    # reverse the sorting: most complex to least

    ranked_pass = sorted(passwords, key=password_ranker_key, reverse=True)

    return ranked_pass

"""
User inputs password and evaluates the strength then provides the necessary suggestions if needed
"""

def input_password_checker():
    password = input("Enter Password: ")
    
    suggestions = password_suggestion_generator(password)

    if suggestions:
        print("Here are some suggestions for improving your password: ")

        for suggestion in suggestions:
            print(" -", suggestion)
    else:
        print("No suggestions nessesary. Your password meets requirements.")

"""
Checks strength of the password provided by the user by their complexity
"""

def input_password_ranker():
    list_passwords = input("Enter list of passwords seperated by commas and spaces: ").replace(",", "").split()
    print("The passwords ranked by complexity are: ", end="") 
    print( *password_ranker(list_passwords), sep=", ")

"""
Provides the option of interacting with the user to select between checking the complexity of a single password (1) or ranking a list of passwords (2)
"""

def input_selector():
    selection = input("Enter 1 to check complexity of a password, Enter 2 to rank list of passwords by complexity: ")
    
    if selection == "1":
        input_password_checker()
    elif selection == "2":
        input_password_ranker()
    else:
        print("Invalid selection. ")



if __name__ == "__main__":
    input_selector()
