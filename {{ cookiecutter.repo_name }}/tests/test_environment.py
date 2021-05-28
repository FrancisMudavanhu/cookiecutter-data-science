import sys

REQUIRED_PYTHON = "python3"
required_major = 3


def main():
    system_major = sys.version_info.major
    
    if system_major != required_major:
        raise TypeError(
            f"This project requires Python {required_major}."
            f" Found: Python {sys.version}")
    else:
        print(">>> Development environment passes all tests!")



if __name__ == '__main__':
    main()
