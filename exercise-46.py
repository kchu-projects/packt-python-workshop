def convert_usd_to_aud(amount, rate=0.75):
    return amount / rate

print(convert_usd_to_aud(100))
print(convert_usd_to_aud(100, rate=0.78))
