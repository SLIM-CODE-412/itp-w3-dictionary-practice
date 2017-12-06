"""
customers = {
    'UT': [{
        'name': 'Mary',
        'age': 28
    }, {
        'name': 'John',
        'age': 31
    }, {
        'name': 'Robert',
        'age': 16
    }],
    'NY': [{
        'name': 'Linda',
        'age': 71
    }],
    'CA': [{
        'name': 'Barbara',
        'age': 15
    }, {
        'name': 'Paul',
        'age': 18
    }]
}
"""



  
  
  
def number_of_customers_per_state(customers_dict):
    final_dict = {}
    for state, state_customers in customers_dict.items():
        if state_customers is None:
            final_dict[state] = 0
        else:
            final_dict[state] = len(state_customers)
    return final_dict
        
    

  
 