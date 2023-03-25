Exactly! All options are correct. :ok_hand:

A function can _declare_ as many parameters in its definition as it needs; for each of them, we must pass an argument when calling the function. The interesting thing is that inside the function definition, it doesn't matter which arguments we used; we will know them by the name of its parameter. In this example, when we type into the console...

```python
ムsum_lengths("learning", "programming")
```
...within the `sum_lengths` function the argument `"learning"` will be `a_string` and `"programming"` will be `another_string`:

```python
def sum_lengths(a_string, another_string):
  #               	▲       	▲
  #          	"learning" "programming"
  return len(a_string) + len(another_string)
  #        	    ▲              	▲
  # 	len("learning") len("programming")
```

However, if we invoke it by typing...

```python
ムsum_lengths("knowing", "Python")
```

... now the parameter `a_string` will have the value `"knowing"` and `another_string` will have the value `"Python"`.

That's why it's so important to give parameters a good name!