from A_data import parse_csv, RAW

def normalize_city(city: str) -> str:
    return city.strip().capitalize()

def normalize_course(course: str) -> str:
    return course.strip().title()

def clean_rows(rows: list[tuple[str,int,str,str,float]]) -> list[tuple[str,int,str,str,float]]:
    cleaned = []
    for name, age, city, course, payment in rows:
        name = name.strip()
        if len(name.replace(" ", "")) < 2:
            continue
        city = normalize_city(city)
        course = normalize_course(course)
        cleaned.append((name, age, city, course, payment))
    return cleaned

if __name__ == "__main__":
    parsed = parse_csv(RAW)
    cleaned = clean_rows(parsed)
    for row in cleaned[:3]:
        print(row)
