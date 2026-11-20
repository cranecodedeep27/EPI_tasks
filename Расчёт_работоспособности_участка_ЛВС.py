"""Расчёт работоспособности участка Ethernet. Вариант 1."""

# Для каждого типа: базы PDV, задержка на метр, базы PVV, предел длины.
# Базы перечислены слева направо: левый, промежуточный, правый.
# None в базе PDV означает, что сегмент нельзя ставить в эту позицию.
# PVV правого сегмента в расчёт не входит, поэтому его вклад равен нулю.
PARAMETERS = {
    "10Base-T": ((15.3, 42.0, 165.0), 0.113, (10.5, 8, 0), 100),
    "10Base-FL": ((12.3, 33.5, 156.5), 0.1, (10.5, 8, 0), 2000),
    "10Base-FB": ((None, 24.0, None), 0.1, (None, 2, 0), 2000),
}

# Тип сегмента, длина в метрах, количество подключённых станций.
SEGMENTS = [
    ("10Base-T", 100, 25),
    ("10Base-FL", 500, 0),
    ("10Base-FB", 50, 0),
    ("10Base-FB", 600, 0),
    ("10Base-FB", 100, 0),
    ("10Base-T", 100, 15),
]

STATION_LIMIT = 1024
PDV_LIMIT = 575
PVV_LIMIT = 48
ROLES = ("левый", "промежуточный", "правый")


def number(value):
    """Формат числа с десятичной запятой."""
    return f"{value:g}".replace(".", ",")

def calculate_path(path):
    """Рассчитать вклад каждого сегмента и суммы PDV и PVV."""
    rows = []
    for index, (segment_number, (kind, length, _)) in enumerate(path):
        role = 1
        if index == 0:
            role = 0
        elif index == len(path) - 1:
            role = 2

        pdv_bases, delay_per_meter, pvv_bases, _ = PARAMETERS[kind]
        base = pdv_bases[role]
        if base is None:
            raise ValueError(f"Сегмент {segment_number}: {kind} нельзя ставить с краю.")

        pdv = round(base + length * delay_per_meter, 3)
        pvv = pvv_bases[role]
        rows.append((segment_number, ROLES[role], base, length, delay_per_meter, pdv, pvv))

    total_pdv = round(sum(row[5] for row in rows), 3)
    total_pvv = sum(row[6] for row in rows)
    return rows, total_pdv, total_pvv


def show_check(label, value, limit, unit):
    """Напечатать сравнение с допустимым пределом."""
    passed = value <= limit
    sign = "<=" if passed else ">"
    status = "норма" if passed else "превышение"
    print(f"{label}: {number(value)} {sign} {limit} {unit} — {status}")
    return passed


def main():
    print("Расчёт работоспособности участка ЛВС — вариант 1")
    print(f"Длина пути по кабелю: {sum(length for _, length, _ in SEGMENTS)} м")
    station_count = sum(stations for _, _, stations in SEGMENTS)
    checks = [show_check("Количество станций", station_count, STATION_LIMIT, "станций")]

    print("\nПроверка длины сегментов")
    path = list(enumerate(SEGMENTS, start=1))
    for segment_number, (kind, length, _) in path:
        label = f"Сегмент {segment_number}, {kind}"
        checks.append(show_check(label, length, PARAMETERS[kind][3], "м"))
        
    for direction in (path, path[::-1]):
        print(f"\nНаправление от сегмента {direction[0][0]} к сегменту {direction[-1][0]}")
        rows, total_pdv, total_pvv = calculate_path(direction)
        for segment_number, role, base, length, delay, pdv, pvv in rows:
            print(
                f"Сегмент {segment_number} ({role}): PDV = {number(base)} + "
                f"{length} * {number(delay)} = {number(pdv)} bt, "
                f"PVV = {number(pvv)} bt"
            )
        checks.append(show_check("Итого PDV", total_pdv, PDV_LIMIT, "bt"))
        checks.append(show_check("Итого PVV", total_pvv, PVV_LIMIT, "bt"))
        
        if all(checks):
            print("\nВывод: участок ЛВС работоспособен.")
        else:
            print("\nВывод: участок ЛВС не удовлетворяет условиям задачи.")
            
if __name__ == "__main__":
    main()