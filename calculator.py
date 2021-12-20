print("1-ADD")
print("2-SUB")
print("3-MULTI")
print("4-DIVIDE")
a=int(input("ENTER A CHOICE:"))
b=int(input("enter num 1"))
c=int(input("enter num2"))
if a==1:
  print(b,'+',c,'=',(b+c))
elif a==2:
  print(b,'-',c,'=',(b-c))
elif a==3:
  print(b,'*',c,'=',(b*c))
elif a==4:
  print(b,'/',c,'/',(b/c))
else:
  print ("enter a valid choice")
