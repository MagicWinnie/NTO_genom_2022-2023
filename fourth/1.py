from typing import List, Dict
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
    map_nucl: Dict[str, str] = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    compliment: str = ''.join([map_nucl[ch] for ch in sequence])
    return compliment


def find_target(seq: str, pam: str, orient_pam: str, length_target: int) -> List[str]:
    pam_regex: str = ''.join(list(map(get_regex, pam)))
    if orient_pam == 'R':
        target_regex: str = f'(?=([AGCT]{{{str(length_target)}}})({pam_regex}))'
    else:
        target_regex: str = f'(?=({pam_regex})([AGCT]{{{str(length_target)}}}))'
    regex = re.compile(target_regex)
    compliment: str = get_compliment(seq)
    output_list: List[str] = []
    output_list += [x[0] if orient_pam == 'R' else x[1] for x in regex.findall(seq)]
    output_list += [x[0] if orient_pam == 'R' else x[1] for x in regex.findall(compliment[::-1])]
    return output_list
