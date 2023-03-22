As we saw, a string can be passed as an argument to a function...

```python
ムis_library("Library Of Babel")
True
ムis_library("Library Of Congress")
True
ムis_library("Colón Theatre")
False
```

...and also, functions can have parameters, one for each argument it needs to receive.

> Wait! Will we have to write differently our parameters when they are of type string? :thinking:
>
> For example, look at the following definition of `is_library`...
>
> ```python
> def is_library("place"):
>   return "library" in "place"
> ```
> ...is it well written? :eyes: