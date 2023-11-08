def solution(skill, skill_trees):
    count = 0
    for skill_tree in skill_trees:
        s = ''
        for ele in skill_tree:
            if ele in skill:
                s += ele
        if skill[:len(s)] == s:
            count += 1
    return count