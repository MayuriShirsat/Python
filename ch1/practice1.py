# PRACTICE SET1
'''Que1->print twinkel twinkel littel star poem'''

print('''TWINKLE, TWINKLE, LITTLE STAR
Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
When the blazing sun is set, and the grass with dew is wet. Then you show your little
light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
are.
Then the traveler in the dark thanks you for your tiny spark. How could he see where to
go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
As your bright and tiny spark lights the traveler in the dark, though I know not what you
are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are''')

# use (''' or """ to print multi-line string and comment)

'''Que2->print table of 5 using REPL'''
'''Que3->use any external module of your intrest
for this i am installing pyttsx3 module which speak the content i give to it'''

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello sofiya. How are you. where is sahara")
engine.runAndWait()