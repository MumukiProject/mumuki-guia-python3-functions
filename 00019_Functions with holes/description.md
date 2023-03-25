You've probably noticed that the functions we've defined so far can return both numbers and booleans. And more: **it can return any type of data** :exploding_head:. But what about what _enters_ into the function? How many arguments can we pass to it? And what exactly are the parameters?

The answer is that the parameters are _...drum roll :drum:..._ little holes! :face_with_raised_eyebrow:

For example, in this definition we are _declaring_ **a single** parameter named `a_number`...

```python
def half(a_number): # a_number is a parameter
  return a_number / 2
```

...so that `half` can receive exactly **one** argument:

```python
ムhalf(4) # 4 is an argument
2
```

For example, when we call `half` with the argument `4`, through this "small hole" called `a_number` it will receive the value `4`, which our function can then divide by two and return its result. On the other hand, if we invoke it like this...


```python
ムhalf(10) # 10 is another argument
5
```

...through the parameter `a_number`, the number `10` we used when invoking the function will reach `half`. And again, it will divide it by two and return the `5`.

> Slow down! Let's go back to the function from the previous exercise...
>
> ```python
> def sum_lengths(a_string, another_string):
>   return len(a_string) + len(another_string)
> ```
>
> ... and mark the correct options.