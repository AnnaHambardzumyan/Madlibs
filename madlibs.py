import random

def type1():
	number = input("Input a Number: ")
	time = input("Input a Measure of time: ")
	trans = input("Input a Mode of Transportation: ")
	adj = input("Input an Adjective: ")
	adj1 = input("Input another Adjective: ")
	noun = input("Input a Noun: ")
	color = input("Input a Color: ")
	bodypart = input("Input Part of the Body: ")
	verb = input("Input a Verb: ")
	number1 = input("Input another Number: ")
	noun1 = input("Input another Noun: ")
	noun2 = input("Input a Noun again: ")
	bodypart1 = input("Input another Part of the body: ")
	verb2 = input("Input another Verb: ")
	noun3 = input("Input a Noun one more time: ")
	adj2 = input("Input an Adjective again: ")
	silly = input("Input a Silly Word: ")
	noun4 = input("Input a Noun one last time: ")

	story = f'''It was about {number} {time} ago when I arrived at the hospital in a {trans}. The hospital is a/an {adj} place, there are a lot of {adj1} {noun} here. There are nurses here who have {color} {bodypart}. If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {number1} {noun1}. Today I talked to a doctor and they were wearing a {noun2} on their {bodypart1}. I heard that all doctors {verb} {noun3} every day for breakfast. The most {adj2} thing about being in the hospital is the {silly} {noun4} !'''
	print(story)

def type2():
	name = input("Input a Proper Noun (Person’s Name): ")
	noun = input("Input a Noun: ")
	adj = input("Input an Adjective(Feeling): ")
	verb = input("Input a Verb: ")
	adj1 = input("Input another Adjective(Feeling): ")
	animal = input("Input a(n) Animal: ")
	verb1 = input("Input another Verb: ")
	color = input("Input a Color: ")
	verbing = input("Input a Verb (ending in ing): ")
	adv = input("Input an Adverb (ending in ly): ")
	number = input("Input a Number: ")
	time = input("Input a Measure of Time: ")
	color1 = input("Input another Color: ")
	animal1 = input("Input another Animal: ")
	number1 = input("Input another Number: ")
	silly = input("Input a Silly Word: ")
	noun1 = input("Input another Noun: ")

	story = f'''This weekend I am going camping with {noun}. I packed my lantern, sleeping bag, and {noun}. I am so {adj} to {verb} in a tent. I am {adj1} we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb1}. I have heard that the {color} lake is great for {verbing}. Then we will {adv} hike through the forest for {number} {time}. If I see a {color1} {animal1} while hiking, I am going to bring it home as a pet! At night we will tell {number1} {silly} stories and roast {noun1} around the campfire!! '''
	print(story)

def type3():
	name = input("Input a Proper Noun (Person’s Name): ")
	adj = input("Input an Adjective(Feeling): ")
	color = input("Input a Color: ")
	animal = input("Input a(n) Animal: ")
	place = input("Input a Place: ")
	adj1 = input("Input another Adjective(Feeling): ")
	magcr = input("Input Magical Creature (Plural): ")
	adj2 = input("Input another Adjective: ")
	magcr1 = input("Input another Magical Creature (Plural): ")
	room  = input("Input a Room in a House: ")
	noun = input("Input a Noun: ")
	noun1 = input("Input another Noun: ")
	noun2 = input("Input a Noun(Plural) again: ")
	adj3 = input("Input an Adjective one more time: ")
	noun3 = input("Input another Noun(Plural): ")
	number = input("Input a Number: ")
	time = input("Input a Measure of Time: ")
	verbing = input("Input a Verb (ending in ing): ")
	adj4 = input("Input an Adjective again: ")
	noun4 = input("Input a Noun one last time: ")

	story = f'''Dear {name}, I am writing to you from a {adj} castle in an enchanted forest. I found myself here one day after going for a ride on a {color} {animal} in {place}. There are {adj1} {magcr} and {adj2} {magcr1} here! In the {room} there is a pool full of {noun}. I fall asleep each night on a {noun1} of {noun2} and dream of {adj3} {noun3}. It feels as though I have lived here for {number} {time}. I hope one day you can visit, although the only way to get here now is {verbing} on a {adj4} {noun4}!! '''
	print(story)


try:
	temp = int(input("Choose 1 of 3 templates or type 0 for random choice: "))
	if temp == 1:
		type1()
	elif temp == 2:
		type2()
	elif temp == 3:
		type3()
	else:
		r = random.randint(1, 3)
		if r == 1:
			type1()
		elif r == 2:
			type2()
		else:
			type3()
except:
	print("Invalid choice, try again")
