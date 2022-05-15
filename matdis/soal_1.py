def main(a, b):
    gcd, (x, y) = find_gcd(a,b, True)
    print("PBB(%d, %d) = %d" % (a,b,gcd))
    print("%d = %d(%d) + %d(%d)" % (gcd, a, x, b, y))
    

def find_gcd(a,b, showSteps = False):
    """
    Find the greatest common divisor of a and b.
    Uses the 'textbook' eucledian algorithm method for
    calculating thereatest common divisor between two
    numbers.
    Parameters
    ----------
    a : int
    b : int
    showSteps : boolean
        If True, will print the equations needed to
        find the gcd as if doing it on paper
    Returns
    -------
    int,
        The gcd of a and b
    (int, int)
        Returned from find_extended_gcd
    """

    if showSteps:
        print("--------------- Persamaan Kombinasi Lanjar ---------------")
        
    # Make sure that a is always bigger than b
    if (b > a):
        b,a = a,b

    list_of_q = []
    while (a % b != 0):
        q,r = a//b, a%b
        list_of_q.append(q)
        if showSteps:
            print("%d = %d(%d) + %d" % (a,b,q,r))
        a = b
        b = r
        
    if showSteps:
        print("-------------- /Persamaan Kombinasi Lanjar ---------------")
        print()
        
    return r, find_extended_gcd(list_of_q, showSteps)


def find_extended_gcd(list_of_q, showSteps = False):
    """
    Find the coeficients of a linear combination
    of a and b to equal the gcd
    Uses the 'textbook' extended eucledian algorithm method
    for calculating the linear combination of a and b needed
    to get the gcd. Uses a tabular method instead of continuous
    substitution.
    In other words, how many a's and how many b's do we need to
    sum up to the gcd?
    Parameters
    ----------
    list_of_q : [int]
        The list of q values obtained by doing the eucledian algorithm
    showSteps : boolean
        If True, will print the table that computes the
        linear combination of a and b needed to get the gcd.
    Returns
    -------
    int, int
        The coeficients of a linear combination
        of a and b to equal the gcd
    """
    a_row_values = [1,0] 
    b_row_values = [0,1]

    for i in range(2,len(list_of_q)+2):
        a_row_values.append(a_row_values[i-2] - a_row_values[i-1] * list_of_q[i-2])
        b_row_values.append(b_row_values[i-2] - b_row_values[i-1] * list_of_q[i-2])
        
    return a_row_values[-1], b_row_values[-1]


if __name__ == '__main__':
    main(1242, 1986)