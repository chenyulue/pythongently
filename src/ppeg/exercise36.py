# Exercise #36: Reverse String
"""Write a `reverse_string()` function with a `text` parameter. The function should return a string with all of text's characters in reverse order. For example, `reverse_string('Hello')` returns 'olleH'. The function should not alter the casing of any letters. And, if text is a blank string, the function returns a blank string."""


def reverse_string(text: str) -> str:
    texts = list(text)
    length = len(text)

    for i in range(len(text) // 2):
        texts[i], texts[length - i - 1] = texts[length - i - 1], texts[i]

    return "".join(texts)


def run(txt: str) -> None:
    print("Reversed string:", reverse_string(txt))
