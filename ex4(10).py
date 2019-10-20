text=input("Please input somthing that include parentheses: ")
char1="("
char2=")"

#upologizw poses fores emfanizetai to kathe sumvolo
def count_open_par(text,char):
    count=0
    for p in text:
        if p==char:
            count+=1
    
    return count

if count_open_par(text,char1)!= count_open_par(text,char2):
    print("check your parenhtses")          #o arithos twn "(" kai ")" prepei na einai o idios

if text.index(char1)>text.index(char2):     #afora tin prwti tous emfanisi
    print("check your parenhtses")          #diladi oti ksekinaei sigoura apo "("

count1=0                                    
count2=0
check_problem=False
for i in text:          #elegxw thn periptwsh mias tetoias eisodou: "(..)))..(("
    if i == "(":
        count1+=1
    elif i== ")":
        count2+=1
    else:
        print(None)
    if count2>count1:
        check_problem=True
    

if check_problem==True:
    print("You can't close a parentheses if you haven't open it yet..")
