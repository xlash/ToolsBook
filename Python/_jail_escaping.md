# Undefined
##	Types
	decimal
	float
	str

chr~(~({}<[])<<({}<[]))
del
exex
eval
file
has_attr
hex

unichr
ord

input
random
range
raw_input
set
super
type
xrange
[]<[]

## Exceptions undefined
Exception
StandardError
ZeroDivisionError
StopIteration
OverflowError
AssertionError
KeyboardInterrupt
ImportError
KeyError
NameError
UnboundLocalError
EnvironmentError
SyntaxError
IndentationError
RuntimeError
NotImplementedError

# Stripped out
``
''
""
\`
<
>
I believe _ is disallowed
# Unsure
__import__
	>> gives invalid syntax, and not builin function

#Allowed
print
dir
()
[]
{}
,
execfile
Exception
IOError
OSError
None
True
False
str.encode (but hasattr not defined)
str.decode (but hasattr not defined)
**function.func_code.co_filename**
print (0.0).hex()[3] ==> .
# Reserved Keywords
pass

# Invalid syntax
u'34'
r'34'
importlib


```python
print(shell.__str__())
print(shell.__repr__())


print(dir(shell.cat(shell.ls()[0])))
'__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__'
'''lways : invalid syntax (<string>, line 1)'''
print(shell.cat(shell.ls()[0].__class__))
print(shell.cat(shell.ls()[0].__delattr__))
print(shell.cat(shell.ls()[0].__doc__))
print(shell.cat(shell.ls()[0].__format__))
print(shell.cat(shell.ls()[0].__getattribute__))
print(shell.cat(shell.ls()[0].__hash__))
print(shell.cat(shell.ls()[0].__init__))
print(shell.cat(shell.ls()[0].__new__))
print(shell.cat(shell.ls()[0].__reduce__))
print(shell.cat(shell.ls()[0].__reduce_ex__))
print(shell.cat(shell.ls()[0].__repr__))
print(shell.cat(shell.ls()[0].__repr__()))
print(shell.cat(shell.ls()[0].__setattr__))
print(shell.cat(shell.ls()[0].__sizeof__))
print(shell.cat(shell.ls()[0].__str__))
print(shell.cat(shell.ls()[0].__subclasshook__))

# About tuples
print(dir((4,5))
>)
>
Executing sandbox
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
> '''always : invalid syntax (<string>, line 1)'''
print((4,5).__repr__())
print((4,5).__doc__)


print(shell.hint.__doc__)
print(shell.help.__doc__)
print(shell.ls.__doc__)
print(shell.cat.__doc__)

print(shell.hint().__doc__)
print(shell.help.__doc__)
print(shell.ls().__doc__)
print(shell.cat().__doc__)

print(dir(shell.help))
bound method shell.help of <__main__.shell instance at 0x7ffff7eb05f0>>

>print(shell.cat.im_class)	
>
Executing sandbox
__main__.shell


print(dir(shell.ls()))
==> Array
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print(dir(shell.cat()))
==> Exception
print(dir(shell.hint()))
print(dir(shell.help()))

print(Exception().type)


print(dir(Exception().message))
>
Executing sandbox
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

```
If I found a % I can do string formating with
myString % shell.cat.im_class
to get a .

A Backslash might let me do :
>>> # this example writes a string "ABC" using hex
>>> "\x41\x42\x43"
'ABC'

double underscore are not trimmed, since I have an invalid syntax for __builtins__

x=shell.ls.func_code
print x.co_code
>
Executing sandbox
dGHg}ytjt�}|GHWn�tk
r?dtGHnX|S
