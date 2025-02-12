t = int(input())

for _ in range(t):
    W = input().strip()
    w_sliced = W[:-2]
    transcribe_word = w_sliced + "i"
    print(transcribe_word)


