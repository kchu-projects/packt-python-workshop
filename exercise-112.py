def _manager_adjust(salary, rise):
    if rise < 0.10:
        # We need to keep the managers happy
        return 0.10

    if salary >= 1000000:
        # They are making enough already
        return rise - 0.10


def calculate_new_salary(salary, promised_pct, is_manager, is_good_year):
    rise = promised_pct
    # remove 10% if it was a bad year
    if not is_good_year:
        rise -= 0.1
    else:
        pass

    # managers have a special adjust
    if is_manager:
        rise = _manager_adjust(salary, rise)

    # extra bonus for people with high rises
    if rise >= 0.20:
        rise = rise + 0.10

    salary_increase = salary * rise
    return int(salary + salary_increase)


rose_salary = calculate_new_salary(1_000_000, 0.30, True, True)
print(f"Rose's salary will be: {rose_salary}")
