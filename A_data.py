RAW = """Shqipe Kola,17,Tiranë,Python,120
Ardit Hysa,19,Durrës,Excel,80
Elira Daci ,18, Tiranë ,Python, 120
Jon Gega,17,Shkodër,Python,90
Megi Poro,18,Elbasan,Excel,80
,17,Tiranë,Python,120
Erion L,18,Tiranë,Python,abc"""

def parse_csv(raw: str) -> list[tuple[str,int,str,str,float]]:
    rows = []
    for line in raw.strip().split('\n'):
        fields = [f.strip() for f in line.split(',')]
        if len(fields) != 5:
            continue
        name, age, city, course, payment = fields
        if not name:
            continue
        try:
            age = int(age)
            payment = float(payment)
        except ValueError:
            continue
        rows.append((name, age, city, course, payment))
    return rows

if __name__ == "__main__":
    parsed = parse_csv(RAW)
    print(f"Rreshta të vlefshëm: {len(parsed)}")

