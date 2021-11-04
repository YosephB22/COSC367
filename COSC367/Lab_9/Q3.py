import csv
def learn_prior(file_name, pseudo_count=0):
    """
    each row corresponds with example(possible assignment).
    there are 12 features(evidence).
    two possible assignment for a feature. 1 or 0.
    1 --> spam(possitive).
    0 --> non-spam(negative).
    finding the probability of how many 1s appears in a table.
    """

    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)] 
    training_examples = training_examples[1:]
    count_spam = 0
    for rows in training_examples:
        if rows[12] == "1":
            count_spam += 1
    probability_spam = (count_spam + pseudo_count) / (len(training_examples) + (pseudo_count * 2))
    return probability_spam



prior = learn_prior("spam-labelled.csv")
print("Prior probability of spam is {:.5f}.".format(prior))