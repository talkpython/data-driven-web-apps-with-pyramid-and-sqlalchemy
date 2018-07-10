from typing import Optional


def try_int(text: str) -> Optional[int]:
    try:
        return int(text)
    except:
        return None
