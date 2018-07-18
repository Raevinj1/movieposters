from random import *

def setup():

    
#First List
    descriptors = [
                   "They're Back and They're Better ",
                   "Look Who's Back in Town ",
                   "In a World With ",
                   "Legend of ",
                   ]
    
    def title(desc):
        print(desc)
        
    for i in range (1):
        titleList = randint (0, len (descriptors) -1)
        title (descriptors [titleList])
        
#Character List
    characters = [
                  "PowerPuff Girls",
                  "The Rock",
                  "Princess Tiana",
                  "Lucifer",
                  ]
    
    def show(person):
        print(person)
         
    for i in range (1):
         theName = randint (0, len(characters) -1)
         show (characters[theName])
    
#Tagline
    tagline = [
               "Back Like Never Before ",
               "Last Time Just Wasn't Enough",
               "The Final Chapter",
               "There Won't be A Next Time",
               ]
    
    def tag(movie):
        print(movie)
        
    for i in range(1):
        movieName = randint (0, len(tagline) -1)
        tag (tagline[movieName])
