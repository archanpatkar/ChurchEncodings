from BooleanEncoding import *
from Combinators import *

# zero is false
zero = lambda f: lambda a: a;

# like identity once removed
once = lambda f: lambda a: f(a);

twice = lambda f: lambda a: f(f(a));

thrice = lambda f: lambda a: f(f(f(a)));

succ = lambda n: lambda f: lambda a: f(n(f)(a));

num = lambda n: n(lambda x: x + 1)(0);

add = lambda n: lambda k: n(succ)(k);

mult = bluebird;

pow = thrush;

iszero = lambda n: n(kestral(FALSE))(TRUE);
