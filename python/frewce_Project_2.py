import emoji
import socket

bomb = emoji.emojize(' :bomb:')
thumb = emoji.emojize(' :red_heart:')
computer = emoji.emojize(' :pager:') #if you have an outdated version of pip the computer emoji won't show so I used a pager instead


user_input = (input("Type no to look up a website's IP address. "))

while (user_input == "no") or (user_input == "No"):

    print ("Ok, look up another.")
    website = (input("Enter a" + str(bomb) + "website: (Ex: www.google.com)"))
    print(website + ': ' + socket.gethostbyname(website) + computer)
    user_input = (input("Are you done? "))
else:
    print("Alright Bye!")

