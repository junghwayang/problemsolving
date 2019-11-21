def organizingContainers(container):
    rowsum = [sum(c) for c in container]
    colsum = [0] * n
    for i in range(n):
        for c in container:
            colsum[i] += c[i]
    return 'Possible' if sorted(rowsum) == sorted(colsum) else 'Impossible'

# OR

def organizingContainers(container):
    rowsum = [sum(c) for c in container]
    colsum = [0] * n
    for i in range(n):
        colsum[i] = sum(map(lambda x: x[i], container))
    return 'Possible' if sorted(rowsum) == sorted(colsum) else 'Impossible'