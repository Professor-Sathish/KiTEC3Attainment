from RG import cocal
cocount=int(input("How many co's : "))
total=int(input("What is the Total Mark that you uploaded : "))
if cocount==2:
    if total==50:
        cocal.twococalc50()
    elif total==100:
        spliter=int(input("split a mark by 50 or 100 : "))
        if spliter==50:
            cocal.twococalc100()
        elif spliter==100:
            cocal.twococalc100100()    
    else:
        print("wrong in total mark")
elif cocount==5:
    cocal.fivecocalc()

