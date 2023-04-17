import numpy as np

def read_input():
    choice = input().rstrip()
    if choice == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif choice == 'F':
        with open("tests/1", "r") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    print(" ".join(map(str, output)))

def poly_hash(s, prime, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % prime
    return ans

def precompute_hashes(text, len_pattern, prime, x):
    len_text = len(text)
    H = np.zeros(len_text - len_pattern + 1, dtype=np.int64)
    S = text[len_text - len_pattern:]
    H[len_text - len_pattern] = poly_hash(S, prime, x)
    y = 1
    for i in range(len_pattern):
        y = (y * x) % prime
    for i in range(len_text - len_pattern - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + len_pattern])) % prime
    return H

def get_occurrences(pattern, text):
    prime = 1000000007
    x = np.random.randint(1, prime)
    len_pattern = len(pattern)
    len_text = len(text)
    pattern_hash = poly_hash(pattern, prime, x)
    H = precompute_hashes(text, len_pattern, prime, x)
    return [i for i in range(len_text - len_pattern + 1) if pattern_hash == H[i]]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
