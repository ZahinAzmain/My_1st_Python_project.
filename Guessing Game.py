hidden_word= "Zahin Azmain"
guess=""
guess_number_from= 0
total_chances= 3
chances_ended= False

while guess!= hidden_word and not (chances_ended):
    
    if guess_number_from < total_chances:
        guess= input("Guess the majic word: ")
        guess_number_from += 1
        
    else:
        chances_ended = True
        
if chances_ended :
    print("Alas! You lost!!!")
    
else:
    print("Congrates, you won!!!")