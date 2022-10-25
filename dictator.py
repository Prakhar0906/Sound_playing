from gtts import gTTS
import time
from ast import ListComp
import random 
import linecache
import os
from audioplayer import AudioPlayer

# for playing note.mp3 file

start = 1
end = 316

work_on = []

print("Hello World")
# line = random.randrange(1,103,1)

# line_read = linecache.getline('words.txt',line)

# line_str = line_read.split(' ')
done = []

def find_word():
	#print("Function has been called")
	while True:
		line = random.randrange(start,end+1)
		line_read = linecache.getline('words.txt',line)
		line_str = line_read.split(' ')
		#print("Open success")
		for i in line_str:
			print(i)
			if not i.isdigit():
				break
			 
			if i not in done:
				print("The Word Number is:",i)
				done.append(i)
				#print(done)
				print(len(done))
				#print(line_read)
				return(line_read)
					

def format_word(line):
	line_sep="".join(c for c in line if c.isalnum())
	line_sep = line.split(' ')
	#print(line_sep)
	for i in line_sep:
		if i.istitle():
			#print(line.partition(i)[:1])
			return (line.partition(i)[:1])
	

def final_seperation(word):
        word_l = word[0].split(' ')
	#print(word)
        for i in word_l:
                if i.isupper():
                        mytext = i
                        language = 'en'
                        myobj = gTTS(text=mytext, lang=language, slow=False)
                        myobj.save("word.mp3")
                        AudioPlayer("word.mp3").play(block=True)
                        spell = input("Enter the Spelling:")
                        if spell == ((mytext.lower()).lstrip()).rstrip():
                                print("correct")
                        else :
                                print("Wrong :", mytext)
                                work_on.append(mytext)
                                
                        mean_check = input("Do you know to meaning(Enter for yes 1 for no)?")

                        if mean_check:
                                print("You do not know the meaning")
                                if mytext not in work_on:
                                        work_on.append(mytext)
                        


		
def main():
	print("Starting...")
	while True:
		cont = input("Continue(press enter to continue and 1 to exit)?")
		if cont:
			cont = input("confirm(enter 1 to confirm)?")
			if cont:
                                print("Words to work on")
                                for i in work_on:
                                        print(i)
                                        
                                return
		else :
			if len(done)!= end:		
				word = final_seperation(format_word(find_word()))
			else :
				print("All Done")
				done.clear()
				return
				

	#print(word)

# This module is imported so that we can 
# play the converted audio
  
# The text that you want to convert to audio

  
# Playing the converted file

#time.sleep(500)
#os.system("welcome.mp3")
#main()

while True:
    mode = int(input("""
    Please Select the Mode using the number key:
    1) All Random 
    2) Ranged
    3)Quit
    """))
    if mode == 1:
            print("Mode 1 selected")
            main()
    elif mode == 2:
            print("Reference the words.txt for the line not the list")
            start = int(input("Enter the starting Line:"))
            end = int(input("Enter the Ending Line:"))
            if start >= end:
                    print("Invalid start and end enter again")
                    continue
            else:
                    main()
    else :
    	break
        	
	
