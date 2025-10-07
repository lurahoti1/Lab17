from B_clean import clean_rows, parse_csv, RAW

def filter_by_course(rows, course: str) -> list:
    return [r for r in rows if r[3] == course]

def filter_by_city(rows, city: str) -> list:
    return [r for r in rows if r[2] == city]

def sum_payments(rows) -> float:
    return sum(r[4] for r in rows)

def avg_age(rows) -> float:
    if not rows:
        return -1
    return sum(r[1] for r in rows) / len(rows)

if __name__ == "__main__":
    rows = clean_rows(parse_csv(RAW))
    py_rows = filter_by_course(rows, "Python")
    ex_rows = filter_by_course(rows, "Excel")
    tirana_rows = filter_by_city(rows, "Tiranë")

    print(f"Python: {len(py_rows)} regjistrime | Shuma: {sum_payments(py_rows)} EUR")
    print(f"Excel: {len(ex_rows)} regjistrime | Shuma: {sum_payments(ex_rows)} EUR")
    print(f"Tiranë | Mesha e moshës: {round(avg_age(tirana_rows), 2)}")
