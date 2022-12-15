from typing import List


def align(seq1: str, seq2: str, match_penalty: int = 2, mismatch_penalty: int = -1, gap_insert_penalty: int = -2, gap_extend_penalty: int = -1) -> List[str]:
    m: int = len(seq1)
    n: int = len(seq2)

    score: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
   
    for i in range(0, m + 1):
        score[i][0] = gap_insert_penalty * i
    for j in range(0, n + 1):
        score[0][j] = gap_insert_penalty * j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match: int = score[i - 1][j - 1] + (match_penalty if seq1[i - 1] == seq2[j - 1] else mismatch_penalty)
            delete: int = score[i - 1][j] + gap_extend_penalty
            insert: int = score[i][j - 1] + gap_insert_penalty
            score[i][j] = max(match, delete, insert)
            
    align1: str = ''
    align2: str = ''
    i: int = m
    j: int = n
    while i > 0 and j > 0:
        score_curr: int = score[i][j]
        score_diag: int = score[i - 1][j - 1]
        score_up: int = score[i][j - 1]
        score_left: int = score[i - 1][j]

        if score_curr == score_diag + (match_penalty if seq1[i - 1] == seq2[j - 1] else mismatch_penalty):
            align1 += seq1[i - 1]
            align2 += seq2[j - 1]
            i -= 1
            j -= 1
        elif score_curr == score_left + gap_extend_penalty:
            align1 += seq1[i - 1]
            align2 += '-'
            i -= 1
        elif score_curr == score_up + gap_insert_penalty:
            align1 += '-'
            align2 += seq2[j - 1]
            j -= 1

    while i > 0:
        align1 += seq1[i - 1]
        align2 += '-'
        i -= 1
    while j > 0:
        align1 += '-'
        align2 += seq2[j - 1]
        j -= 1
    
    return [align1[::-1], align2[::-1]]
