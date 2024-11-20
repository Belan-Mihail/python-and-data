import string


def text_analyse(filename):
    """
    this function analyse text file
    """

    # open text file
    with open(filename, "r", encoding='utf-8') as file:
        text = file.read()
        

    # remove punctuation marks and convert to lowercase
    words = text.translate(str.maketrans('', '', string.punctuation)).lower().split
    

filename = "d.txt"
text_analyse(filename)