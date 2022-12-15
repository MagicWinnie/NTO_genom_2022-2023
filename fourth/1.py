from typing import List
import re


def get_regex(nucl: str) -> str:
    if nucl == r'A':
        return r'A'
    elif nucl == 'C':
        return r'C'
    elif nucl == 'G':
        return r'G'
    elif nucl == 'T':
        return r'T'
    elif nucl == 'R':
        return r'[GA]'
    elif nucl == 'Y':
        return r'[TC]'
    elif nucl == 'K':
        return r'[GT]'
    elif nucl == 'M':
        return r'[AC]'
    elif nucl == 'S':
        return r'[GC]'
    elif nucl == 'W':
        return r'[AT]'
    elif nucl == 'B':
        return r'[GTC]'
    elif nucl == 'D':
        return r'[GAT]'
    elif nucl == 'H':
        return r'[ACT]'
    elif nucl == 'V':
        return r'[GCA]'
    else:
        return r'[AGCT]'


def get_compliment(sequence: str) -> str:
    map_nucl = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    compliment = ''.join([map_nucl[ch] for ch in sequence])
    return compliment


def find_target(seq: str, pam: str, orient_pam: str, length_target: int) -> List[str]:
    pam_regex = ''.join(list(map(get_regex, pam)))
    target_regex_r = '([AGCT]{' + str(length_target) + '})' + '(' + pam_regex + ')'
    target_regex_l = '(' + pam_regex + ')' + '([AGCT]{' + str(length_target) + '})'
    compliment = get_compliment(seq)
    output_list = []
    output_list += [x[0] if orient_pam == 'L' else x[0] for x in re.findall(target_regex_r, seq)]
    output_list += [x[1] if orient_pam == 'L' else x[0] for x in re.findall(target_regex_l, seq[::-1])]
    output_list += [x[0] if orient_pam == 'L' else x[0] for x in re.findall(target_regex_r, compliment)]
    output_list += [x[1] if orient_pam == 'L' else x[0] for x in re.findall(target_regex_l, compliment[::-1])]
    return output_list

seq, pam, or_pam, len_target = input().split()
print(find_target(seq, pam, or_pam, int(len_target)))
print(get_compliment('TAGCTACGATCGATCGTTTCTAGCTACGATGCAAGAAAGATCGATCGATCGACGTACG')[::-1])