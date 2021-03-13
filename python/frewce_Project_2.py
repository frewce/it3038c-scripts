import emoji
import socket

bomb = emoji.emojize(' :bomb:')
thumb = emoji.emojize(' :red_heart:')
computer = emoji.emojize(' :pager:') #if you have an outdated version of pip computer won't show so I used a pager instead


user_input = (input("Are you done? "))

while (user_input == "no") or (user_input == "No"):

    print ("ok, look up another.")
    website = (input("Enter a" + str(bomb) + "website: (Ex: www.google.com)"))
    print(website + ': ' + socket.gethostbyname(website) + computer)
    user_input = (input("Are you done? "))
else:
    print("Alright Bye!")

