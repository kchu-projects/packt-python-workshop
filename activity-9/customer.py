def format_customer(fname, lname, location=""):
    customer_info = f"{fname} {lname}"
    if location:
        customer_info = f"{customer_info} ({location})"
    return customer_info
