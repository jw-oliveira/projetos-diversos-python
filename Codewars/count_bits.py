def count_bits(n):
    bits = f'{n:08b}'
    count = bits.count('1')
    return count