import sys

def main():
    a = 10
    b = 20
    
    if len(sys.argv) > 1 and sys.argv[1] == '--root':
        try:
            custom = int(sys.argv[2])
            print(f"Sum: {a + b + custom}")
        except:
            print("Invalid custom number")
    else:
        print(f"Sum: {a + b}")

if __name__ == "__main__":
    main()
