import logging
logging.basicConfig(level=logging.INFO)

def integerCubeRootHelper(n, left, right):
    logging.info(f"integerCubeRootHelper({n},left={left},right={right})")
    cube = lambda x: x * x * x # anonymous function to cube a number
    assert(n >= 1)
    assert(left < right)
    assert(left >= 0)
    assert(right < n)
    assert(cube(left) < n), f'{left}, {right}'
    assert(cube(right) > n), f'{left}, {right}'
    # your code here

    mid = (left+right)//2
    logging.info(f"midpoint={mid}")
    logging.info(f"cube({mid})={cube(mid)}, cube({mid+1})={cube(mid+1)}")

    if cube(mid) <= n and cube(mid+1) > n:
        logging.info(f"reached end of the line; returning {mid}")
        return mid
    elif cube(mid) <= n:
        return integerCubeRootHelper(n, mid, right)
    else:   
        return integerCubeRootHelper(n, left, mid)


# Write down the main function
def integerCubeRoot(n):
    assert( n > 0)
    if (n == 1): 
        return 1
    if (n == 2):
        return 1
    return integerCubeRootHelper(n, 0, n-1)

def assert_code():
    assert(integerCubeRoot(1) == 1)
    assert(integerCubeRoot(2) == 1)
    assert(integerCubeRoot(4) == 1)
    assert(integerCubeRoot(7) == 1)
    assert(integerCubeRoot(8) == 2)
    assert(integerCubeRoot(20) == 2)
    assert(integerCubeRoot(26) == 2)
    for j in range(27, 64):
        assert(integerCubeRoot(j) == 3)
    for j in range(64,125):
        assert(integerCubeRoot(j) == 4)
    for j in range(125, 216):
        assert(integerCubeRoot(j) == 5)
    for j in range(216, 343):
        assert(integerCubeRoot(j) == 6)
    for j in range(343, 512):
        assert(integerCubeRoot(j) == 7)
    print('Congrats: All tests passed! (10 points)')

def main():
    try:
        assert_code()
    except:
        import ipdb
        ipdb.post_mortem()

if __name__ == "__main__":
    main()