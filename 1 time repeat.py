while True:
    sentence=input("i love you")
    words = sentence.split()
    number_of_words = len(words)
    counter=0
    for x in sentence:
        if x in "!?.":
            counter=counter+1
    print("There is "+str(counter)+" sentences and " + str(number_of_words) + "words")
    if input('Do you want to repeat(y/n)') == 'n':
        break