# Math函数

- `math.ceil`(*x*) 【向上取整】

  Return the ceiling of *x*, the smallest integer greater than or equal to *x*. If *x* is not a float, delegates to `x.__ceil__()`, which should return an [`Integral`](mk:@MSITStore:E:\summer\Doc\Python372.chm::/library/numbers.html#numbers.Integral) value

  ```
  >>> math.ceil(5)
  5
  ```

- `math.copysign`(*x*, *y*)

  Return a float with the magnitude (absolute value) of *x* but the sign of *y*.  On platforms that support signed zeros, `copysign(1.0, -0.0)` returns *-1.0*.

  返回一个浮点数，绝对值是x，符号为y，在支持带符号零的平台上，`copsign（1.0,-0.0）`返回-1.0

  ```
  >>> math.copysign(3.4,-0)
  3.4
  >>> math.copysign(3.4,-0.0)
  -3.4
  >>> math.copysign(3.4,-1)
  -3.4
  >>> math.copysign(3.4,1)
  3.4
  ```

  这里-0表示正数，-0.0表示复数

- `math.fabs`(*x*)

  Return the absolute value of *x*.

  返回关于x的绝对值小数

  ```
  >>> math.fabs(-1241)
  1241.0
  ```

  python自己有abs绝对值，返回的是整数

  ```
  >>> abs(-1241)
  1241
  ```

- `math.factorial`(*x*)

  Return *x* factorial.  Raises [`ValueError`](mk:@MSITStore:E:\summer\Doc\Python372.chm::/library/exceptions.html#ValueError) if *x* is not integral or is negative.

  返回关于x的阶乘，如果x不是整数或者是复数，则引发valueerror错误

  ```
  >>> math.factorial(5)
  120
  >>> math.factorial(1)
  1
  >>> math.factorial(2)
  2
  >>> math.factorial(3)
  6
  >>> math.factorial(4)
  24
  ```

- `math.floor`(*x*)【向下取整】

  Return the floor of *x*, the largest integer less than or equal to *x*. If *x* is not a float, delegates to `x.__floor__()`, which should return an [`Integral`](mk:@MSITStore:E:\summer\Doc\Python372.chm::/library/numbers.html#numbers.Integral) value.

  ```
  >>> math.floor(2.51512)
  2
  >>> math.floor(0.2)
  0
  >>> math.floor(3.999999)
  3
  >>> math.floor(3)
  3
  类似于python自带的int函数
  >>> int(3.9)
  3
  ```

- `math.fmod`(*x*, *y*)

  Return `fmod(x, y)`, as defined by the platform C library. Note that the Python expression `x % y` may not return the same result.  The intent of the C standard is that `fmod(x, y)` be exactly (mathematically; to infinite precision) equal to `x - n*y` for some integer *n* such that the result has the same sign as *x* and magnitude less than `abs(y)`.  Python’s `x % y` returns a result with the sign of *y* instead, and may not be exactly computable for float arguments. For example, `fmod(-1e-100, 1e100)` is `-1e-100`, but the result of Python’s `-1e-100 % 1e100` is `1e100-1e-100`, which cannot be represented exactly as a float, and rounds to the surprising `1e100`.  For this reason, function [`fmod()`](mk:@MSITStore:E:\summer\Doc\Python372.chm::/library/math.html#math.fmod) is generally preferred when working with floats, while Python’s `x % y` is preferred when working with integers.

  返回x%y的取余值，并且带一位小数

  ```
  >>> 5%3
  2
  >>> math.fmod(5.5,3)
  2.5
  ```

- `math.frexp`(*x*)

  Return the mantissa and exponent of *x* as the pair `(m, e)`.  *m* is a float and *e* is an integer such that `x == m * 2**e` exactly. If *x* is zero, returns `(0.0, 0)`, otherwise `0.5 <= abs(m) < 1`.  This is used to “pick apart” the internal representation of a float in a portable way.

  ```
  >>> 0.625*2**3
  5.0
  >>> math.frexp(5)
  (0.625, 3)
  ```

- `math.fsum`(*iterable*)

  Return an accurate floating point sum of values in the iterable.  Avoids loss of precision by tracking multiple intermediate partial sums:`>>> sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]) 0.9999999999999999 >>> fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]) 1.0 `The algorithm’s accuracy depends on IEEE-754 arithmetic guarantees and the typical case where the rounding mode is half-even.  On some non-Windows builds, the underlying C library uses extended precision addition and may occasionally double-round an intermediate sum causing it to be off in its least significant bit.For further discussion and two alternative approaches, see the [ASPN cookbook recipes for accurate floating point summation](https://code.activestate.com/recipes/393090/).

  列表小数求和总所周知，python里的小数进行加减所得到的值未必是自己想要的，有时候使用sum求和一个列表里的所有小数得到的值也可能是错误的，因此出现了fsum，用来进行小数的求和

  ```
  >>> sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]) 0.9999999999999999 
  >>> fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
  1.0
  >>> sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1,.1])
  1.0999999999999999
  >>> math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1,.1])
  1.1
  ```

- `math.gcd`(*a*, *b*)

  Return the greatest common divisor of the integers *a* and *b*.  If either *a* or *b* is nonzero, then the value of `gcd(a, b)` is the largest positive integer that divides both *a* and *b*.  `gcd(0, 0)` returns `0`.New in version 3.5.

  返回最小公约数

  ```
  >>> math.gcd(50,25)
  25
  ```

- `math.isclose`(*a*, *b*, ***, *rel_tol=1e-09*, *abs_tol=0.0*)

  Return `True` if the values *a* and *b* are close to each other and `False` otherwise.Whether or not two values are considered close is determined according to given absolute and relative tolerances.*rel_tol* is the relative tolerance – it is the maximum allowed difference between *a* and *b*, relative to the larger absolute value of *a* or *b*. For example, to set a tolerance of 5%, pass `rel_tol=0.05`.  The default tolerance is `1e-09`, which assures that the two values are the same within about 9 decimal digits.  *rel_tol* must be greater than zero.*abs_tol* is the minimum absolute tolerance – useful for comparisons near zero. *abs_tol* must be at least zero.If no errors occur, the result will be: `abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)`.The IEEE 754 special values of `NaN`, `inf`, and `-inf` will be handled according to IEEE rules.  Specifically, `NaN` is not considered close to any other value, including `NaN`.  `inf` and `-inf` are only considered close to themselves.New in version 3.5.See also [**PEP 485**](https://www.python.org/dev/peps/pep-0485) – A function for testing approximate equality 

  返回a与b的值是否接近，如果接近，则返回true，如果不接近则返回True，后面的rel_tol是允许a与b之间的最大的差别指数，默认为小数点后9位，如果想把这个值提高，可以传入一个大于0的参数。

  ```
  >>> math.isclose(0.3,0.1+0.2)
  True
  >>> 0.1+0.2
  0.30000000000000004
  >>> math.isclose(0.33333,0.333333,rel_tol=0.000001)
  False
  >>> math.isclose(0.33333,0.333333,rel_tol=0.00001)
  True
  ```

- `math.isfinite`(*x*)

  Return `True` if *x* is neither an infinity nor a NaN, and `False` otherwise.  (Note that `0.0` *is* considered finite.)New in version 3.2.

- `math.isinf`(*x*)

  Return `True` if *x* is a positive or negative infinity, and `False` otherwise.

- `math.isnan`(*x*)

  Return `True` if *x* is a NaN (not a number), and `False` otherwise.

- `math.ldexp`(*x*, *i*)

  Return `x * (2**i)`.  This is essentially the inverse of function [`frexp()`](mk:@MSITStore:E:\summer\Doc\Python372.chm::/library/math.html#math.frexp).

- `math.modf`(*x*)

  Return the fractional and integer parts of *x*.  Both results carry the sign of *x* and are floats.

  返回x的小数部分与整数部分，并且都带一位小数

  ```
  >>> math.modf(5)
  (0.0, 5.0)
  >>> math.modf(3.4)
  (0.3999999999999999, 3.0)
  >>> math.modf(3.7)
  (0.7000000000000002, 3.0)
  ```

- `math.remainder`(*x*, *y*)

  Return the IEEE 754-style remainder of *x* with respect to *y*.  For finite *x* and finite nonzero *y*, this is the difference `x - n*y`, where `n` is the closest integer to the exact value of the quotient `x / y`.  If `x / y` is exactly halfway between two consecutive integers, the nearest *even* integer is used for `n`.  The remainder `r = remainder(x, y)` thus always satisfies `abs(r) <= 0.5 * abs(y)`.Special cases follow IEEE 754: in particular, `remainder(x, math.inf)` is *x* for any finite *x*, and `remainder(x, 0)` and `remainder(math.inf, x)` raise [`ValueError`](mk:@MSITStore:E:\summer\Doc\Python372.chm::/library/exceptions.html#ValueError) for any non-NaN *x*. If the result of the remainder operation is zero, that zero will have the same sign as *x*.On platforms using IEEE 754 binary floating-point, the result of this operation is always exactly representable: no rounding error is introduced.New in version 3.7.

  返回x%y的值，并且带一位小数

  ```
  >>> math.remainder(1,2)
  1.0
  >>> math.remainder(4,2)
  0.0
  >>> math.remainder(9,4)
  1.0
  ```

- `math.trunc`(*x*)

  Return the [`Real`](mk:@MSITStore:E:\summer\Doc\Python372.chm::/library/numbers.html#numbers.Real) value *x* truncated to an [`Integral`](mk:@MSITStore:E:\summer\Doc\Python372.chm::/library/numbers.html#numbers.Integral) (usually an integer). Delegates to [`x.__trunc__()`](mk:@MSITStore:E:\summer\Doc\Python372.chm::/reference/datamodel.html#object.__trunc__).
  
  返回x的整数部分，且整数部分为int型
  
  ```
  >>> math.trunc(10.5)
  10
  >>> math.trunc(12.5555555555)
  12
  >>> math.trunc(10)
  10
  ```

Note that [`frexp()`](mk:@MSITStore:E:\summer\Doc\Python372.chm::/library/math.html#math.frexp) and [`modf()`](mk:@MSITStore:E:\summer\Doc\Python372.chm::/library/math.html#math.modf) have a different call/return pattern than their C equivalents: they take a single argument and return a pair of values, rather than returning their second return value through an ‘output parameter’ (there is no such thing in Python).

For the [`ceil()`](mk:@MSITStore:E:\summer\Doc\Python372.chm::/library/math.html#math.ceil), [`floor()`](mk:@MSITStore:E:\summer\Doc\Python372.chm::/library/math.html#math.floor), and [`modf()`](mk:@MSITStore:E:\summer\Doc\Python372.chm::/library/math.html#math.modf) functions, note that *all* floating-point numbers of sufficiently large magnitude are exact integers. Python floats typically carry no more than 53 bits of precision (the same as the platform C double type), in which case any float *x* with `abs(x) >= 2**52` necessarily has no fractional bits.