def find_mutation(seq1: str, seq2: str) -> str:
    if '-' in seq1:
        l_ind = seq1.index('-')
        r_ind = seq1.rindex('-')
        return f'ins{l_ind}:{seq2[l_ind:r_ind + 1]}'
    elif '-' in seq2:
        l_ind = seq2.index('-')
        r_ind = seq2.rindex('-')
        return f'del{l_ind + 1}:{r_ind + 1}'
    else:
        return 'False'
