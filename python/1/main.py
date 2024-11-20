# projects from https://thecleverprogrammer.com/2021/01/13/acronyms-using-python/



# ##################################################################################
# 3 Email Slicer


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