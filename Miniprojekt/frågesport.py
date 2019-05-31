from random import randint
import random    #Importerar biblioteket random. Behövcde importera randint separat eftersom det inte fungerade annars
import requests  #Importerar biblioteket requests

print("---------------------------------\n Vilken svårighetsgrad vill du ha?\n Lätt \n Medel \n Svår \n---------------------------------")
Svårighet = (input("Ange svårighetsgrad här:"))
Svårighet = Svårighet.title()     #Frågar vilken svårighetsgrad man vill ha och gör svaret till små bokstäver med en stor bokstav i början så att det inte spelar roll vilken sorts bokstäver man använder

print("---------------------------------\n Hur många frågor vill du ha?\n---------------------------------")
Afrågor = int(input("Ange hur många frågor du vill ha här:"))     #Frågar hur många frågor man vill ha och gör om svaret till typen int

points = 0    #Skapar variabeln points och sätter dess värde till 0


urllätt = "https://opentdb.com/api.php?amount=50&difficulty=easy"  #Säger att variablen urllätt till url:en för en öppen api som innehåller 50 lätta frågor
r1 = requests.get ( urllätt )   #Hämtar dictionariet från api:n och döper den till r1
lätt_dictionary = r1.json()      #Gör r1 till ett json objekt och döper det till lätt_dictionary  

print(r1)

urlmedel = "https://opentdb.com/api.php?amount=50&difficulty=medium"    #Säger att variablen urlmedel till url:en för en öppen api som innehåller 50 medel svåra frågor
r2 = requests.get ( urlmedel )  #Hämtar dictionariet från api:n och döper den till r2
medel_dictionary = r2.json()    #Gör r2 till ett json objekt och döper det till medel_dictionary

urlsvår = "https://opentdb.com/api.php?amount=50&difficulty=hard"   #Säger att variablen urlsvår till url:en för en öppen api som innehåller 50 Svåra frågor
r3 = requests.get ( urlsvår )   #Hämtar dictionariet från api:n och döper den till r3
svår_dictionary = r3.json()     #Gör r3 till ett json objekt och döper det till svår_dictionary



if Svårighet == "Lätt":
    dictionary = lätt_dictionary
elif Svårighet == "Medel":
    dictionary = medel_dictionary
elif Svårighet == "Svår":
    dictionary = svår_dictionary
else:
    print("Svårighetsgraden du angav finns inte. Testa med en av svårighetsgraderna ovan") #Bestämmer vilket dictionary som ska användas beroende på svårighetsgraden som angavs

F1 = randint(0,49) #Gör variabels F1 till ett slumpmässigt tal mellan 0 och 49 

Fråga = 0  #Skapar variabeln Fråga och ger den värdet 0




while Fråga < Afrågor:     #Ställer en ny fråga så länge Variabeln Fråga är mindre än antalet frågor man valde i början
    

    if dictionary["results"][F1]["correct_answer"] == "True" or dictionary["results"][F1]["correct_answer"] == "False":
        alternativ = [dictionary["results"][F1]["correct_answer"],dictionary["results"][F1]["incorrect_answers"][0]]
    else:
        alternativ = [dictionary["results"][F1]["correct_answer"],dictionary["results"][F1]["incorrect_answers"][0], dictionary["results"][F1]["incorrect_answers"][1], dictionary["results"][F1]["incorrect_answers"][2]]    #Om frågan är sant eller falskt har den bara två alternativ så då har listan med alternativ bara dessa två altyernativ. Alla andra frågor har fyra alternativ så om det är en fråga som inte är sant eller falsk läggs alla fyra alternativ till i listan alternativ
    
    random.shuffle(alternativ)   #Använder ransom som vi importerade tidigare till att lägga objekten i listan alternativ i slumpmässig ordning

    print ("Question : ", dictionary["results"][F1]["question"])     #Skriver ut en slumpmässig fråga från dictionariet som är valt

    if dictionary["results"][F1]["correct_answer"] == "True" or dictionary["results"][F1]["correct_answer"] == "False":
        print("ALternativ: ","\nA", alternativ[0],"\nB", alternativ[1])
    else:
        print ("ALternativ: ","\nA", alternativ[0],"\nB", alternativ[1],"\nC", alternativ[2],"\nD", alternativ[3])    #Om det är en sant eller falsk fråga som bara har två alternativ skriver den ut de två alternativen som finns i listan alternativ. Annars skriver den ut alla fyra

    svar1 = (input("Svar:"))
    svar1 = svar1.title()      #Frågar om svar och gör det man skriver till små bokstäver med en stor i början

    rätt1 = dictionary["results"][F1]["correct_answer"]  #Gör variabeln rätt1 till rätt svar

    if rätt1 == alternativ[0]: 
        rätt1 = "A"
    elif rätt1 == alternativ[1]: 
        rätt1 = "B"
    elif rätt1 == alternativ[2]: 
        rätt1 = "C"
    elif rätt1 == alternativ[3]: 
        rätt1 = "D"                #Kollar vilken position i listan som innehåller rätt svar och gör om rätt1 till bokstaven som representerar det svaret

    if svar1 == rätt1:   
        print ("Rätt svar")
        points += 1
        print ("poäng: ", points,"\n ----------------------\n")
        Fråga += 1
        F1 = randint(0,49)                  #Om det bokstaven man skrivit matchar bokstaven som är rätt skriver den ut rätt svar, Lägger på en poäng samt skriver ut poäng. Ger variabeln F1 ett nytt slumpmässigt värde mellan 0 och 49 och lägger på ett på variabeln fråga
    else:
        print("Fel svar. Rätt svar var: ", dictionary["results"][F1]["correct_answer"],". poäng: ", points,"\n ----------------------\n")
        Fråga += 1
        F1 = randint(0,49)          #Du inte rätt skriver den ut rätt svar samt din totala påäng. Sedan läggerd en på ett på variablen fråga och ger variabeln F1 ett nytt slumpmässigt värde mellan 0 och 49
print("Din slutpoäng är: ", points,"\n Antal frågor: ", Afrågor, "\n Svårighetsgrad: ", Svårighet)   #När Frågorna är lut skriver den ut din totala poäng, hur många frågor du svarat på samt vilken svårighet du kört på