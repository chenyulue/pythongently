# Exercise #10: Find And Replace
"""Write a `find_and_replace()` function that has three parameters: `text` is the 
string with text to be replaced, `old_text` is the text to be replaced, and 
`new_text` is the replacement text. Keep in mind that this function must be 
case-sensitive: if you are replacing 'dog' with 'fox', then the 'DOG' in 'MY DOG 
JONESY' won't be replaced. 

This exercise is aimed to reimplement the `replace()` strin method for practice, 
only using slices, indexes, `len()`, and augmented assignment operator.
"""

def find_and_replace(text: str, old_text: str, new_text: str) -> str:
    replaced_text: list[str] = []
    
    pre, i = 0, 0
    while i < len(text):
        if text[i : i+len(old_text)] == old_text:
            replaced_text.append(text[pre : i])
            replaced_text.append(new_text)
            i += len(old_text)
            pre = i
        else:
            i += 1
    replaced_text.append(text[pre : i])
    
    return ''.join(replaced_text)

def run(text: str, old_text: str, new_text: str) -> None:
    print("Replaced text:", find_and_replace(text, old_text, new_text))