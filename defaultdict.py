word_count = defaultdict(int)
banned_words = set(banned)

#3). count the appearance of each word, excluding the banned words
for word in words:
    if word not in banned_words:
        word_count[word] += 1
