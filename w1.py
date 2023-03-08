def bag_of_words(texts):
    stop_words = set(["is", "This", "the", "Is"])
    vocabulary = set()
    for text in texts:
        words = text.split()
        for word in words:
            if word not in stop_words:
                vocabulary.add(word)
    vocabulary = list(vocabulary)
    
    bags = []
    for text in texts:
        bag = [0] * len(vocabulary)
        words = text.split()
        for word in words:
            if word in vocabulary:
                bag[vocabulary.index(word)] += 1
        bags.append(bag)
        
    return bags, vocabulary

texts = ['This is the first document.',
         'This is the second second document.',
         'And the third one.',
         'Is this the first document?']
bags, vocabulary = bag_of_words(texts)
print(vocabulary)
print(bags)