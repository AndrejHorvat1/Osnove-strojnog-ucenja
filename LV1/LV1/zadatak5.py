file = open("SMSSpamCollection.txt")
lines = file.readlines()
wordsHam = 0
wordsSpam = 0
counterHam = 0
counterSpam = 0

exclamation_mark_SMS = 0
for line in lines:
    words = line.split()
    if(words[0] == "ham"):
        wordsHam=wordsHam+len(words)-1
        counterHam+=1
    elif(words[0]=="spam"):
        wordsSpam=wordsSpam+len(words)-1
        counterSpam+=1
        if words[-1]=="!":
            exclamation_mark_SMS+=1
            
print(f"Average number of words in ham: {wordsHam/counterHam}")
print(f"Average number of words in spam: {wordsSpam/counterSpam}")
print(f"Number of spam ending with exclamation mark: {exclamation_mark_SMS}")