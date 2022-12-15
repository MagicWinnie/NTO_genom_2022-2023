def is_self_compliment(sequence: str, max_self_compliment: int) -> bool:
    map_nucl = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    sequence = sequence.upper()
    to_check = sequence[-max_self_compliment:]
    compliment = ''.join([map_nucl[ch] for ch in to_check])
    return compliment in sequence[::-1]


def get_primer(sequence: str, primer_len: int, min_gc: float = 50, max_gc: float = 60,
               min_melting_temp: float = 50, max_melting_temp: float = 60, max_self_compl: int = 4):
    for i in range(len(sequence) - primer_len + 1):
        subsequence = sequence[i:i+primer_len]
        a = subsequence.count('A')
        t = subsequence.count('T')
        g = subsequence.count('G')
        c = subsequence.count('C')
        gc = (g + c) / primer_len * 100
        Tm = 64.9 + 41 * (g + c - 16.4) / primer_len
        if (min_gc <= gc <= max_gc and min_melting_temp <= Tm <= max_melting_temp and not is_self_compliment(subsequence, max_self_compl)):
            return subsequence
    return False
