def print_upper_words(string_list):
    """This function prints out each word on a list of words in uppercase letters.
    Example: 
        print_upper_words(['hello', 'bye', 'hi']) 

    This should print:
        HELLO
        BYE
        HI
    """
    for string in string_list:
        print(string.upper())


def print_upper_words_2(string_list):
    """This function prints out each word that starts with an uppercase "E" or lowercase "e" on a list of words in uppercase letters.
    Example: 
      print_upper_words_2(['hello', 'bye', 'hi', 'eye', 'Elephant']) 

    This should print:
       EYE
       ELEPHANT
     """
    for string in string_list:
        if string.startswith("e") or string.startswith("E"):
            print(string.upper())


def print_upper_words_3(string_list, must_start_with):
    """This function prints out each word whose first letter matches with the letters provided in the set: must_start_with and change the word to be uppercased.
    Example:  
      print_upper_words_3(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})

    This should print:
       HELLO
       HEY
       YO
       YES
     """
    for string in string_list:
        # Convert the first letter of the word to lowercase and check if it's in the must_start_with set.
        if string[0].lower() in must_start_with:
            print(string.upper())
