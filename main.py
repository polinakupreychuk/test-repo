def count_words_and_sentences(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        word_count = len(text.split())
        sentence_count = 0

        for char in text:
            if char in ['.', '!', '?']:
                sentence_count += 1

        return word_count, sentence_count

file_path = "text.txt"
word_count, sentence_count = count_words_and_sentences(file_path)
print("Кількість слів:", word_count)
print("Кількість речень:", sentence_count)
