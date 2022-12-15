def check_primer(sequence: str, min_GC: float = 50, max_GC: float = 60, min_primer_len: int = 18, max_primer_len: int = 25) -> bool:
    sequence = sequence.upper()
    primer_len = len(sequence)
    GC = (sequence.count('G') + sequence.count('C')) / primer_len * 100
    return min_primer_len <= primer_len <= max_primer_len and min_GC <= GC <= max_GC
