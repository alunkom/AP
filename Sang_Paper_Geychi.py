# OUTPUT LIKE THIS :

"""
 _____________ 
   Geek_tory!               # Sang
      \                     # Paper
       \   ,__,             # Geychi
        \  (oo)____         # End
           (__)    )\   
              ||--|| *      [ Mahdi Ojaghloo | alunkom.mahdi@gmail.com ]
                            [ Alunkom | https://github.com/alunkom/]


          ______________________________
Ex :

Enter a choice :  s
                                User | Coputer  Winner is Computer :)
          ______________________________


Enter a choice :
""""
#---------------------------------------------------------------------------------------------------------------------------------------------------


#                                                               < THE CODE >


#---------------------------------------------------------------------------------------------------------------------------------------------------


# Import choice from random library

from random import choice 

#--------------------------------------------------------

# Start Section :)

def print_cow():
    print("\n")
    print(" _____________ ")
    print(" \033[07m  Geek_tory! \033[27m              # \033[07mS\033[1;mang")
    print("      \                     # \033[07mP\033[1;maper")
    print("       \   \033[1;31m,__,\033[1;m             # \033[07mG\033[1;meychi")
    print(
        "        \  \033[1;31m(\033[1;moo\033[1;31m)____\033[1;m         # \033[07mE\033[1;mnd"
    )
    print("           \033[1;31m(__)    )\ \033[1;m  ")
    print(
        "           \033[1;31m   ||--|| \033[1;m\033[05m*\033[25m\033[1;m      [ Mahdi Ojaghloo | alunkom.mahdi@gmail.com ]"
    )
    print(28 * " " + "[ Alunkom | https://github.com/alunkom/]\r\n\n")
    print(' '*10+"___"*10)
    print("Ex :\n\nEnter a choice :  s\n\t\t\t\tUser | Coputer\tWinner is Computer :)")
    print(' '*10+"___"*10)
    

print_cow()

#---------------------------------------------------------------------------------------------------------------------------------------------------

possible_actions = ["sang" , "paper" , "geychi"]

while True:
    
    computer_action = choice(possible_actions)
    user_action = input("\n\n\033[1;mEnter a choice :  ").lower()
    # Help user to input just one letter
    
    if user_action == 's':
        user_action = 'sang'
    elif user_action == 'p':
        user_action = 'paper'
    elif user_action == 'g':
            user_action = 'geychi'

    #-------------------------------
    
    # Determine winner
    
    if user_action == computer_action :
        user_action = user_action[0].upper()
        print("\t\t\t\t\033[1;30m%s%s | %s%s\t\033[1;30mBoth player select."%(user_action[0].upper(),computer_action[1:],computer_action[0].upper(),computer_action[1:]))
    else :
        
        if user_action == "sang" and computer_action == 'paper': 
            print("\t\t\t\t\033[1;31mSang | Paper \t\033[1;31mWinner is Computer :)")
        elif user_action == 'sang' and computer_action == 'geychi':
            print("\t\t\t\t\033[1;34mSang | Geychi\t\033[1;34mHooooooora Barandeh shodi ;)")
        
        elif user_action == 'paper' and computer_action == 'sang' :
            print("\t\t\t\t\033[1;34mPaper | Sang \t\033[1;34mHooooooora Barandeh shodi ;)")
        elif user_action == 'paper' and computer_action == "geychi":
            print('\t\t\t\t\033[1;31mPaper | Geychi\t\033[1;31mWinner is Computer :)')
        
        elif user_action == 'geychi' and computer_action =='sang':
            print('\t\t\t\t\033[1;31Geychi | Sang \t\033[1;31mWinner is Computer :)')
        elif user_action == 'geychi' and computer_action =='paper':
            print("\t\t\t\t\033[1;34Geychi | Paper\t\033[1;34mHooooooora Barandeh shodi ;)")            
    
    #-----------------------------------
    
    # END
        elif user_action == 'end' or 'e':
            break 
#---------------------------------------------------------------------------------------------------------------------------------------------------        
"""
                                                                             ____________
                                                                            < Geek_TORY! >
                                                                             ------------
                                                                                   \    ____
                                                                                    \  /    \
                                                                                      | ^__^ |
                                                                                      | (oo) |______
                                                                                      | (__) |      )\/\
                                                                                       \____/|----w |
                                                                                            ||     ||

                                                                                                                    """
