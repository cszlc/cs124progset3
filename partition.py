import sys

# input: partition flag algorithm inputfile

# Print input args
def main():

    # Ensure right number of arguments
    if (len(sys.argv) != 5):
        print("Usage: partition flag algorithm inputfile")
        return -1

    print(sys.argv[1])
    print(sys.argv[2])
    print(sys.argv[3])
    print(sys.argv[4])

if (__name__ == "__main__"):
    main()