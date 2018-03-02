def getBuilding(src):
        classdict = {
        "CS" : "Computer Science Building",     #33.882148, -117.882660
        "SGMH" : "Mihaylo",                     #33.878866, -117.883385
        "PL" : "Pollak Library",                #33.881530, -117.885766
        "MH" : "McCarthy Hall",                 #33.879864, -117.885550
        "E" : "Engineering Building",           #33.882177, -117.883186
        "H" : "Humanities-Social Sciences",     #33.880497, -117.884462
        "KHS" : "Kinesiology & Health Science", #33.882628, -117.885890
        "cs" : "Computer Science Building",
        "sgmh" : "Mihaylo",
        "pl" : "Pollak Library",
        "mh" : "McCarthy Hall",
        "e" : "Engineering Building",
        "h" : "Humanities-Social Sciences",
        "khs" : "Kinesiology & Health Science"
        }
        abv = ""
        if len(src) > 3:
                if src[-3] in ("0", "1", "2", "3", "4", "5"):
                        src = src[:-3]
        for i in src:
                if i != "-":
                        abv = abv + i
                else:
                        break
        if abv in classdict:
                building = classdict[abv]
                building.upper()  #makes sure upper AND lower case will work
        else:
                building = ''


#        if building == "CS":
#                continue
                #building = "33.882148, -117.882660"

#        elif building == "SGMH":
 #               continue
                #building = "33.878866, -117.883385"


        return building


#var end =  "{{ src }}, Fullerton";  this was line 13


        



