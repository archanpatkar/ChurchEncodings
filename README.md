# ChurchEncodings 
### Church encoding is a means of modeling data and operators using lambda abstractions.
### Python implementation of Lambda Calculus

## Illustration

### Code
``` python
# Representing true as a function
def TRUE(x):
  return lambda y: x

# Representing false as a function
def FALSE(x):
  return lambda y: y

# Representing ! (Not) operator as a function
def NOT(b):
  return b(FALSE)(TRUE)

print(NOT(TRUE))
print(NOT(FALSE))
```

### Output

``` python
<function FALSE at 0x1040bce18>
<function TRUE at 0x10432d0d0>
```
