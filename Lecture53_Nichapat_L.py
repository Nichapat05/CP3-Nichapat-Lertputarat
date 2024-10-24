price = int(input("Enter price : "))
def vatCalculation(totalprice):
    result = totalprice + (totalprice * 0.07)
    return result

print(vatCalculation(price))
    