#4.1

# lista = range(1000001)                                                   # Skriver en lista med alla nummer mellan 0 och 1000000. det är 1000001 eftersom det första numret är 0

# summa = 0                                                                #skapar variabels summa och ger den värdet 0

# for nummer in lista:                                                     
#     summa += nummer                                                      # adderar alla nummer i listan till summa vilket är samma sak som att addera alla nummer i listan eftersom summa startar på noll

# print(summa)                                                             # Skriver ut summan

#4.2


# lista = range(1, 500, 2)  	                                           

# summa = 0

# for nummer in lista:
#     summa += nummer

# print(summa)


#4.3



# registrerade= ["Anna", "Lars", "Filip", "Oliver", "Knut"]
# avanmälda= ["Anna", "Lars"]                                                           #listor över namn på registrerade och avanmälda

# for namn in avanmälda:
#     registrerade.remove(namn)                                                         # Tar bort dom avanmälda ur listan registrerade

# print (registrerade)                                                                  # Skriver ut de registrerade

#4.4

# förnamn = ["Maria", "Erik", "Karl"]
# efternamn = ["Svensson", "Andersson", "Karlsson"]                                     # Lista för förnamn och efternamn som ska kombineras

# for fnamn in förnamn:
#     for enamn in efternamn:
#         print (fnamn + enamn)                                                         # Skriver ut alla möjliga kombinationer av förnamn och efternmamn
