file=open("song.txt")
dictionary={}
counter=0
for line in file :
    for word in line.split():
        if word in dictionary.keys():
            value=dictionary.get(word)
            dictionary.update({f"{word}": value+1})
        else:
            dictionary.update({f"{word}": 1})


for value in dictionary.values():
    if value == 1:
        counter +=1     

print(f"Number of unique words: {counter}")

for item in dictionary.items():
    print(item)
    
file.close ()