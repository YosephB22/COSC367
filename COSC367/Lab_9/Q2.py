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



prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, True, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true))  