def angryProfessor(k, a):
    return 'YES' if sum(map(lambda x: x <= 0, a)) < k else 'NO'