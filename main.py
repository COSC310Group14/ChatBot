from trainer import *
from synonym import *
from BotActionChart import *
#from GuiControl import *

#author: MichaelOdermatt

bot_name = "Thera-bot"
prevTag = 'None' #stores the previous input type from the user, used to handle the user saying yes or no
errorString = ["I'm afraid I don't know what you mean.", "What was that?", "Could you trying saying that again?", "Sorry, my systems are limited. Could you try again?", "I'm not sure I understand"]

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

# initiates the conversation and predicts passes the input to the model. It predicts which type of response to give
# and chooses one randomly from the selected words.
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
                print(getErrorString())


def isInputYesOrNo(tag):
    keyTags = ["confirmation", "decline"]
    if any(tag in s for s in keyTags):
        return True

def handleYesOrNoInput(tag, previousTag):
    global prevTag
    try:
        s = actionChart[previousTag][tag]
    except:
        s = getErrorString()
    prevTag = 'None'
    return s

def isInputExplain(tag):
    if tag == "explain":
        return True

def handleExplain():
    inp = input("You: ")
    return "Thanks for letting me know."

def getErrorString():
	return random.choice(errorString)

def get_response(inp):
    #find synonyms
    synonimousPhrases = findSynonyms(inp)
    synonimousPhrases.insert(0, inp)
    print(synonimousPhrases)
    for phrase in synonimousPhrases:
        print("phrase: ", phrase)
        global prevTag
        results = model.predict([bag_of_words(phrase, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        if results[results_index] > 0.7:
            if isInputYesOrNo(tag):
                print(prevTag)
                return handleYesOrNoInput(tag, prevTag)
            else:
                for tg in data["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']

                if isInputExplain(tag):
                    return handleExplain()
                prevTag = tag
                print(prevTag)
                return random.choice(responses)
    ## if we have iterated through all possible synonimous options we return error string
    return getErrorString()


#where the code starts
#chat()
#app = ChatApplication()
#app.run()