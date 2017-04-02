sentense = 'he is go-out run'
result = []


def Isnouns(word):
    word = word + '\n'
    text_file_ = open('dic/nouns.txt', 'r')
    lines = text_file_.readlines()
    for line in lines:
        if (word == line):
            return 'true'
            break
    return 'false'


def Isverp(word):
    word = word + '\n'
    text_file_verps = open('dic/verbs.txt', 'r')
    lines = text_file_verps.readlines()
    for line in lines:
        if (word == line.lower()):
            return 'true'
            break
    return 'false'


def IsAdverbs(word):
    word = word + '\n'
    text_file_ = open('dic/adverbs.txt', 'r')
    lines = text_file_.readlines()
    for line in lines:
        if (word == line.lower()):
            return 'true'
            break
    return 'false'


def IsAdjectives(word):
    word = word + '\n'
    text_file_ = open('data/adjectives.txt', 'r')
    lines = text_file_.readlines()
    for line in lines:
        if (word == line.lower()):
            return 'true'
            break
    return 'false'


def IsAdpositions(word):
    word = word + '\n'
    text_file_ = open('data/adpositions.txt', 'r')
    lines = text_file_.readlines()
    for line in lines:
        if (word == line.lower()):
            return 'true'
            break
    return 'false'


def IsConjunctions(word):
    word = word + '\n'
    text_file_ = open('data/conjunctions.txt', 'r')
    lines = text_file_.readlines()
    for line in lines:
        if (word == line.lower()):
            return 'true'
            break
    return 'false'


def IsDeterminers(word):
    word = word + '\n'
    text_file_ = open('data/determiners.txt', 'r')
    lines = text_file_.readlines()
    for line in lines:
        if (word == line.lower()):
            return 'true'
            break
    return 'false'


def IsNumeral(word):
    word = word + '\n'
    text_file_ = open('data/numeral.txt', 'r')
    lines = text_file_.readlines()
    for line in lines:
        if (word == line.lower()):
            return 'true'
            break
    return 'false'


def IsPronouns(word):
    word = word + '\n'
    text_file_ = open('data/pronouns.txt', 'r')
    lines = text_file_.readlines()
    for line in lines:
        if (word == line.lower()):
            return 'true'
            break
    return 'false'


def main():
    words = sentense
    words = words.lower()
    words = words.replace('\n', ' ')
    words = words.split(' ')
    words = list(filter(None, words))

    for w in words:
        if (Isverp(w) == 'true'):
            result.append('Verb')
        elif (IsAdjectives(w) == 'true'):
            result.append('Adjective')
        elif (IsAdpositions(w) == 'true'):
            result.append('Adposition')
        elif (IsAdverbs(w) == 'true'):
            result.append('Adverbs')
        elif (IsConjunctions(w) == 'true'):
            result.append('Conjunction')
        elif (IsDeterminers(w) == 'true'):
            result.append('Determiner')
        elif (IsNumeral(w) == 'true'):
            result.append('Numeral')
        elif (IsPronouns(w) == 'true'):
            result.append('Pronoun')
        elif (Isnouns(w) == 'true'):
            result.append('Noun')
        else:
            result.append('Not Define')

    for x in range(0, len(words)):
        print(words[x], '---->', result[x])


main()
