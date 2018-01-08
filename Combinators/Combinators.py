from BooleanEncoding import *

identity = lambda a: a;

kestral = lambda x: lambda y: x;

kite = lambda x: lambda y: y;

mockingbird = lambda f: f(f);

cardinal = lambda f: lambda a: lambda b: f(b)(a);

# function composition B-Combinator
bluebird = lambda f: lambda g: lambda x: f(g(x));

# T-Combinator
thrush = lambda a: lambda f: f(a);

vireo = lambda x: lambda y: lambda f: f(x)(y);

blackbird = lambda f: lambda g: lambda a: lambda b: f(g(a)(b))

print(bluebird(NOT)(NOT)(FALSE));
