def rot13(message):
    rot13_1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    rot13_2 = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
    encoding_message = []

    for char in message:
        if char in rot13_1:
            encoding_message.append(rot13_2[rot13_1.index(char)])
            
        elif char in rot13_2:           
            encoding_message.append(rot13_1[rot13_2.index(char)])
            
        elif char.isupper() == True:
            char = char.lower()
            if char in rot13_1:
                encoding_message.append(rot13_2[rot13_1.index(char)].upper())

            elif char in rot13_2:                             
                encoding_message.append(rot13_1[rot13_2.index(char)].upper())
        
        else:
            encoding_message.append(char)
            
    return ''.join(encoding_message)
