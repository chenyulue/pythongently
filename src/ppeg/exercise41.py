# Exercise #41: Rot 13 Encryption
"""Write a `rot13()` function with a `text` parameter that returns the ROT 13 encrypted version of text. Uppercase letters encrypt to uppercase letters and lowercase letters encrypt to lowercase letters. For example, 'HELLO, world!' encrypts to 'URYYB, jbeyq!' and 'hello, WORLD!' encrypts to 'uryyb, JBEYQ!'.

You may use the following Python functions and string methods as part of your solution: ord(), chr(), isalpha(), islower(), and isupper().
"""


def rot13(text: str) -> str:
    def cipher_letter(letter: str) -> str:
        if letter.isalpha():
            if letter.islower():
                return chr((ord(letter) - ord("a") + 13) % 26 + ord("a"))
            else:
                return chr((ord(letter) - ord("A") + 13) % 26 + ord("A"))
        else:
            return letter

    return "".join(map(cipher_letter, text))

def run(text: str) -> None:
    print(rot13(text))
