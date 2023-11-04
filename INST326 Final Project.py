"""
INST326 Final Project: Password Strength Checker
Members: Stephen V. Thang, Bryan Wright, Ikenna Ashiogwu
---------------------------------------------------------
"""

"""
Password checker function that check if password meets the length requirements (8 characters)

return: length of password typed or an error message
"""
def password_length_checker(password):
    min_length = 8 
    if password >= min_length:
        return len(password)
    else: 
        return "Password does not meet length criteria (8 characters)"

"""
Password complexity verification: checks for necessary characteristics such as uppercase, lowercase, numbers, and special characters.

return: message that indicates which characteristics the password contains. 

"""
def password_complexity_checker(password): 
    upperCase = False
    lowerCase = False
    number = False
    special = False

    for char in password:
        if char.isupper():
            upperCase = True
        elif char.islower():
            lowerCase = True
        elif char.isdigit():
            number = True
        elif char in "!@#$%^&*()_+{}[]|\:;<>,.?/":
            special = True 
    return f"Has uppercase {upperCase}, has lowercase {lowerCase}, has number {number},  has special character {special}"
         

"""
Generates suggestions for stronger passwords based on the input password

returns: a list of suggestions for password improvement.
"""
def password_suggestion_generator(password):
    suggestions = []

    if len(password) <= 8:
        suggestions.append("Try a longer password")
    has_number = False
    has_lowercase = False
    has_uppercase = False

    if p in password:
        if p.isdigit():
            has_number = True
        elif p.islower():
            has_lowercase = True
        elif p.isupper():
            has_uppercase = True

    if not has_number:
        suggestions.append("Try adding numbers to increase complexity of password")
    if not has_lowercase:
        suggestions.append("Try adding lowercase to increase complexity of password")
    if not has_uppercase:
        suggestions.append("Try adding uppercase to increase complexity of password")    
    return suggestions    

"""
Parse text files to check if they meet the criteria

Returns: a message indicating strong and weak passwords. 
"""
def text_file_analyzer(filename):
    file = open(filename, 'r') 
    strong_passwords = []
    weak_passwords = []

    for line in file:
        password = line.strip()
        if password_length_checker(password) and password_complexity_checker(password):
            strong_passwords.append(password)
        else:
            weak_passwords.append(password)
    file.close()
    return f"Your strong password: {strong_passwords}, your weak password: {weak_passwords}"

"""
Ranks lists of passwords based on their length and complexity

Returns: list of passwords from strongest to least strong. 
"""
def password_ranker(passwords):
    def password_ranker_key(password):
        return (len(password), password_complexity_checker(password))
    ranked_pass = sorted(passwords, key=password_ranker_key )
    return ranked_pass
