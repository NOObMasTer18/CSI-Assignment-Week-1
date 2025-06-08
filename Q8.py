#Formatting a String

#defining a fucntion

def print_formatted(number):
    #width is the required size of padded space
    width = len(f"{number:b}")

    
    for i in range(1,number+1):
        print(f"{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)