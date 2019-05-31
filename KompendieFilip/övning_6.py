#6.1

# import requests
# url = "https://77.238.56.27/examples/numinfo/?intiger=100"
# r = requests.get ( url )
# response_dictionary = r.json()
# print ( response_dictionary )

#6.2

# stad = (input("ange stad: "))                                                                   #Ange vilken stad du vill se vädret för

# import requests

# url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/"+stad                   # Importera väder bibliotek
# r = requests.get(url)
# response_dictionary = r.json()                                                                  # Gör väderbiblioteket till ett json objekt och ger det variabeln response_dictionary

# print("---------------------------------\n            Forecasts             \n*********************************\nStad: ", stad)
# for day in response_dictionary["forecasts"]:
#     print(day["date"],"   ", day["forecast"])
# print("---------------------------------")                                                       #Skriver ut datum och väder för den valda staden

#6.3

# import requests

# url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
# r = requests.get(url)
# response_dictionary = r.json()                                                #Hämtar biblioteket och ger det variabeln response_dictionary samt gör om det till ett json objekt      

# print("----Artist DB----")

# for artist in response_dictionary["artists"]:
#     print(artist["name"])                                                     #Skriver ut namnet på alla artister i biblioteket

# print("-----------------")

# vartist = (input("Select artist:\n"))                                         #Ber klienten skriva in en artist och ger artisten variabeln vartist som står för vald artist

# print("-----------------")

# vartist = vartist.title()                                                     #Gör att den valda artisten stär med stor bokstav och sedan små bokstäver så att det inte spelar roll vilken sorts bokstäver klienten använde

# if vartist == "Avicii":
#     vartist = 1
# elif vartist == "Ariana grande":
#     vartist = 0
# elif vartist == "Blink-182":
#     vartist = 2
# elif vartist == "Brad Paisley":
#     vartist = 3
# elif vartist == "Ed Sheeran":
#     vartist = 4
# elif vartist == "Imagine Dragons":
#     vartist = 5
# elif vartist == "Maroon 5":
#     vartist = 6
# elif vartist == "Scorpions":
#     vartist = 7
# else:
#     print("fel")                                                              # Gör att Vartist blir nummret artisten har i listan istället för namnet på artisten så att vi ska kunna hämta id. Finns inte namnet som klienten skrev in skrivs ett felmeddelande ut 


# import requests

# url2 = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"+response_dictionary["artists"][vartist]["id"]   #Hämta ett andra bibliotek med hjälp av id som hör till artisten klienten skrev in
# r2 = requests.get(url2)                                                       
# response_dictionary2 = r2.json()                                              # Gör biblioteket till en json och ger den variabeln response_dictionary2

# print ("Name:")

# print(response_dictionary2["artist"]["name"])                                 # Skriver ut artistens namn

# print ("------------------" ,"\n Years active:")

# for years_active in response_dictionary2["artist"]["years_active"]:           # Skriver år artisten varit aktiv
#     print (years_active)

# print ("------------------" ,"\n Members:")

# for members in response_dictionary2["artist"]["members"]:                     #Skriver medlemmar i bandet / artisten
#     print (members)

# print ("------------------" ,"\n genres:")

# for genres in response_dictionary2["artist"]["genres"]:                       # Skriver genrer artisten spelat
#     print (genres)
   


