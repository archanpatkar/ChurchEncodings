from Combinators import *
from Numerals import *

pair = vireo;

first = lambda p: p(kestral);

second = lambda p: p(kite);

phi = lambda p: pair(second(p))(succ(second(p)));

pred = lambda n: first(n(phi)(pair(zero)(zero)));

sub = lambda n: lambda k: k(pred)(n);

leq = lambda n: lambda k: iszero(sub(n)(k));

eq = lambda n: lambda k: AND(leq(n)(k))(leq(k)(n));

geq = lambda n: lambda k: blackbird(NOT)(leq)(n)(k);

p1 = pair(zero)(zero);

print(num(first(p1)));

print(num(second(p1)));

p2 = phi(p1);

print(num(first(p2)));

print(num(second(p2)));

print(num(pred(thrice)));

print(num(sub(thrice)(twice)));

print(leq(twice)(thrice));

print(eq(twice)(twice));

print(eq(zero)(twice));

print(geq(thrice)(twice));
