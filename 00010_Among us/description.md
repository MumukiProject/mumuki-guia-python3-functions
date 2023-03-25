Let's do a quick review of booleans before we continue!

* You can do the logical conjunction between two booleans (_logical and_), using the `and` operator. For example: `it_is_raining and it_is_hot`
* You can do the logical disjunction between two booleans (_logical or_), by means of the `or` operator. For example: `is_summer or is_spring`

And in addition to these two operators, we have a third: the negation operator `not`, which converts `True` to `False` and vice versa:

```python
ムnot True
False
ムnot False
True
```

> Let's practice! :muscle: Define the following functions:
>
> * `is_between`, which takes three numbers and says if the first is greater than the second and less than the third.
> * `is_out_of_range`: take three numbers and say if the first is less than the second or greater than the third
>
> ```python
> ムis_between(3, 1, 10)
> True
> ムis_between(90, 1, 10)
> False
> ムis_between(10, 1, 10)
> False
> ムis_out_of_range(17, 1, 10)
> True
> ```
>