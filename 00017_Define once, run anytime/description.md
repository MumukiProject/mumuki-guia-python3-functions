Python gives us operations with which we can solve various tasks and also allows us to combine them, but the real power of programming is that we can also create our own operations.

And to this we'll then welcome _the functions_ :confetti_ball:! With our new friends, we can "teach" the computer to perform a task that wasn't originally included in the language. How to do that? By writing **only once** a definition like the following :one:...

```python
def is_longer_than(a_string, another_string):
  return len(a_string) > len(another_string)
```

...and then _calling_ - also known as _invoking_ - this function **as many times as we want** :1234::

```python
ムis_longer_than("Valle de Uco", "Cerro de los Siete Colores")
False
ムis_longer_than("Valle de Uco", "Cerro de los Siete Colores")
False # both times it returns the same thing
```

But wait, there is more! Every time we call it, we can do it with different _arguments_ :open_mouth::

```python
ムis_longer_than("Amazonas", "Tapón de Darién")
False
ムis_longer_than("Viña del Mar", "Iquitos")
True # if the arguments change, the result can be different too
```

> Let's see if it's understood:
>
> 1. 📋 Copy the _definition_ of the function 'is_longer_than' into the editor below;
> 2. 📢 Call the function `is_longer_than` in the `Console` several times with different arguments;
> 3. ▶ Then go back to the 'Solution' tab and press the 'Submit' button.
