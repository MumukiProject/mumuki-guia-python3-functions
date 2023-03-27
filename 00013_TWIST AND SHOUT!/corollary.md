:clap: :smiley: :gem: :crown: Marvelous! 

If you are wondering, since the exclamation mark has no uppercase or lowercase variant, you could just as well concatenate the result of `str.upper`...

```python
def shout(text):
  return str.upper(text) + "!"  
```

...or convert to uppercase the result of `+`:

```python
def shout(text):
  return str.upper(text + "!")   
```
