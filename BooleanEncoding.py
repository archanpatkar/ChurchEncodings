def TRUE(x):
    return lambda y: x;

def FALSE(x):
    return lambda y: y;

def NOT(b):
    return b(FALSE)(TRUE);

def AND(x):
    return lambda y: x(y)(x);

def OR(x):
    return lambda y: x(x)(y);
