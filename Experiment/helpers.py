##check if value is integer
def isInt(value):
    try:
        int(value)
    except Exception:
        raise ValueError("%s IS NOT INTEGER!!!" % value)
    return 0