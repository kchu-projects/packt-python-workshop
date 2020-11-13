import urllib.request
import collections


url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
response = urllib.request.urlopen(url)
words = response.read().decode().split()
len(words)

word_counter = collections.Counter(words)

for word, count in word_counter.most_common(5):
    print(f"{word} - {count}")

print(f"QUESTION - {word_counter['QUESTION']}")
print(f"CIRCUMFLEX - {word_counter['CIRCUMFLEX']}")
print(f"DIGIT - {word_counter['DIGIT']}")
print(f"PYTHON - {word_counter['PYTHON']}")
