#the task of the backpack

#input values
MAX_WEIGHT = 26
print(f"Backpack capacity: {MAX_WEIGHT}")
#goods
goods = list()
objCreate = lambda t, w, p: dict(title = t, weight = w, price = p)
def obj(t, w, p):
  ob = objCreate(t, w, p)
  goods.append(ob)
  return ob

#things list [INPUT]
a = obj('a', 4, 10)
b = obj('b', 6, 4)
c = obj('c', 8, 10)
d = obj('d', 7, 7)
e = obj('e', 10, 6)
f = obj('f', 3, 1)
g = obj('g', 5, 9)
h = obj('h', 2, 5)
#goods output
print("All the things:")
for i in goods: print(i)
#sets generation
setTitles = list()
for step in range(len(goods) - 1):
  if step:
    for product in goods:
      for productsCouple in setTitles:
        productsSorted = productsCouple.copy()
        productsSorted.append(product['title'])
        productsSorted.sort()
        if not (productsSorted in setTitles or \
         product['title'] in productsCouple):
          setTitles.append(productsSorted)
  else:
    for product1 in goods:
      for product2 in goods:
        things = [product1['title'], product2['title']]
        productsSorted = things.copy()
        productsSorted.sort()
        if not (product1['title'] == product2['title'] or \
         productsSorted in setTitles):
          setTitles.append(productsSorted)

sets = list()
for titles in setTitles:
  things = list()
  for title in titles:
    for product in goods:
      if title == product['title']:
        things.append(product)
  sets.append(things)
#output values
weight = 0
price = 0
things = None
#searching {weight, price}
for _set in sets:
  _weigth = 0
  _price = 0
  for product in _set:
    _weigth += product['weight']
    _price += product['price']
  if _weigth <= MAX_WEIGHT and _price >= price:
    weight = _weigth
    price = _price
    things = setTitles[sets.index(_set)]

#output result
print(f"\nApproptiate set {things}:")
print(f"  weight: {weight}\n  price: {price}")
