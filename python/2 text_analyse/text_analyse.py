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

     # sentences count
    sentences_count = text.count(".") + text.count("!") + text.count("?")
    print(sentences_count)

    # paragraph count
    paragraph_count = text.count('\n\n') + 1
    print(paragraph_count)

    # words count
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # sort words
    most_common_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]


    print("10 most common words:")
    for word, freq in most_common_words:
        print(f"{word}: {freq}")


    

filename = "d.txt"
text_analyse(filename)