from collections import defaultdict
def posterior(prior, likelihood, observation):
    """
    prior = the probability value of the class being TRUE.
    likelihood = ( P(observation = true|class=FALSE), P(observation=true|class=TRUE) )
    observation = the feature's domain value
    posterior function = P(C|observation[i])
    """
    class_false = 1 - prior
    class_true = prior
    # result = defaultdict(float)
    for index, (obser_T_class_F, obser_T_class_T) in enumerate(likelihood):
        if observation[index] == True:
            class_true *= obser_T_class_T
            class_false *= obser_T_class_F
        else:
            class_false *= (1 - obser_T_class_F)
            class_true *= (1 - obser_T_class_T)
    alpha = class_false + class_true
    return class_true / alpha



prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, True, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
    .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
    .format(class_posterior_true))
