def diamond_kata(given_letter: str):
    if not given_letter.isalpha():
        return
    
    given_letter = given_letter.upper()
    value_A = ord("A")
    
    value_given_letter = ord(given_letter)
    
    diff = value_given_letter - value_A
    