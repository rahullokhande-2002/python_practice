password=input('enter the password')

if len(password)<=10:
    if password[0].upper():
        if password[-3:].isdigit():
            print('correct')
        else:
            print('your last 3 digits must be digit')
    else:
        print('your last 1st character uppercase')  
else:
    print('incorrect passwords')                    