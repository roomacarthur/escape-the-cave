# def two_choice_option(prompt,opt1,opt2,path1,path2):
#     """
#     Allows for the input(prompt) of an option(opt1/op2) with two outcomes(path1,path2).
#     When user enters a correct option the loops is passed and the given path is executed.
    
#     """
#     while True:
#         try:
#             choice = input(prompt)
#             if choice == opt1:
#                 path1()
#                 break
#             elif choice == opt2:
#                 path2()
#                 break
#             elif choice == "" and choice != (opt1) or (opt2):
#                 print(f"please enter a valid option! ({opt1} or {opt2})\n")
#                 continue
#             else:
#                 break
#         except ValueError:
#             print(f"please enter a valid option! ({opt1} or {opt2})\n")


# def option_four():
#     print("option four :D")

# def option_five():
#     print("option five :D")

# two_choice_option("Do you keep the axe? (yes/no): ","yes","no",option_four,option_five)

#================ TEST ================
def two_choice_option(prompt,opt1,opt2,path1,path2):
    """
    Allows for the input(prompt) of an option(opt1/op2) with two outcomes(path1,path2).
    When user enters a correct option the loops is passed and the given path is executed.
    
    """

    # Consider if the try/except is even needed here as the else statement works fine. 
    while True:
        try:
            choice = input(prompt)
            if choice == opt1:
                path1()
                break
            elif choice == opt2:
                path2()
                break
            else:
                print(f"Please enter a valid option! ({opt1} or {opt2})\n")
                continue
            
        except ValueError:
            print(f"ERROR: please enter a valid option! ({opt1} or {opt2})\n")


def option_four():
    print("option four :D")

def option_five():
    print("option five :D")


two_choice_option("Do you keep the axe? (yes/no): ","yes","no",option_four,option_five)
