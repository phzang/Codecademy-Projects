"""    xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je
tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!

This message has an offset of 10. Can you decode it?"""

alphabet = "abcdefghijklmnopqrstuvwxyz"

def decode_message(message):
    decoded_message = []
    for l in message:
        i = alphabet.find(l)        
        #position of the decoded message
        location = i + 10
       
        #if the letter is a space, then just add it to the message
        if (l == ' ' or l == '?' or l == '.' or l == '!'):
            decoded_message.append(l)            
        #26 letters in the alphabet, but index starts at 0
        elif ((location / 25 < 1) and (location / 25 >= 0)):
            try:                
                decoded_message.append(alphabet[location])
            except IndexError:
                print("Oops, something happened")
            
        else:
            #new location if it's towards the end of the alphabet
            location = location - 26
            try:
                decoded_message.append(alphabet[location])
            except IndexError:
                print("oops, something ELSE happened")

            
    return ''.join(decoded_message)
            
#print(decode_message("xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"))
            
"""Great job! Now send Vishal back a message using the same offset.
Your message can be anything you want! Remember, coding happens in opposite
direction of decoding."""

def code_message(message):
    coded_message = []
    for l in message:
        i = alphabet.find(l)
        #position of the coded message
        location = i - 10
        #print(l, location)
       
        #if the letter is a space, then just add it to the message
        if (l == ' ' or l == '?' or l == '.' or l == '!'):
            #print("if {} {}".format(location,l))
            coded_message.append(l)            
        #26 letters in the alphabet, but index starts at 0
        elif ((location / 25 < 1.0) and (location / 25 >= 0)):
            try:
                #print("elif {} {} {}".format(location,l,(alphabet[location])))
                coded_message.append(alphabet[location])
            except IndexError:
                print("Oops, something happened")
            
        else:
            #new location if it's towards the beginning of the alphabet
            location = location + 26
            try:
                #print("else {} {} {}".format(location,l,(alphabet[location])))
                coded_message.append(alphabet[location])
            except IndexError:
                #print("ELSE IndexError {}".format(location))
                print("oops, something ELSE happened")

        #print("Code Message " + ''.join(coded_message))

            
    return ''.join(coded_message)

#print(code_message("hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!"))
    

"""define two functions decoder(message, offset) and coder(message, offset)
that can be used to quickly decode and code messages given any offset."""

def decoder(message, offset):
    decoded_message = []
    for l in message:
        i = alphabet.find(l)        
        #position of the decoded message
        location = i + offset
       
        #if the letter is a space, then just add it to the message
        if (l == ' ' or l == '?' or l == '.' or l == '!'):
            decoded_message.append(l)            
        #26 letters in the alphabet, but index starts at 0
        elif ((location / 25 < 1) and (location / 25 >= 0)):
            try:                
                decoded_message.append(alphabet[location])
            except IndexError:
                print("Oops, something happened")
            
        else:
            #new location if it's towards the end of the alphabet
            location = location - 26
            try:
                decoded_message.append(alphabet[location])
            except IndexError:
                print("oops, something ELSE happened")

            
    return ''.join(decoded_message)

def coder(message, offset):
    coded_message = []
    for l in message:
        i = alphabet.find(l)
        #position of the coded message
        location = i - 10
        #print(l, location)
       
        #if the letter is a space, then just add it to the message
        if (l == ' ' or l == '?' or l == '.' or l == '!'):
            #print("if {} {}".format(location,l))
            coded_message.append(l)            
        #26 letters in the alphabet, but index starts at 0
        elif ((location / 25 < 1.0) and (location / 25 >= 0)):
            try:
                #print("elif {} {} {}".format(location,l,(alphabet[location])))
                coded_message.append(alphabet[location])
            except IndexError:
                print("Oops, something happened")
            
        else:
            #new location if it's towards the beginning of the alphabet
            location = location + 26
            try:
                #print("else {} {} {}".format(location,l,(alphabet[location])))
                coded_message.append(alphabet[location])
            except IndexError:
                #print("ELSE IndexError {}".format(location))
                print("oops, something ELSE happened")

        #print("Code Message " + ''.join(coded_message))

            
    return ''.join(coded_message)

#print(decoder("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.",10))

#print(decoder("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!",14))
    
def ceasar_noshift(message):
    i = 0
    while (i < 26):
        print(decoder(message,i))
        i += 1

ceasar_noshift("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.")


        
          
