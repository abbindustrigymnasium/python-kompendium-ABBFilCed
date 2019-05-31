#5.1
# kön = (input("Ange kön "))

# hår = (input("Ange hårfärg "))

# Ögon = (input("Ange Ögonfärg "))                                                          #klienten skriver in sin hårfärg, kön och ögonfärg

# if kön == "man":
#     if hår == "brun":
#         if Ögon == "brun":
#             print ("egenskaper matchar med Daniel Radcliffe")                             #om man har egenskaper liknande daniel radcliffe skriver den det
    

# if kön == "man":
#     if hår == "röd":
#         if Ögon == "blå":
#             print ("egenskaper matchar med Rupert Grint")                                  #om man har egenskaper liknande Rupert Grint skriver den det

# if kön == "kvinna":
#     if hår == "brun":
#         if Ögon == "brun":
#             print ("egenskaper matchar med Selena Gomez och Emma watson")                 #om man har egenskaper liknande Emma watson skriver den det
            
# else:
#     print("Ditt utseende matchar inte med någon!")                                        #matchar man ingen skriver den det

#5.2

# namn = (input("Ange din namn"))
# ålder = int(input("Ange din ålder"))                                                      #klienten skriver sitt namn och ålder

# if ålder == 1:
#     sömn = "14"
# elif ålder == 2:
#     sömn = "13"
# elif ålder == 3:
#     sömn = "12"
# elif ålder == 4:
#     sömn = "11,5"
# elif ålder == 5 or 6:
#     sömn = "11"
# elif ålder == 7:
#     sömn = "10,5"
# elif ålder == 8 or 9 or 10:
#     sömn = "10"
# elif ålder == 11:
#     sömn = "9,5"
# elif ålder == 12 or 13 or 14 or 15:
#     sömn = "9"
# elif ålder == 16:
#     sömn = "8,5"
# else:
#     sömn = "8"                                                    # bestämmer variabeln sömn beroende på åldern klienten angav

# print("Hallå ", namn, ". Personer i din ålder (",ålder , ") behöver", sömn, " timmars sömn per natt enligt vårdguiden")    #Skriver hur mycket sömn klienten behöver

#5.3

# land = (input("var kommer du ifrån? "))                                                           #Klienten skriver vilket land hen kommer ifrån och detta får variabeln land. 
# land = land.title()                                                                               # Land blir landet klienten skrev in men med stor bokstav i början och resten små så att det inte spelar roll vilken sorts bokstäver klienten använde 
# if land == "Danmark" or "Finland" or "Island" or "Norge" or "Sverige":
#     print("Ditt land (", land,") tillhör norden ")                                                # Om landet matchar ett land i norden skriver den det
# elif land == "England" or "Nordirland" or "Skottland" or "Wales":
#     print("Ditt land(", land, ") tillhör storbrittanien!")                                        # Om landet matchar ett land i storbrittanien skrivs det
# else:
#     print("Ditt land(", land, ") hör varken till Norden eller storbrittanien")                    # Matchar landet varken storbrittanien eller norden skriver den det

