print("-------Guessing Game-------")
joy= False
hidden_word="zahin azmain"
guess=""
    

while joy== False:
    print("")
    print("  -----New game-----")
    carry= input("Are you ready?: ")
    if carry.lower()=="no":
        print("OK, happy to be with you. Good bye!!!")
        break
    
    elif carry.lower() != "yes" :
        print("Only Yes or No is valid!")
        
    else:
        print("The real Aura is _____ !")
        print("")
        guess_number_from= 0
        total_chances= 3
        chances_ended= False

        while guess.lower()!= hidden_word and not (chances_ended):
    
            if guess_number_from < 1:
                guess= input("Guess the hidden word: ")
                guess_number_from += 1
                
            elif guess_number_from < total_chances and guess_number_from> 0 :
                guess = input("Incorrect answer. Please try again: ")
                guess_number_from += 1
        
            else:
                chances_ended = True
        
        if chances_ended :
            lose=print("Ah! You lost!!!")
    
        else:
            win=print("Good job, you won!!!")
            joy=True
            
            L2= input("You did it, Let's move forward to level 2: ")
            
            if L2.lower() == "yes":
                print("_________________")
                print("Okey, let's go!!!")
                print("")
                print("-----Level 2-----")
                print("")
                j2 = False
                h2 = "7"
                g2 = ""
                
                while j2 == False:
                    car2 = input("Are you ready?: ")
                    if car2.lower() == "no":
                        print("OK, happy to be with you. Good bye!!!")
                        break
                    
                    elif car2.lower() == "yes":
                        print("A week has ___ days")
                        print("")
                        gnf2 = 0
                        tc2 = 3
                        ce2 = False
                        while g2 != h2 and not ce2:
                            
                            if gnf2 < 1:
                                g2 = input("Enter a number: ")
                                gnf2 += 1
                                
                            elif gnf2 < tc2 and gnf2 > 0:
                                g2 = input("Incorrect answer. Please try again: ")
                                gnf2 += 1
                                
                            else:
                                ce2 = True
                            
                        if ce2 :
                            lost2= print("Ah, you lost!!!")
                            
                        else:
                            win2 = print("Good job. You did it again")
                            j2= True                          
                    else:
                        print("Only Yes or No is valid")
                
            elif L2.lower() == "no":
                print("OK, happy to be with you. Good bye!!!")
            
            else:
                print("Only Yes or No is valid!")
                
