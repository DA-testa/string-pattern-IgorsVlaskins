def read_input():

    input_type = input().strip()
    if input_type == "F":
        with open("tests/1", "r") as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        pattern = input().strip()
        text = input().strip()

    # return both lines in one return
    return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):

    result = []
    p = 1000000007
    x = 263
    t_len = len(text)
    p_len = len(pattern)
    p_hash = sum(ord(pattern[i]) * pow(x, i, p) for i in range(p_len)) % p
    t_hash = sum(ord(text[i]) * pow(x, i, p) for i in range(p_len)) % p

    x_p = pow(x, p_len, p)
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if pattern == text[i:i+p_len]:
                result.append(i)
        if i < t_len - p_len:
            t_hash = (t_hash - ord(text[i]) * x_p) % p
            t_hash = (t_hash * x + ord(text[i+p_len])) % p
            t_hash = (t_hash + p) % p

    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

