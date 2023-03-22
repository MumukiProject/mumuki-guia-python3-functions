Now let's look at the definition of another function...

```python
def is_question(sentence):
  return str.endswith(sentence, "?")
```

...which we can use like this:

```python
ムis_question("What time is it?")
True
ムis_question("In this house we obey the laws of thermodynamics!")
False
```

Does the definition of this function look like the one above? Why?

> :mag: Compare this new definition with the one we saw before...
>
> ```python
> def is_longer_than(a_string, another_string):
> return len(a_string) > len(another_string)
> ```
>
> ...and answer what they have in common.



...la cual podemos usar así: 

```python
ム es_pregunta("¿Qué hora es?")
True
ム es_pregunta("¡En esta casa obedecemos las leyes de la termodinámica!")
False
```

¿Se parece la definición de esta función a la anterior? ¿Por qué será?

> :mag: Compará esta nueva definición con la que vimos anteriormente...
>
> ```python
> def es_mas_largo_que(un_string, otro_string):
>   return len(un_string) > len(otro_string)
> ```
>
> ...y respondé qué tienen en común.
