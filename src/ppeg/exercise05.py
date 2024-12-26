# Exercise #5: Fizz Buzz
"""Write a `fizz_buzz()` function with a single integer parameter named `up_to`. 
For the numbers 1 up to and including `up_to`, the function prints one of four 
things:
- Prints 'FizzBuzz' if the number is divisible by 3 and 5.
- Prints 'Fizz' if the number is only divisible by 3.
- Prints 'Buzz' if the number is only divisible by 5.
- Prints the number if the number is neither divisible by 3 nor 5.
Instead of printing each string or number on a separate line, print them 
without newlines. 
"""
from collections.abc import Iterator

def fizz_buzz(up_to: int) -> None:
    def _fizz_buzz_helper(up_to: int) -> Iterator['str']:
        for i in range(1, up_to + 1):
            if i % 15 == 0:
                yield 'FizzBuzz'
            elif i % 3 == 0:
                yield 'Fizz'
            elif i % 5 == 0:
                yield 'Buzz'
            else:
                yield str(i)
    
    fizz_buzz_txt = ' '.join(_fizz_buzz_helper(up_to))
    print(fizz_buzz_txt)


def run(n: str) -> None:
    fizz_buzz(int(n))