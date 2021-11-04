network = {
    'Y': {
        'Parents': [],
        'CPT': {
            (): 6/11,
         }
    },
        
    'X1': {
        'Parents': ["Y"],
        'CPT': {
            (True,): 3/8,
            (False,): 5/7,
        }
    },

    'X2': {
        'Parents': ["Y"],
        'CPT': {
            (True,): 3/8,
            (False,): 4/7,
        }
    },

    'X3': {
        'Parents': ['Y'],
        'CPT': {
            (True,): 2/8,
            (False,): 2/7,
        }
    },
}


for assignment, prob in sorted(network['X1']['CPT'].items()):
    print(assignment, "{:0.2f}".format(prob))