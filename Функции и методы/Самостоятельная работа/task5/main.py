# TODO реализовать функцию
def get_sentences_list(text):
    list = []
    sentens = text.split('.')
    for word in sentens:
        if word:
            word_new = word.strip()
            list.append(word_new)
    return list


print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
