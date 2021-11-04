network = {
    'Y': {
        'Parents': [],
        'CPT': {
            (): (4+2)/(7+4),
         }
    },
        
    'X1': {
        'Parents': ['Y'],
        'CPT': {
            (True,): (1+2)/(4+4),
            (False,): (3+2)/(3+4)
        }
    },

    'X2': {
        'Parents': ['Y'],
        'CPT': {
            (True,): (1+2)/(4+4),
            (False,): (2+2)/(3+4)
            
        }
    },
    'X3': {
        'Parents': ['Y'],
        'CPT': {
            (True,): (0+2)/(4+4),
            (False,): (0+2)/(3+4)
        }
    }
}