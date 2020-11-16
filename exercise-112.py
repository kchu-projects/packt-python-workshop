from decimal import Decimal, getcontext
getcontext().prec = 3


base_rate = Decimal(0.10)

def _manager_adjust(salary, rise):
    if rise < base_rate:
        # We need to keep the managers happy
        return base_rate

    if salary >= 1000000:
        # They are making enough already
        return rise - base_rate


def calculate_new_salary(salary, promised_pct, is_manager, is_good_year):
    rise = promised_pct
    # remove 10% if it was a bad year
    if not is_good_year:
        rise -= base_rate
    else:
        pass

    # managers have a special adjust
    if is_manager:
        rise = _manager_adjust(salary, rise)

    # extra bonus for people with high rises
    if rise >= base_rate * 2:
        rise = rise + base_rate

    salary_increase = salary * rise
    return int(salary + salary_increase)


rose_salary = calculate_new_salary(1_000_000, Decimal(0.30), True, True)
print(f"Rose's salary will be: {rose_salary}")
