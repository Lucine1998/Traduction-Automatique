path = "../TP_1/"
listOftypesWords = []
dico_words = {}
numWord = 0
listOfWords =[]
with open(path+"wsj_0010_sample.txt.ner.stanford", "r") as text:
    text = text.read().strip().split(" ")
    for item in text:
        #word, type = item.split("/")
        item = item.split("/")
        if item[1] == "O":
            pass
        else:
            listOftypesWords.append((item[0], item[1])) # item[0]->word, item[1]->type
            listOfWords.append(item[0])

    for word in listOfWords:
        numWord = listOfWords.count(word)
        dico_words[word] = numWord

tplt = "{:^10}\t{:^15}\t{:^5}\t{:^10}\n"
tplt2 = "{:^15}\t{:^15}\t{:^15}\t{:^25}\n"
print(tplt.format("Entité nommée", "Type", "Nombre d’occurrences", "Proportion dans le texte (%)"))
for e, t in listOftypesWords:
    print(tplt2.format(e, t, dico_words[e], str(dico_words[e]/len(listOfWords)*100)[:5]+"%"))