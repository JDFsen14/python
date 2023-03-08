"""
This program will let the user type a word and convert that
word to a Soundex code number.
"""
#02/15/2023
#Jaren Frandsen
#CSIS 1300

#Setting up the function to be called whenever sending a word through the soundex system
#Wanted to mess around with functions in Python, so this will be my creative element.
def soundex(string):

    #Starting the soundex word with the letter it starts with
    SoundexWord = string[0] + ""

    #for loop that will check each position in the normal word and will see if it needs to be changed
    for i in range(1, len(string)):

        #Checks if the current position in the word corresponds to the soundex code number '1' and removes repeats
        if(string[i] == 'b' or string[i] == 'f' or string[i] == 'p' or
           string[i] == 'v'):
            if  (SoundexWord[-1]!= '1'):
                SoundexWord =  SoundexWord + '1'

        #Checks if the current position in the word corresponds to the soundex code number '2' and removes repeats
        elif (string[i] == 'c' or string[i] == 'g' or string[i] == 'j' or
              string[i] == 'k' or string[i] == 'q' or string[i] == 's' or
              string[i] == 'x' or string[i] == 'z'):
            if  (SoundexWord[-1] != '2'):
                SoundexWord =  SoundexWord +'2'

        #Checks if the current position in the word corresponds to the soundex code number '3' and removes repeats
        elif string[i] == 'd' or string[i] == 't':
            if  (SoundexWord[-1] != '3'):
                SoundexWord =  SoundexWord + '3'

        #Checks if the current position in the word corresponds to the soundex code number '4' and removes repeats
        elif string[i] == 'l' :
            if  (SoundexWord[-1] != '4'):
                SoundexWord =  SoundexWord + '4'

        #Checks if the current position in the word corresponds to the soundex code number '5' and removes repeats
        elif string[i] == 'm' or string[i]== 'n' :
            if  (SoundexWord[-1] != '5'):
                SoundexWord =  SoundexWord + '5'

        #Checks if the current position in the word corresponds to the soundex code number '6' and removes repeats
        elif string[i] == 'r' :
            if  SoundexWord[-1] != '6':
                SoundexWord =  SoundexWord + '6'

    #End of the function. Returns the soundex coded word
    return  SoundexWord

#Asks the user to input a word, and will give the Soundex Coded version as output
normalWord = input ('Enter a word to code : ')
print("\nThe coded word is " + soundex(normalWord))
