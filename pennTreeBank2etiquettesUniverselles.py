import re

pathBase = "../TP_1/"

# Cette fonction permet de créer un dictionnaire ayant les POS Penn Tree comme clés, les POS universels comme valeurs
def creatDicoRef(chemin: str):
    with open(pathBase+chemin, "r") as reference:
        reference = reference.readlines()
        dico_ref = {}
        for line in reference:
            dico_ref[line.strip().split()[0]] = line.strip().split()[1]
    return dico_ref

dico_ref = creatDicoRef("POSTags_PTB_Universal_Linux.txt")


# Cette fonction permet de mettre les mots et leur POS associé dans une liste pour l'utiliser ultérieurement
def txt2List(chemin: str):
    with open(pathBase+chemin, "r") as text:
        text = text.readlines()
        listItems = []
        for line in text:
            line = re.sub("\n", "", line)
            line = line.split()
            for item in line:
                item = item.split("_")
                listItems.append(f"{item[0]}_{dico_ref[item[1]]}")
    return listItems

listItems = txt2List("wsj_0010_sample.txt.pos.stanford")


# Cette fonction permet de basculer les éléments de "listItems" dans le fichier que nous voulons obtenir
def write2txt(chemin: str):
    with open(pathBase+chemin, "w") as text:
        for item in listItems:
            if item != "._.":
                text.write(item+" ")
            else:
                text.write(item+"\n")


write2txt("wsj_0010_sample.txt.pos.univ.stanford")
write2txt("wsj_0010_sample.txt.pos.univ.ref")
