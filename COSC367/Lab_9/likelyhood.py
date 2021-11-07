import csv
def learn_likelihood(file_name, pseudo_count=2, n=3):
    """return the likelihood probabilities"""
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)] 
    training_examples = training_examples[1:]

    liklihood = [[0, 0]for c in range(n)]
    spam1 = len([[i[n]] for i in training_examples if i[n] == "T"])
    spam0 = len(training_examples) - spam1



    result = []
    for index, value in enumerate(training_examples):
        for i in range(n):
            if value[-1] == "T" and value[i] == "T":
                liklihood[i][1] += 1
            elif value[-1] == "F" and value[i] == "T":
                liklihood[i][0] += 1
    final_result = []
    for l in liklihood:
        spam_0, spam_1 = l
        probability_spam0 =  (spam_0 + pseudo_count) / (spam0 + (pseudo_count * 2)) 
        probability_spam1 = (spam_1 + pseudo_count) / (spam1 + (pseudo_count * 2)) 
        final_result.append((probability_spam0, probability_spam1))
    final_result.append(((spam1 + pseudo_count)/(len(training_examples) + (pseudo_count * 2))))
    return (final_result)


likelihood = learn_likelihood("test_csv.csv")
print(likelihood)
print("P(X1=True | Y=True ) = {:.2f}".format(likelihood[0][True]))
print("P(X1=True | Y=False) = {:.2f}".format(likelihood[0][False]))

print()
print("P(X2=True | Y=True ) = {:.2f}".format(likelihood[1][True]))
print("P(X2=True | Y=False) = {:.2f}".format(likelihood[1][False]))
print()
print("P(Y=True = {:.2f}".format(likelihood[3]))