def add_tax(pretax_total) :
    total_after_tax = pretax_total * 0.10
    return pretax_total + total_after_tax
print(add_tax(200))
