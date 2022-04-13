import re
path = "../TP_1/"

# ouvrir le fichier qu'on veut traiter
with open(path+"wsj_0010_sample.pos.ref", "r") as text:
    text = text.readlines()
    listItems = []
    for item in text:
        item = re.sub("\t", "_", item.strip()) # remplacer la tabulation par un "_"
        item = re.sub("\]", "", item) # supprimer "]"
        listItems.append(item)

# créer un fichier pour mettre le résultat
with open(path + "wsj_0010_sample.pos.stanford.ref", "w") as new_text:
    for item in listItems:
        if item == "._.":  # Si on rencontre "._.", on saute une ligne
            new_text.write(item)
            new_text.write("\n")
        else: # Sinon, on ajoute un espace
            new_text.write(item + ' ')