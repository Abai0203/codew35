# #1 Вы, вероятно, знакомы с системой «лайков» в Facebook и других социальных сетях. Люди могут «лайкать» записи в блогах, фотографии или другие материалы. Мы хотим создать текст, который должен отображаться рядом с такими элементами.

# Реализуйте функцию, которая принимает массив, содержащий имена людей, которым понравился товар. Она должна возвращать текст, отображаемый на экране, как показано в примерах:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Примечание: При наличии 4 и более имен число "and 2 others"просто увеличивается.

def likes(names):
    n = len(names)
    if n == 0:
        return "no one likes this"
    if n == 1:
        return f"{names[0]} likes this"
    if n == 2:
        return f"{names[0]} and {names[1]} like this"
    if n == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    return f"{names[0]}, {names[1]} and {n - 2} others like this"


# #2 Тролли атакуют ваш раздел комментариев!
# Распространенный способ решения этой проблемы — удалить все гласные буквы из комментариев троллей, тем самым нейтрализовав угрозу.
# Ваша задача — написать функцию, которая принимает строку и возвращает новую строку, из которой удалены все гласные.
# Например, строка "This website is for losers LOL!" превратится в "Ths wbst s fr lsrs LL!".
# Примечание: в данном случае слово «ката» yне считается гласной буквой.

def disemvowel(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result

# 3 

def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 == 1:
            return i


print(find_it([7]))
print(find_it([0]))
print(find_it([1, 1, 2]))
print(find_it([0, 1, 0, 1, 0]))
print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))


# 4 


def find_outlier(integers):
    if sum(i % 2 for i in integers[:3]) > 1:
        for i in integers:
            if i % 2 == 0:
                return i
            
    else:
        for i in integers:
            if i % 2 != 0:
                return i
            
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))


# 5

def get_middle(s):
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid - 1:mid + 1]
    else:
        return s[mid]

# 6

def find_uniq(xs):
    a, b, c = xs[0], xs[1], xs[2]
    common = a if a == b or a == c else b
    for x in xs:
        if x != common:
            return x

# 7 

def is_pangram(st):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in st.lower():
            return False
    return True

# 8

def find_missing_letter(chars):
    for a, b in zip(chars, chars[1:]):
        if ord(b) - ord(a) > 1:
            return chr(ord(a) + 1)

#9 

def create_phone_number(n):
    #your code here
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# 10

def high(x):
    words = x.split()
    return max(words, key=lambda w: sum(ord(c) - ord('a') + 1 for c in w))
