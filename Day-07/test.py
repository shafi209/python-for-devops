import sys 

type = sys.argv[1]

if type ==("t2.micro"):
   print ("this will charge you 2$ per day ")
elif type==("t2.medium"):
  print("this will charge you 4 per day")

else:
    print("please provide corect input")

