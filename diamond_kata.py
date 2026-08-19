def diamond_kata(given_letter: str):
    if not given_letter.isalpha():
        return
    
    given_letter = given_letter.upper()
    value_A = ord("A")
    letter = chr(value_A)

    value_given_letter = ord(given_letter)
    diff = value_given_letter - value_A
    
    inner_space = 0
    leading_space = diff

    
    for i in range(diff):
        if letter == "A":
            print((" " * leading_space )+ letter + (" " * leading_space))
        
        # print("we are here with ", letter)
        else:
            print((" " * leading_space )+ letter + (" " * inner_space) + letter + (" " * leading_space))
        
        value_of_letter = ord(letter)
        # print("value_of_letter", value_of_letter)
        # print("value_given_letter", value_given_letter)
        
        if value_of_letter < value_given_letter:
            value_of_next_letter = value_of_letter + 1
            letter = chr(value_of_next_letter)
            inner_space += 2
            leading_space -=1
            
            # print("next letter, inner, leading=", letter, inner_space, leading_space)
    
    for i in range(diff + 1):
        if letter == "A":
            # print("letter A")
            print((" " * leading_space )+ letter + (" " * leading_space))
            return
        
        
        print((" " * leading_space )+ letter + (" " * inner_space) + letter + (" " * leading_space))
        
        value_of_letter = ord(letter)
        value_of_next_letter = value_of_letter - 1
        letter = chr(value_of_next_letter)
        inner_space -= 2
        leading_space +=1
        # print("next letter else =", letter)
        
        
        



print(diamond_kata("D"))
    