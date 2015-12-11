##check if value is integer
def isInt(value):
    try:
        int(value)
    except Exception:
        raise ValueError("%s IS NOT INTEGER!!!" % value)
    return 0


def kill(proc_pid):         ##function for killing process of showing picture
    process = psutil.Process(proc_pid)
    for proc in process.get_children(recursive=True):
        proc.kill()
    process.kill()          ##kill the process of showing an image

def yesOrNo(x):
    return {
        'Y': 1,
        'y': 1,
        'N': 0,
        'n': 0,
    }.get(x, -1)