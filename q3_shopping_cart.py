# Part A-Spot the Bug
def add_item(item, cart=[]):
    cart.append(item)
    return cart
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"])) # New list is applied 
print(add_item("eggs"))
# Part B - fix it
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
# Part C-Build the cart
# Create Cart
def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }
# Add Item
def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })
# Update Price (Tuple Example)
def update_price(price_tuple, new_price):
    # Tuples are immutable.
    # The next line will raise TypeError.
    price_tuple[0] = new_price
# Calculate Total
def calculate_total(cart):
    total = 0
    for item in cart["items"]:
        total += item["price"] * item["qty"]  #total=total+another quantity
        discount = total * cart["discount"] / 100
        return total - discount
# Customer 1
cart1 = create_cart("Rida", 10)
add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 500, 2)
# Customer 2
cart2 = create_cart("Ali", 5)
add_to_cart(cart2, "Book", 300, 3)
add_to_cart(cart2, "Pen", 20, 5)
print(cart1)
print("Total:", calculate_total(cart1))
print()
print(cart2)
print("Total:", calculate_total(cart2))
print()
try:
    price = (500,)
    update_price(price, 600)
except TypeError:
    print("TypeError: Tuples are immutable.")                           
    # 1. Why is discount=0 safe but cart=[] dangerous?
# Because 0 is immutable, while [] is mutable.
# Mutable objects can be shared between function calls.

# 2. Difference between rebinding and mutating?
# Rebinding means assigning a variable to a new object.
# Mutating means changing the existing object.

# 3. Which are mutable?
# Mutable: list,dict,set
# Immutable: tuple,str,int

# 4. When you pass a list into a function and modify it,
# do changes reflect outside?
# Yes.Lists are mutable and passed by object reference,
# so changes inside the function affect the original list