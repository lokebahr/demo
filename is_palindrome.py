
import re

def is_palindrome(s: str) -> bool:
    cleaned = re.sub(r"[^0-9a-zA-Z]+", "", s).lower()
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    print(is_palindrome("level"))                 
    print(is_palindrome("A man, a plan, a canal: Panama"))  
    print(is_palindrome("chatgpt"))              
