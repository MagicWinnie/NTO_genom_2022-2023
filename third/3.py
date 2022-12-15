def get_compliment(sequence: str) -> str:
    map_nucl = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    compliment = ''.join([map_nucl[ch] for ch in sequence])
    return compliment


def is_self_compliment(sequence: str, max_self_compliment: int) -> bool:
    to_check = sequence[-max_self_compliment:]
    compliment = get_compliment(to_check)
    return compliment in sequence[::-1]


def get_reverse_primer(sequence: str, primer_sequence: str, rev_primer_len: int,
                       min_ampl_len: int, max_ampl_len: int,
                       min_gc: float = 50, max_gc: float = 60,
                       min_melting_temp: float = 50, max_melting_temp: float = 60, max_self_compl: int = 4):
    sequence = sequence.upper()
    primer_sequence = primer_sequence.upper()
    rev_compl_sequence = get_compliment(sequence[::-1])
    straight_primer_ind = len(rev_compl_sequence) - sequence.index(primer_sequence)
    for i in range(0, len(rev_compl_sequence) - rev_primer_len + 1):
        subsequence = rev_compl_sequence[i:i+rev_primer_len]
        g = subsequence.count('G')
        c = subsequence.count('C')
        gc = (g + c) / rev_primer_len * 100
        Tm = 64.9 + 41 * (g + c - 16.4) / rev_primer_len
        # print(subsequence, i, straight_primer_ind - i, gc, Tm, not is_self_compliment(subsequence, max_self_compl))
        if (min_gc <= gc <= max_gc and min_melting_temp <= Tm <= max_melting_temp and
                not is_self_compliment(subsequence, max_self_compl) and
                min_ampl_len <= abs(straight_primer_ind - i) <= max_ampl_len):
            return subsequence
    return False
