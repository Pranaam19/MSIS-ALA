C:\Users\MSIS>python
Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> def nap(x,y):
...     if x<10:
...         print("The no, is less than 10")
...     else:
...         g(x,y)
...
>>>
>>> nap(10,20)
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    nap(10,20)
    ~~~^^^^^^^
  File "<python-input-0>", line 5, in nap
    g(x,y)
    ^
NameError: name 'g' is not defined
>>> nap(9,20)
The no, is less than 10
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>> exit

C:\Users\MSIS>g++
'g++' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\MSIS>python
Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> def add(int x,int y):
  File "<python-input-0>", line 1
    def add(int x,int y):
                ^
>>> def ho_add(x):
...     return lambda y: x+y
...
>>> ho_add()
Traceback (most recent call last):
  File "<python-input-10>", line 1, in <module>
    ho_add()
    ~~~~~~^^
TypeError: ho_add() missing 1 required positional argument: 'x'
>>> ho_add
<function ho_add at 0x000002D36B979220>
>>> f = ho_add(100)
>>> f
<function ho_add.<locals>.<lambda> at 0x000002D36B979430>
>>> e=1000
>>> f =add(e)
Traceback (most recent call last):
  File "<python-input-15>", line 1, in <module>
    f =add(e)
TypeError: add() missing 1 required positional argument: 'y'
>>> f =add(100)
Traceback (most recent call last):
  File "<python-input-16>", line 1, in <module>
    f =add(100)
TypeError: add() missing 1 required positional argument: 'y'
>>> f =ho_add(e)
>>> f
<function ho_add.<locals>.<lambda> at 0x000002D36B979640>
>>> f(200)
1200
>>> def ho_add2(x):
...     def _add_(y):
...         return x+y
...     return _add
...
...
>>> ho_add2(10)
<function ho_add2.<locals>._add_ at 0x000002D36B979380>
>>> f2 =ho_add2(10)
>>> f2
<function ho_add2.<locals>._add_ at 0x000002D36B9797A0>
>>> def ho_add2(x):
...
...     _bias_ =-2
...     def _add_(y):
...         return x+y + _bias_
...     return _add_
...
>>> f20 =ho_add2(10)
>>> f20
<function ho_add2.<locals>._add_ at 0x000002D36B9796F0>
>>> print(f20)
<function ho_add2.<locals>._add_ at 0x000002D36B9796F0>
>>> f20(100)
108
>>> b=10
>>> assert a ==b
>>> l1 =[10,20,30]
>>> l2=[10,20,30]
>>> assert l1==l2
>>> a is b
True
>>> l1 is l2
False
>>> #"is" is a keyword  checks for identity 
>>> a=100
>>> a is b
False
>>> l1 ==l2
True
>>> l3 = l1
>>> # here l3 =l1 is a shallow copy
>>> l3 ==l2
True
>>> l3 ==l1
True
>>> l3 is l2
False
>>> l3 is  l1
True
>>> l3[2] = 100
>>> l3 ==l1
True
>>> l1 is l3
True
>>> l1
[10, 20, 100]

>>> class UpiId:
...     def __init__(self,id,bank_id):
...             self.my_id = id
...             self.my_bank_id = bank_id
...     def __repr__(self):
...             return "upi {"+self.my_id+"@"+self.my_bank_id+"}"
... 
>>> pran_upi_id = UpiId("9380554650","oksbi")
>>> print(pran_upi_id)
upi {9380554650@oksbi}
>>> somebody = pran_upi_id
>>> print(somebody)
upi {9380554650@oksbi}
>>> somebody is pran_upi_id
True
>>> somebody ==  pran_upi_id
True

>>> class UpiId:
...     def __init__(id,bank_id):
... 
KeyboardInterrupt
>>> class UpiId:
...     def __init__(self,id,bank_id):
...             self.my_id = id
...             sel.my_bank_id = bank_id
...     def __repr__(self):
...             return "upi "+self.my_id+"@"+self.my_bank_id
... 
>>> 
>>> pran_upi_id = UpiID("9380554650","oksbi")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'UpiID' is not defined. Did you mean: 'UpiId'?
>>> pran_upi_id = UpiId("9380554650","oksbi")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in __init__
NameError: name 'sel' is not defined. Did you mean: 'self'?
>>>     def __init__(self,id,bank_id):
  File "<stdin>", line 1
    def __init__(self,id,bank_id):
IndentationError: unexpected indent
>>> class UpiId:
...     def __init__(self,id,bank_id):
...             self.my_id = id
...             self.my_bank_id = bank_id
...     def __repr__(self):
...             return "upi {"+self.my_id+"@"+self.my_bank_id+"}"
... 
>>> pran_upi_id = UpiId("9380554650","oksbi")
>>> print(pran_upi_id)
upi {9380554650@oksbi}
>>> 
>>> somebody = pran_upi_id
>>> print(somebody)
upi {9380554650@oksbi}
>>> somebody is pran_upi_id
True
>>> somebody ==  pran_upi_id
True
>>> other_upi = UpiId("9380554650","oksbi")
>>> somebody = other_upi
>>> somebody == other_upi
True
>>> class Upi:
...     def __init__(self,id,bank_id):
...             self.id = id
...             self.bank_id = bank_id
...     def __repr__(Self):
...             return "upi {"+self.id+"@"+Self.bank_id+"}"
...     def __eq__(self,other):
...             return self.id ==other.id and self.bank_id == other.bank_id
... 
>>> pn = Upi("1234567","oksbi")
>>> pn
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in __repr__
NameError: name 'self' is not defined. Did you mean: 'Self'?
>>> print(pn)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in __repr__
NameError: name 'self' is not defined. Did you mean: 'Self'?
>>> class Upi:
...     def __init__(self,id,bank_id):
...             self.bank_id = bank_id
...             self.id = id
...     def __repr__(Self):
...             return "upi {"+self.id+"@"+self.bank_id+"}"
...     def __eq__(self,other):
...             return self.id ==other.id and self.bank_id == other.bank_id
... 
>>> pn = Upi("9798789","oksbi")
>>> pn
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in __repr__
NameError: name 'self' is not defined. Did you mean: 'Self'?
>>> 