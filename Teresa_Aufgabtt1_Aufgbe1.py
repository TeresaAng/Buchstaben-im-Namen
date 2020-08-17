vorname = "Teresa" 
nachname = "Angelopoulos"

laengevor = len(vorname) 
laengenach = len(nachname)
laengename = laengevor + laengenach

name = vorname + " " + nachname
print("Mein Name ist " + name + " und er ist " + str(laengename) + " Buchstaben lang.")

vokale = ["a", "e", "i", "o", "u"]
stelle = laengename % 5  # Ermittelter Vokal
vorkommen = vokale[stelle-1] in vokale
print("Der ", stelle, ". Vokal in der Liste ist '", vokale[stelle-1],
      "' und er kommt in meinem Namen vor: ", vorkommen, ".", sep="")

i = 0
for i in range(0,5):
    vork = vokale[i] in name   # Vorkommen
    print("Der Vokal '",  vokale[i], "' kommt in meinem Namen vor: ", vork, ".", sep="")
    
