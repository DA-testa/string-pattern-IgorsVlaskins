def read_input():
    input_type = input()
    if "I" in input_type or "i" in input_type:
        pattern = input().rstrip()
        text = input().rstrip()
    elif "F" in input_type or "f" in input_type:
        file = "06"
        if "a" not in file:
            with open("tests/" + file, 'r')as f:
                pattern = f.readline().rstrip()
                text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    prime = 1
    pattern_len, text_len = len(pattern), len(text)
    pattern_hash = sum(ord(pattern[i]) * pow(prime, i) for i in range(pattern_len))
    text_hash = sum(ord(text[i]) * pow(prime, i) for i in range(pattern_len))
    occurrences = []
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+pattern_len]:
                occurrences.append(i)
        if i < text_len - pattern_len:
            text_hash = (text_hash - ord(text[i])) / prime + ord(text[i+pattern_len]) * pow(prime, pattern_len-1)
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
