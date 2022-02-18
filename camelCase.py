#create function for parsing user inptu
def parser(userInput):
    try:
        string_list = userInput.split()#splits string into individual elements in list

        new_list = [] # variable creating empty list used to store elements
        for e in string_list:
            new_list.append((e.title())) #capatalizing first letter of elements in list

        first_word = new_list[0].lower()
        new_list[0] = first_word

        j = "".join(new_list)
        return j
    except:
        print("The input you entered is invalid.")
        return userInput

def banner():
    """ Display program name """
    message = "Awesome camelcase program!!"
    stars = "*" * len(message)
    print(f'\n{stars} \n{message} \n{stars}\n')

def instructions():
    print("Enter a sentance and this program will convert it to camelcase.")

def main():
    banner()
    instructions()
    user_txt = input("Enter the senetence you wish to parse:")
    print(parser(user_txt))
if __name__ == ' __main__':
    main()