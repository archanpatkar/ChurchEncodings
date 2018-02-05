# ChurchEncodings 
### Church encoding is a means of modeling data and operators using lambda abstractions.
### Python implementation of Lambda Calculus

## Illustration

### Code
``` python
# Representing true as a lambda
def TRUE(x):
  return lambda y: x

# Representing false as a lambda
def FALSE(x):
  return lambda y: y

# Representing ! (Not) operator as a lambda
NOT = lambda b: b(FALSE)(TRUE)

print(NOT(TRUE))
print(NOT(FALSE))
```

### Output

``` python
<function FALSE at 0x1040bce18>
<function TRUE at 0x10432d0d0>
```
