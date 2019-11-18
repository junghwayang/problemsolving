def acmTeam(topic):
    maxtopic, maxteam = 0, 1
    for i in range(n):
        for j in range(i+1, n):
            know = 0
            for x in range(m):
                if topic[i][x] == '1' or topic[j][x] == '1':
                    know += 1
            if know > maxtopic:
                maxtopic = know
                maxteam = 1
            elif know > 0 and know == maxtopic:
                maxteam += 1
    return maxtopic, maxteam