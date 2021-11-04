import csv
def learn_prior(file_name, pseudo_count=0):
    """
    calculate P(c=true)
    """
    print(file_name)
    spam = 0
    total = 0
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)] 
        training_examples = training_examples[1:]
        for row in training_examples:
            total += 1
            if row[-1] == "1":
                spam += 1
        smoothing = (spam + pseudo_count) / (total + (pseudo_count * 2))
        return smoothing


prior = learn_prior("spam-labelled.csv", pseudo_count = 1)
print(format(prior, ".5f"))