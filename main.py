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