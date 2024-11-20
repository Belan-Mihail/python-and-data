import string


def text_analyse(filename):
    """
    this function analyse text file
    """

    # open text file
    with open(filename, "r", encoding='utf-8') as file:
        text = file.read()
        

    # remove punctuation marks and convert to lowercase
    words = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
    
    # words count
    words_count = len(words)
    print(words_count)

    sentences_count = text.count(".") + text.count("!") + text.count("?")
    print(sentences_count)

    
    

filename = "d.txt"
text_analyse(filename)