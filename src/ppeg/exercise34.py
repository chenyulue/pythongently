# Exercise #34: Uppercase Letters
"""Write a `get_uppercase()` function with a `text` string parameter. The function returns a string with all lowercase letters in text converted to uppercase. Any non-letter characters in text remain as they are. For example, 'Hello' causes `get_uppercase()` to return 'HELLO' but 'goodbye 123!' returns 'GOODBYE 123!'.
"""

def to_upper(letter: str) -> str:
    diff = ord('a') - ord('A')
    if ord('a') <= ord(letter) <= ord('z'):
        return chr(ord(letter) - diff)
    return letter

def get_uppercase(text: str) -> str:
    return ''.join(map(to_upper, text))


def run(text: str) -> None:
    print(get_uppercase(text))