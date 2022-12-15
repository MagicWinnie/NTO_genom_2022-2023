from typing import List

def sliding_window(sequence: str, n: int) -> List[float]:
    GC = []
    for i in range(len(sequence) - n + 1):
        subsequence = sequence[i:i+n]
        gc = (subsequence.count('G') + subsequence.count('C')) / n
        GC.append(gc)
    return GC
