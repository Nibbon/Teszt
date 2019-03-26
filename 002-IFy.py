num = int(input())
if num>=100 or num<=1:
    print ("Nem ám pamutzoknyi!")
elif (num%2==1) or (num%2==0 and 6<= num<=20):
    print ("weird")
elif num%2==0 and (2<=num<=5 or num>20):
    print ("Not weird")
