num = int(input())
while num<=1 or num>=100:
    print ("Nem ám pamutzoknyi!")
    num = int(input())
    continue    
if (num%2==1) or (num%2==0 and 6<= num<=20):
    print ("Weird")
elif num%2==0 and (2<=num<=5 or num>20):
    print ("Not Weird")
