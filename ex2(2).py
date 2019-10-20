
string ='Mystring\nItsnames\bis\tMy File\r55'

# kanw prospelasi to string kai elegxw ean o kathe character einai
# ektupwsimos 
# ean vrw mh ektipwsimo xaraktira auksanw ton counter

count = 0 
for a in string: 
    if (a.isprintable()) == False: 
            count+= 1


with open ("ex2.txt") as f :
    print(count)
