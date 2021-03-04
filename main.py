from trainer import *
from BotActionChart import *

prevTag = "test" #stores the previous input type from the user, used to handle the user saying yes or no
errorString = "Sorry, I'm not sure what you are trying to say. Could you please try again."

#predict with model
def bag_of_words(s, words):
	bag = [0 for _ in range(len(words))]

	s_words = nltk.word_tokenize(s)
	s_words = [stemmer.stem(word.lower()) for word in s_words]

	for se in s_words:
		for i, w in enumerate(words):
			if w == se:
				bag[i] = 1

	return numpy.array(bag)

def chat():
	print("Start talking with the bot (type quit to exit)!")
	while True:
		inp = input("You: ")
		if inp.lower() == "quit":
			break


		results = model.predict([bag_of_words(inp, words)])[0]
		results_index = numpy.argmax(results)
		tag = labels[results_index]
		if isInputYesOrNo(tag):
			print(handleYesOrNoInput(tag, prevTag))
			prevTag = ''
		else:
			if results[results_index] > 0.7:
				for tg in data["intents"]:
					if tg['tag'] == tag:
						responses = tg['responses']

				print(random.choice(responses))
				if isInputExplain(tag):
					handleExplain()
				prevTag = tag
			else:
				print(errorString)

def isInputYesOrNo(tag):
	keyTags = ["confirmation", "decline"]
	if any(tag in s for s in keyTags):
		return True

def handleYesOrNoInput(tag, previousTag):
	try:
		s = actionChart[previousTag][tag]
	except:
		s = errorString
	return s

def isInputExplain(tag):
	if tag == "explain":
		return True

def handleExplain():
	inp = input("You: ")
	print("Thanks for letting me know.");

chat()