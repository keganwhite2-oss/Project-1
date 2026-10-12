def tip(bill, percent) :
    tip_in_dollars = bill * (percent / 100)
    return tip_in_dollars
def total(bill, percent) :
    return bill + tip(bill, percent)
print(f"Tip: ${tip(50, 20):.2f}")     # Tip: $10.00
print(f"Tip: ${tip(23.5, 15):.2f}")   # Tip: $3.52
print(f"Total: ${total(50, 20):.2f}")
