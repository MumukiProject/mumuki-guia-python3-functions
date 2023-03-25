Good! The parameters are simply identifiers, which are written without quotes and can be used to receive arguments of any type. Therefore this function can be written as follows:

```python
def is_library(place)
  return "library" in place
```

On the other hand, the original definition…

```python
def is_library("place"):
   return "library" in "place"
```

…will throw a `SyntaxError`!
