TRUE = lambda x: lambda y: x;

FALSE lambda x: lambda y: y;

NOT = lambda b: b(FALSE)(TRUE);

AND lambda x: lambda y: x(y)(x);

OR lambda x: lambda y: x(x)(y);

# XOR = lambda x: lambda y:
