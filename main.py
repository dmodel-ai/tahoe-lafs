
import sys

from twisted.scripts.trial import run

def main():
    sys.argv = ["twisted.trial", "allmydata"]
    run()


if __name__ == "__main__":
    main()
