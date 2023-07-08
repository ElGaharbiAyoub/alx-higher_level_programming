>>> add_integer = __import__("0-add_integer").add_integer
>>> print(add_integer(1, 2))
3
>>> print(add_integer(100, -2))
98
>>> print(add_integer(2))
100
>>> print(add_integer(100.3, -2))
98
>>> try:
... 	print(add_integer(4, "School"))
... except Exception as e:
... 	print(e)
b must be an integer
>>> try:
... 	print(add_integer(None))
... except Exception as e:
... 	print(e)
a must be an integer
>>> add_integer(2.45, 3.1)
5
>>> add_integer(1, float('nan'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 9, in add_integer
ValueError: cannot convert float NaN to integer
>>> add_integer(1, float('inf'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 9, in add_integer
OverflowError: cannot convert float infinity to integer
>>> add_integer(999999999999999999999999999999, 1)
1000000000000000000000000000000
>>> add_integer([1], 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in add_integer
TypeError: a must be an integer
>>> add_integer(3, "2")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in add_integer
TypeError: b must be an integer
>>> add_integer()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add_integer() missing 1 required positional argument: 'a'
>>> add_integer(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add_integer() takes from 1 to 2 positional arguments but 3 were given
