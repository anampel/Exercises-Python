#epilegw to zeugari "my"
#me to anoigma tou erxeiou ex3
#kanw mia prosperali gia kathe character
#kai ean sumpeftoun auksanw ton counter

with open ("ex3.txt") as f:
    text=f.read()
    count=0
    for i in text:
        for j in text:
            if i=="m" and j=="y":
                    count+=1

    perc=100*count/len(text)    #pososto emfanisis
    print("{0}-{1}%".format("my",round(perc,2)))    #metatropi se string kai strogkilopoihsi

