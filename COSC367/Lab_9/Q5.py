
import csv
# Q2 function
def posterior(prior, likelihood, observation):
    """ 
    prior = real number --> p(Class=true).
    likelihood = tuple -->  likelihood[i][False] -->  p(X[i]=true|C=false).
    observation = tuple n booleans -->  observation[i] --> (true or false)
    returns p(Class=true|observation)"""
    result_true_prior = prior
    result_false_prior = 1 - prior
    for index, obs in enumerate(observation):
        prior_false, prior_true = likelihood[index]
        if obs == True:
            result_true_prior *= prior_true
            result_false_prior *= prior_false
        else:
            result_true_prior *= (1 - prior_true)
            result_false_prior *= (1 - prior_false)
    alpha = result_true_prior + result_false_prior
    return result_true_prior / alpha

# Q2 function
def learn_prior(file_name, pseudo_count=0):
    """
    each row corresponds with example(possible assignment).
    there are 12 features(evidence).
    two possible assignment for a feature. 1 or 0.
    1 --> spam(possitive).
    0 --> non-spam(negative).
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

# Q4 function
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

# new function
def nb_classify(prior, likelihood, input_vector):
    """
    input vector --> tuple of 12 integers(0 or 1) = featues from X1 to X12.
    return a tuple, where first element is spam or no-spam. the second element is certainty(posterior).
    """
    # spam(1)
    P_class_True_observation = posterior(prior, likelihood, input_vector)
    # not spm(0)
    P_class_False_observation = 1 - P_class_True_observation
    if P_class_True_observation <= 0.5:
        return ("Not Spam", P_class_False_observation)
    else:
        return ("Spam", P_class_True_observation)












prior = learn_prior("spam-labelled.csv", pseudo_count=1)
likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
    ]

predictions = [nb_classify(prior, likelihood, vector) 
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))