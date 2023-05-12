import numpy as np
import matplotlib.pyplot as plt

black = np.ones((50, 50))
white = np.zeros((50, 50))

column1 = np.vstack((white, black))
column2 = np.vstack((black, white))

img = np.hstack((column1, column2))
plt.imshow(img, cmap="gray")
plt.show()

#5.
file = open('SMSSpamCollection.txt', encoding="utf-8")
spam = 0
ham = 0
spamExclamation = 0
spamAvg = 0.0
hamAvg = 0.0
for line in file:
    line = line.rstrip()#uklanja praznine s desne strane
    line = line.split()
    if line[0] == 'ham':
        ham += 1
        hamAvg += (len(line)-1)
    else:
        spam += 1
        spamAvg += (len(line)-1)
        if line[-1].endswith('!'): #koristi se -1 za posljednji element, a -2 za predposljednji i tako dalje
            spamExclamation += 1
file.close()
print("Average number of ham SMS: ", hamAvg/ham)
print("Average number of spam SMS: ", spamAvg/spam)
print("Number of messages ending with exclamation: ", spamExclamation)
