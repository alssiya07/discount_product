# Product catalog
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount rules
discount_rules = {
    "flat_10_discount": (200, 10),
    "bulk_5_discount": (10, 5),
    "bulk_10_discount": (20, 10),
    "tiered_50_discount": (30, 50)
}

# Fees
gift_wrap_fee = 1
shipping_fee_per_package = 5
items_per_package = 10

# Input quantities and gift wrap preference for each product
quantities = {}
gift_wraps = {}

for product in catalog.keys():
    quantity = int(input(f"Enter the quantity of {product}: "))
    gift_wrap = input(f"Wrap {product} as a gift? (yes/no): ").lower()

    quantities[product] = quantity
    gift_wraps[product] = gift_wrap == "yes"

# Calculate subtotal
subtotal = 0
for product, quantity in quantities.items():
    subtotal += catalog[product] * quantity

# Apply discount rules and find the most beneficial one
discount_name = None
discount_amount = 0

for rule, (threshold, discount) in discount_rules.items():
    if subtotal > threshold:
        if rule == "bulk_10_discount" and sum(quantities.values()) > 20:
            discount_name = rule
            discount_amount = subtotal * (discount / 100)
        elif rule == "tiered_50_discount" and sum(quantities.values()) > 30 and any(
                qty > 15 for qty in quantities.values()):
            discount_name = rule
            discount_amount = sum(
                (qty - 15) * catalog[product] * (discount / 100) for product, qty in quantities.items() if qty > 15)
        elif rule == "flat_10_discount":
            discount_name = rule
            discount_amount = discount
        elif rule == "bulk_5_discount" and any(qty > 10 for qty in quantities.values()):
            max_discount = max(
                qty * catalog[product] * (discount / 100) for product, qty in quantities.items() if qty > 10)
            if max_discount > discount_amount:
                discount_name = rule
                discount_amount = max_discount

# Calculate shipping fee and gift wrap fee
num_packages = sum(quantities.values()) // items_per_package
shipping_fee = num_packages * shipping_fee_per_package
# gift_wrap_fee_total = sum(gift_wraps.values()) * gift_wrap_fee
gift_wrap_fee_total = sum([quantities[product] for product, wrap in gift_wraps.items() if wrap]) * gift_wrap_fee

# Calculate total
total = subtotal - discount_amount + shipping_fee + gift_wrap_fee_total

# Output details
print("Product Details:")
for product, quantity in quantities.items():
    total_amount = catalog[product] * quantity
    print(f"{product}: {quantity} x ${catalog[product]} = ${total_amount}")

print("\nSubtotal: $", subtotal)
print("Discount applied:", discount_name)
print("Discount amount: $", discount_amount)
print("Shipping fee: $", shipping_fee)
print("Gift wrap fee: $", gift_wrap_fee_total)
print("Total: $", total)
