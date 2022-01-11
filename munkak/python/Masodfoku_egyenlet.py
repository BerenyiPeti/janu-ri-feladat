import math
print("""
Egy másodfokú egyenlet gyökeit számolja ki, paraméterként kapott eredményekből. (ax2+bx+c=0)
""")
print("Kérem minden paraméterhez valós számot adjon meg!")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
d=b**2-(4*a*c)
if a==0:
    print("Hiba: a nem lehet egyenlő 0-val!")
elif d<0:
    print("Az egyenletnek nincs valós gyöke!")
elif d==0:
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print("Az egyenletnek 1 gyöke van:")
    print("x1=",x1)
elif d>0:
    x1 = ((-b) + (math.sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
    x2 = ((-b) - (math.sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
    print("Az egyenletnek 2 gyöke van:")
    print("x1=",x1,"x2=",x2)





