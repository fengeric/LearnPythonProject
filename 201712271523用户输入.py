def reverse(text):
    return text[::-1]

def is_palindrome(text):#回文：文字是否正读和倒读都一样
    return text == reverse(text)

text = input('Enter input:')

if is_palindrome(text):
    print("yes")
else:
    print('no')
