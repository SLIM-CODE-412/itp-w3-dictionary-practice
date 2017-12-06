def calculate_purchase_price(purchase, set_to_dict=False):
    sub_total = 0
    for k1, v1 in purchase.items():
        if k1 == 'books':
            for i in v1:
                for k2, v2 in i.items():
                    if k2 == "price":
                        sub_total += v2
    if set_to_dict == True:
        purchase['total'] = sub_total
                            
    return sub_total
        

                
                



"""
def add_book_to_purchase(purchase_dict, title, author, price=0.99):
    purchase_dict['books'].append({'title': title, 'author': author, 'price': price})
    return purchase_dict
    
    """