#CO SPLITUP GENERATOR
import random
import math
import sys
import csv

#Welcome to the CO Attainment Generator

print(" Hi Team \n", "--> Don't Get Stressed \n","--> I  simplified your work , support of PYTHON\n")
def twococalc():
    #Intialize the Mark list as empty list
    ml=[]
    #To read the Mark List from inputm.csv file from stored Location
    with open('inputm.csv', newline='') as f:
        reader = csv.reader(f)
        totall=[list(map(int,rec)) for rec in csv.reader(f, delimiter=',')]
    #To update the Mark List from Readed CSV File
    for i in range(len(totall)):
        ml.append(math.ceil((totall[i][0])/2)) 
    #Get CO1 and CO2 Mark Splitup
    CO1=int(input("Enter 1st CO Splitup Mark :"))
    CO2=int(input("Enter 2nd CO Splitup Mark :"))
    assname=input("Enter Assesment name :")
    subname=input("Enter Subject name :")
    fname=(assname+subname)+".csv"
    studentcount=len(ml)
    #To intialize the student number list,co1 mark list, co2 marklist
    stuco1ml=[]
    stuco2ml=[]
    #Random Generator
    for i in range(studentcount):
        Flag=True
        total=ml[i]
        while Flag:
            a=random.randint(10,CO1)
            b=random.randint(10,CO2)
            tt=a+b
            if tt==total:
                Flag=False
        stuco1ml.append(a)
        stuco2ml.append(b)
    # Generated Random Values to store the output CSV file
    with open(fname, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["CO1 Mark", "CO2 Mark","Total Mark"])
        for i in range(studentcount):
           writer.writerow([stuco1ml[i], stuco2ml[i],ml[i]])

def fivecocalc():
    #Intialize the Mark list as empty list
    ml=[]
    #To read the Mark List from inputm.csv file from stored Location
    with open('inputm.csv', newline='') as f:
        reader = csv.reader(f)
        totall=[list(map(int,rec)) for rec in csv.reader(f, delimiter=',')]
    
    #To update the Mark List from Readed CSV File
    for i in range(len(totall)):
        ml.append(totall[i][0]) 
    #Get CO1 and CO2 Mark Splitup
    CO1=int(input("Enter 1st CO Splitup Mark :"))
    CO2=int(input("Enter 2nd CO Splitup Mark :"))
    CO3=int(input("Enter 3rd CO Splitup Mark :"))
    CO4=int(input("Enter 4th CO Splitup Mark :"))
    CO5=int(input("Enter 5th CO Splitup Mark :"))
    
    assname=input("Enter Assesment name :")
    subname=input("Enter Subject name :")
    fname=(assname+subname)+".csv"
    studentcount=len(ml)
    #To intialize the student number list,co1 mark list, co2 marklist
    stuco1ml=[]
    stuco2ml=[]
    stuco3ml=[]
    stuco4ml=[]
    stuco5ml=[]
    
    
    #Random Generator
    for i in range(studentcount):
        Flag=True
        total=ml[i]
        while Flag:
            a=random.randint(5,CO1)
            b=random.randint(5,CO2)
            c=random.randint(5,CO3)
            d=random.randint(5,CO4)
            e=random.randint(5,CO5)
            
            tt=a+b+c+d+e
            if tt==total:
                Flag=False
        stuco1ml.append(a)
        stuco2ml.append(b)
        stuco3ml.append(c)
        stuco4ml.append(d)
        stuco5ml.append(e)
    # Generated Random Values to store the output CSV file
    with open(fname, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["CO1 Mark", "CO2 Mark","CO3 Mark", "CO4 Mark","CO5 Mark","Total Mark"])
        for i in range(studentcount):
           writer.writerow([stuco1ml[i], stuco2ml[i],stuco3ml[i], stuco4ml[i],stuco5ml[i],ml[i]])


'''def threecocalc():
    #Intialize the Mark list as empty list
    ml=[]
    #To read the Mark List from inputm.csv file from stored Location
    with open('inputm.csv', newline='') as f:
        reader = csv.reader(f)
        totall=[list(map(int,rec)) for rec in csv.reader(f, delimiter=',')]
    
    #To update the Mark List from Readed CSV File
    for i in range(len(totall)):
        ml.append(totall[i]) 
    #Get CO1 and CO2 Mark Splitup
    CO1=int(input("Enter 1st CO Splitup Mark :"))
    CO2=int(input("Enter 2nd CO Splitup Mark :"))
    CO3=int(input("Enter 3rd CO Splitup Mark :"))
  
    
    assname=input("Enter Assesment name :")
    subname=input("Enter Subject name :")
    fname=(assname+subname)+".csv"
    studentcount=len(ml)
    #To intialize the student number list,co1 mark list, co2 marklist
    stuco1ml=[]
    stuco2ml=[]
    stuco3ml=[]
 
    
    
    #Random Generator
    for i in range(studentcount):
        Flag=True
        total=ml[i]
        while Flag:
            a=random.randint(5,CO1)
            b=random.randint(5,CO2)
            c=random.randint(5,CO3)
            
            
            tt=a+b+c
            if tt==total:
                Flag=False
        stuco1ml.append(a)
        stuco2ml.append(b)
        stuco3ml.append(c)
      
    # Generated Random Values to store the output CSV file
    with open(fname, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["CO1 Mark", "CO2 Mark","CO3 Mark","Total Mark"])
        for i in range(studentcount):
           writer.writerow([stuco1ml[i], stuco2ml[i],stuco3ml[i],ml[i]])'''