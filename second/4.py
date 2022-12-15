def calculate_tm(sequence: str) -> int:
    sequence = sequence.upper()
    w = sequence.count('A')
    x = sequence.count('T')
    y = sequence.count('G')
    z = sequence.count('C')
    Tm = 64.9 + 41 * (y + z - 16.4) / (w + x + y + z)
    Tm = round(Tm)
    return Tm
