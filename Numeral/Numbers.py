def Numeral(n):
    if(n == 0):
        pass
    else:
        print("Called!")
        Numeral(n-1)
    return Numeral

def Successor(n):
    return Numeral(n + 1)

def Plus(m,n):
    if n > 0:
        Plus(m,n-1)
    Successor(m)
    
print(Numeral(0))
print(Numeral(5))
print(Numeral(10))
print(Successor(10))
print(Plus(10,20))
