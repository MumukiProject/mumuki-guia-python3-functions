But is it possible to combine these functions as we did with the operators and functions already included in Python? Of course! :heart_eyes: In other words, _we can call any function inside a definition_. For example:

```python
def double(number):
  return 2 * number

def successor_of_double(number):
  return double(number) + 1
```

Or even better:

```python
def double(number):
  return 2 * number

def successor(number):
  return number + 1

def successor_of_double(number):
  return next(double(number))
```

> Let's see if it's clear. Define the following functions:
>
> * `previous`: takes a number and returns that number minus one.
> * `triple`: returns triple a number.
> * `prev_of_triple`, which combines the two functions above: multiplies a number by 3 and subtracts 1 from it.
>