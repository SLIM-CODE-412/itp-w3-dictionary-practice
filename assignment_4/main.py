def eldest_customer_in_list(customers_list):
    eldest_customer = None
    for customer in customers_list:
        if eldest_customer is None or customer['age'] >= eldest_customer['age']:
            eldest_customer = customer
    return eldest_customer

def eldest_customer_per_state(customers_list):
    final_dict = {}
    for state, state_customers in customers_list.items():
        eldest_customer = eldest_customer_in_list(state_customers)
        final_dict[state] = eldest_customer
    return (final_dict)
    
  