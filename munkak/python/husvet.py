print("""A program kérjen be egy évszámot a felhasználótól! 
Ha ez 1900 és 2099 közé esik, akkor a program írja ki, hogy az adott évben melyik napra esik húsvét vasárnap! 
A kiszámítás algoritmusát megtalálja a Wikipedia-ban Gauss módszer néven.
""")
K=int(input("""Adja meg szám segítségével mely évek között szeretné kiszámolni húsvét vasárnapját!
1: 1583-1699
2: 1700-1799
3: 1800-1899
4: 1900-2099
5: 2100-2199
6: 2200-2299"""))

if K==1:
    Y=int(input("Adja meg az év számát 1583 és 1699 között!"))
    M = 22
    N = 2
elif K==2:
    Y=int(input("Adja meg az év számát 1700 és 1799 között!"))
    M = 23
    N = 3
elif K==3:
    Y=int(input("Adja meg az év számát 1800 és 1899 között!"))
    M = 23
    N = 4
elif K==4:
    Y=int(input("Adja meg az év számát 1990 és 2099 között!"))
    M = 24
    N = 5
elif K==5:
    Y=int(input("Adja meg az év számát 2100 és 2199 között!"))
    M = 24
    N = 6
else:
    Y=int(input("Adja meg az év számát 2200 és 2299 között!"))
    M = 25
    N = 0

#változók
a=Y%19
b=Y%4
c=Y%7
d=(19*a+M)%30
e=(2*b+4*c++6*d+N)%7

if (d+e)<10:
    print(Y,"húsvét vasárnapja március",d+e+22,".-ére/ára esik")
elif (d+e-9)==26:
    print(Y,"húsvét vasárnapja április 19.-ére esik.")
elif (d+e-9)==25 and d==28 and e==6 and a>10:
    print(Y,"húsvét vasárnapja április 18.-ára esik.")
else:
    print(Y,"húsvét vasárnapja április",d+e-9,".-ére/ára esik.")









