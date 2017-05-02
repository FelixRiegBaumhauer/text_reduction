
#FXN 1, pulls in the text
def pull_text():
    stream = open("Constitution.txt", "r").read()

    lines = stream.split("\n")
    elements = []
    for strophe in lines:
        elements.extend(strophe.split(" "))

    elements = map(lambda x: x.rstrip('').strip('\",.*&%$#[]').replace('\r',''), elements)
    elements = filter(lambda x: len(x)>0, elements)

    return elements

container = pull_text()

#FXN #2 finds the frequncy of a single word
def find_freq(w):
    return len(filter(lambda x: x==w or x==w.lower() or x.lower()==w, container))


#FXN #3 find the frequcny of a group
def  group_freq(a, b, c):
    return find_freq(a) + find_freq(b) + find_freq(c)


#FXN #4 find the most frequent word
def most_freq():
    mah_list = []
    champ = container[0]
    
    for a in container:
        if(a not in mah_list):
            mah_list.append(a)
            if find_freq(a) > find_freq(champ):
                champ = a
                
    #champ = mah_list[0]
    #for b in mah_list:
    #    if find_freq(b) > find_freq(champ):
    #        champ = b
    return champ

print ("The number of occurences of 'The': "+str(find_freq("The")))

print ("The number of occurnces of 'The', 'Is', 'are': "+str(group_freq("The", "Is", "are")))

print("The most frequnt word is: "+str(most_freq()))


