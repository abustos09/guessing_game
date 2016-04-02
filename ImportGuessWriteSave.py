from sys import argv

script, filename = argv

name = raw_input("Hello! What is your name?")

txt = """Nice to meet you %s, my name is bot. Lets play a game...... I will select a 
random number between 1 and 10 and you will have 3 chances to guess it, ok?""" % name
import sys
import time
for line in txt:
	for char in line:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(.125)
		
print "\n"
raw_input("Hit Return to start")

import random

number = random.randint(1,10)



txt = open(filename, "a")

txt.write(name)
txt.write("\n")
txt.write("The correct number is: ")
txt.write(str(number))
txt.write("\n")

txt.close()


def numberguess(n, f):
	count = 1
	while count < 4:
		try:
			g = int(raw_input("What is your guess?"))
		except ValueError:
			print "Try again... that is not a number"
			continue
			
		if g == n:
			tx = open(f, "a")
			tx.write("Your correct guess is: ")
			tx.write(str(g))
			tx.close()
			if count == 1:
				print "\n"
				print "Fuego!!! On the first try!"
				break
					
			print "Right on! You guessed the right number!"
			break
			
		
		elif g == n-1 or g == n+1:
			print "you are so close!"
		
		elif g == n-2 or g == n+2:
			print "getting warmer"
		else:
			print "Wrong! Strike ", count, "Guess again"
			
		count += 1
		
	else:
		print "Game over you lose!"	
	
numberguess(number, filename)

# warmer colder
#txt = open(filename, "a")

#txt.write("You guessed: ")
#txt.write(str(guess))

#txt.close()
#else:
#			print "Wrong! Strike ", count, "Guess again"
#		count += 1