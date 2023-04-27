def pascal(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        new_line = [1]
        last_line = pascal(n - 1)
        for i in range(len(last_line) - 1):
            new_line.append(last_line[i] + last_line[i + 1])
        new_line.append(1)
    return new_line


print(pascal(8))
