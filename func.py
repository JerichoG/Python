Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def myfunc(a, b):
	return a+b

>>> funcs = [myfunc]
>>> funcs[0]
<function myfunc at 0x03D9B3D8>
>>> funcs[0](2, 3)
5
>>> 
