# projects from https://thecleverprogrammer.com/2021/01/13/acronyms-using-python/



# ##################################################################################
# 7 Python Program to Convert Roman Numbers to Decimals

# taillies = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000
# }

# def RomanNumeraltoDecimal(romanNumeral):
#     sum = 0
#     for i in range(len(romanNumeral) - 1):
#         left = romanNumeral[i]
#         print(f"left {left}")
#         right = romanNumeral[i+1]
#         print(f"right {right}")
#         if taillies[left] < taillies[right]:
#             print(f"line 25. sum {sum} - tailes-left {taillies[left]}")
#             sum -= taillies[left]
#         else:
#             print(f"line 28. sum {sum} + tailes-left {taillies[left]}")
#             sum += taillies[left]
#     print(f"line 30. sum {sum} + tailes-left {taillies[romanNumeral[-1]]} ")
#     sum += taillies[romanNumeral[-1]]
#     return sum

# a = RomanNumeraltoDecimal("XVIII")
# print(a)


# ##################################################################################
# 6 Colored Terminal Text
# import colorama

# from colorama import Fore, Back, Style
# colorama.init(autoreset=True)

# print(Fore.BLUE+Back.YELLOW+"Hi My name is Mykhailo Bilan "+ Fore.YELLOW+ Back.BLUE+"I am a programmer")
# print(Back.CYAN+"Hi My name is Mykhailo Bilan")
# print(Fore.RED+ "Hi My name is Mykhailo Bilan")


# ##################################################################################
# 5 QR Code Generator

# import pyqrcode
# from pyqrcode import QRCode 

# # Url
# url = "https://github.com/Belan-Mihail"

# # QR Code qenerate
# qr = pyqrcode.create(url)

# qr.svg("mygithub", scale=8)


# ##################################################################################
# 4 Generate Password

# import random
# passlen = int(input("Enter password lenght: "))

# possible symbols for password
# s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# password generate
# password = "".join(random.sample(s, passlen))

# print(password)

# ##################################################################################
# 3 Email Slicer

# email = input("Enter your email: ").strip()
# username = email[:email.index("@")]
# domainname = email[email.index("@") + 1:]
# format = (f"Your name is {username}. Your domain is {domainname}")
# print(format)

# ##################################################################################
# 2 Alarm Clock

# from datetime import datetime

# alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")

# alarm_hour = alarm_time[0:2]

# alarm_minute=alarm_time[3:5]

# alarm_second=alarm_time[6:8]


# while True:

#     now = datetime.now()
    
#     current_hour = now.strftime('%I')
    
#     current_minute = now.strftime('%M')
    
#     current_second = now.strftime('%S')
    
#     if(alarm_hour == current_hour):
#         if(alarm_minute == current_minute):
#             if (alarm_second == current_second):
#                 print('Wake up')
#                 break


# ##################################################################################
#  1 Create Acronyms using Python

# user_input = str(input("Enter you Phrase: "))

# text = user_input.split()

# a = ""

# for i in text:
#     a = a + str(i[0]).upper()

# print(a)