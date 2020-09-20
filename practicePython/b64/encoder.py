import base64
import sys

__all__ = ["str_to_base64"]

def str_to_base64(x):
    return base64.b64encode(x.encode("utf-8"))


def main():
    target = sys.argv[1]
    print(str_to_base64(target))


if __name__ == "__main__":
    main()