network = {
    'B': {
        'Parents': [],
        'CPT': {
            (): 0.001,
         }
    },
        
    'C': {
        'Parents': ['A','D'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
        }
    },

    'A': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
        }
    },

    'D': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
        }
    },
}