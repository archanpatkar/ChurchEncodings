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

print("Testing Numerals")
print(zero(NOT)(TRUE));
print(once(NOT)(TRUE));
print(twice(NOT)(TRUE));
print(thrice(NOT)(TRUE));

print("Testing Succesor")
print(succ(once)(NOT)(TRUE));
print(twice(NOT)(TRUE));

print("Testing Number Forms");
print(num(zero));
print(num(once));
print(num(twice));
print(num(thrice));

print("Testing Succesor on Numbers");
print(num(succ(zero)));
print(num(succ(once)));
print(num(succ(twice)));
print(num(succ(thrice)));

print("Testing Adding");
print(num(add(twice)(thrice)))

print("Testing Multiplication");
print(num(mult(thrice)(twice)));

print("Testing Power");
print(num(pow(thrice)(twice)))

print("Testing IS ZERO");
print(iszero(once))
print(iszero(zero))
