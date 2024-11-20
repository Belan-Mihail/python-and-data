# projects from https://thecleverprogrammer.com/2021/01/13/acronyms-using-python/







#  1 Create Acronyms using Python

user_input = str(input("Enter you Phrase: "))

text = user_input.split()

a = ""

for i in text:
    a = a + str(i[0]).upper()

print(a)