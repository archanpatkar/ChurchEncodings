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
