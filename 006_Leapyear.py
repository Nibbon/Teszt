def is_leap(year):
    leap=False
    if year%4==0 and (year%100!=0 or year%400==0):
        leap=True
    return leap

while True:
    year=int(input())
    print (is_leap(year))

#teszter
"""i=1950
while i<=2010:
    print (i)
    print (is_leap(i))
    i=i+1"""
