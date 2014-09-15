import sys
import random

lines = [	"Long walks at night--",
			"that's what good for the soul: ", 
			"peeking into windows",
			"watching tired housewives",
			"trying to fight off",
			"their beer-maddened husbands."]

wordsCorrect = 0
linesSeen = 0

easyMode = True

def getLineArray(line):
	return line.split(" ")

def wordToBlanks(word):
	length = len(word)
	return "_" * length

for line in lines:
	lineArray = getLineArray(line)
	blank = random.choice(lineArray)
	lineArray[lineArray.index(blank)] = wordToBlanks(blank)
	word = str(raw_input(" ".join(lineArray) + "\n"))
	if(easyMode):
		word = word.lower().strip()
		blank = blank.lower().strip()
	if(word == blank):
		print "Correct!"
		wordsCorrect += 1
	else:
		print "Incorrect.\n%s" % line
	linesSeen += 1
	print "%d / %d" % (wordsCorrect, linesSeen)