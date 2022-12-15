def formating(string: str):
    if string.startswith('#'):
        return False
    columns = string.strip().split()
    chrom, pos, _, ref, alt, *_ = columns
    return f"chr{chrom}:{pos} {ref}/{alt}"
