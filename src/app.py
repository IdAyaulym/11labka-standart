def is_palindrome(s: str) -> bool:
    s2 = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s2 == s2[::-1]

def sum_numbers(nums):
    return sum(nums)

if __name__ == "__main__":
    print("Пример: is_palindrome('А роза упала на лапу Азора') ->", is_palindrome("А роза упала на лапу Азора"))
    print("Пример: sum_numbers([1,2,3]) ->", sum_numbers([1,2,3]))
