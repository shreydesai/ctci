def zero_matrix(m):
    seen = init_matrix(len(m), len(m[0]))

    r, c = len(m), len(m[0])

    for i in range(r):
        for j in range(c):
            if m[i][j] == 0 and not seen[i][j]:
                seen[i][j] = True

                # reset rows
                for k in range(c):
                    m[i][k] = 0
                    seen[i][k] = True

                # reset columns
                for k in range(r):
                    m[k][j] = 0
                    seen[k][j] = True


def init_matrix(r, c):
    return [[False for x in range(c)] for y in range(r)]
