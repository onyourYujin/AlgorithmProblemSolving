def solution(s):
    words = s.split(" ")
    new_word = []
    for word in words:
        new_word.append(word.capitalize())
    return ' '.join(new_word)