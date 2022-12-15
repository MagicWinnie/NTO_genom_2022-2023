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
