import csv
def learn_likelihood(file_name, pseudo_count=0):
    """return the likelihood probabilities"""
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)] 
    training_examples = training_examples[1:]
    liklihood = [[0, 0]for c in range(12)]
    spam1 = len([[i[12]] for i in training_examples if i[12] == "1"])
    spam0 = len(training_examples) - spam1
    result = []
    for index, value in enumerate(training_examples):
        for i in range(12):
            if value[-1] == "1" and value[i] == "1":
                liklihood[i][1] += 1
            elif value[-1] == "0" and value[i] == "1":
                liklihood[i][0] += 1
    final_result = []
    for l in liklihood:
        spam_0, spam_1 = l
        probability_spam0 =  (spam_0 + pseudo_count) / (spam0 + (pseudo_count * 2)) 
        probability_spam1 = (spam_1 + pseudo_count) / (spam1 + (pseudo_count * 2)) 
        final_result.append((probability_spam0, probability_spam1))
    return (final_result)


likelihood = learn_likelihood("spam-labelled.csv")
print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))