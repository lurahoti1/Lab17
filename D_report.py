from C_query import clean_rows, parse_csv, RAW, filter_by_city, filter_by_course, sum_payments, avg_age

def as_money(v: float) -> str:
    return f"{v:.2f}"

def city_summary(rows, city: str) -> str:
    filtered = filter_by_city(rows, city)
    total = as_money(sum_payments(filtered))
    avg = round(avg_age(filtered), 2)
    return f"Qyteti: {city} | Regjistrime: {len(filtered)} | Shuma: {total} EUR | Mesha moshës: {avg}"

def course_summary(rows, course: str) -> str:
    filtered = filter_by_course(rows, course)
    total = as_money(sum_payments(filtered))
    return f"Kursi: {course} | Regjistrime: {len(filtered)} | Shuma: {total} EUR"

if __name__ == "__main__":
    rows = clean_rows(parse_csv(RAW))
    print(course_summary(rows, "Python"))
    print(course_summary(rows, "Excel"))
    print(city_summary(rows, "Tiranë"))
    print(city_summary(rows, "Durrës"))
