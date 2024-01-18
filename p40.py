#Get the top three items in a shop
items_prices = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
top_items=[]
for i in range(3):
    max_items=max(items_prices,key=items_prices.get)
    top_items.append(max_items)
    del items_prices[max_items]
print(top_items)
counter=0
while counter<3 and items_prices:
    max_items=max(items_prices,key=items_prices.get)
    top_items.append(max_items)
    del items_prices[max_items]
    counter+=1
print(top_items)
