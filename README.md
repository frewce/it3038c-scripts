# it3038c-scripts
  
Project 2 

  This code is referenced from the getmyIP.py work we did in class. This has the same functions but has emojis from the emoji module to make it fun, as well as a while loop.
  You start by getting asked if you want to look up a website's IP address.
  
    user_input = (input("Type no to look up a website's IP address. "))
    
  If you want to look up an IP address, you type and say "no" or "No".
  
    while (user_input == "No") or (user_input == "no"):

  It prompts to look up a websites IP address. then it gives the ip with a fun emoji and prompts again.
      print ("Ok, look up another.")
      website = (input("Enter a" + str(bomb) + "website: (Ex: www.google.com)"))
      print(website + ': ' + socket.gethostbyname(website) + computer)
      user_input = (input("Are you done? "))
      
  Type no to keep looking up ip addresses, and when you get tired type anything besides "no" or "No" to leave. 
  Theres a farewell message.
  
    else:
    print("Alright Bye!")
    
  This is how you use my code!
