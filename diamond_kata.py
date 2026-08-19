def _build_row(letter, leading_space, inner_space):
    if letter == "A":
        return " " * leading_space + letter
    return " " * leading_space + letter + " " * inner_space + letter   

def diamond_kata(given_letter: str):
    if not given_letter.isalpha():
        return
    
    given_letter = given_letter.upper()
    value_A = ord("A")
    letter = chr(value_A)

    value_given_letter = ord(given_letter)
    diff = value_given_letter - value_A
    
    inner_space = -1
    leading_space = diff

    
    for i in range(diff):
        print(_build_row(letter, leading_space, inner_space))
        
        value_of_letter = ord(letter)
        
        if value_of_letter < value_given_letter:
            value_of_next_letter = value_of_letter + 1
            letter = chr(value_of_next_letter)
            inner_space += 2
            leading_space -=1
    
    for i in range(diff + 1):
        print(_build_row(letter, leading_space, inner_space))
        
        value_of_letter = ord(letter)
        value_of_next_letter = value_of_letter - 1
        letter = chr(value_of_next_letter)
        inner_space -= 2
        leading_space +=1
        

        
        


diamond_kata("D")

diamond_kata("C")
    