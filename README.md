# ChurchEncodings 
### Church Encoding is a means of modeling data and operators using lambda abstractions in Lambda Calculus.
### Implementated in Python

## Illustration

### Code
``` python
# Representing true as a function
TRUE = lambda x: lambda y: x

# Representing false as a function
FALSE = lambda x: lambda y: y

# Representing ! (Not) operator as a function
NOT = lambda  b: b(FALSE)(TRUE)

print(NOT(TRUE))
print(NOT(FALSE))
```

### Output

``` python
<function FALSE at 0x1040bce18>
<function TRUE at 0x10432d0d0>
```
