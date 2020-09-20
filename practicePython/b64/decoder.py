import base64

__all__ = ["base64_to_str"]

def base64_to_str(x):
    return base64.b64decode(x).decode("utf-8")


