#CurrencyConvert.py
Current = input("")
if "USD" in Current:
    RMB = eval( Current[3: ]) * 6.78
    print("RMB{:.2f}".format(RMB))
elif "RMB" in Current:
    UBD = eval( Current[3: ]) / 6.78
    print("USD{:.2f}".format(UBD))
