from ossapi.enums import Grade


def parse_score_rank(rank: Grade) -> str:
    if rank.A != None:
        return "A"
    if rank.B != None:
        return "B"
    if rank.C != None:
        return "C"
    if rank.D != None:
        return "D"
    if rank.F != None:
        return "F"
    if rank.S != None:
        return "S"
    if rank.SH != None:
        return "SH"
    if rank.SS != None:
        return "SS"
    if rank.SSH != None:
        return "SSH"
    return None
