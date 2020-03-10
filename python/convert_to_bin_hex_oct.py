def print_formatted(number):
    # your code goes here
    #D, O, H, b
    max_len = len(oct(number)[2:]) + len(hex(number)[2:]) + len(bin(number)[2:])

    bandwith = (len(bin(number)[2:])+1)
    #print(bandwith)
    for i in range(1, number+1):
        n_oct = oct(i)[2:]
        n_hex = (hex(i)[2:]).upper()
        n_bin = bin(i)[2:]
        print(str(i).rjust(bandwith-1) + n_oct.rjust(bandwith) + n_hex.rjust(bandwith) + n_bin.rjust(bandwith))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
