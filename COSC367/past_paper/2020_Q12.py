network = {
    'D': {
        'Parents': [],
        'CPT': {
            (): 0.001,
         }
    },
    'B': {
        'Parents': ['A','D'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
        }
    },

    'A': {
        'Parents': ['C'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
        }
    },

    'C': {
        'Parents': [],
        'CPT': {
            (): 0.7,
        }
    },
}