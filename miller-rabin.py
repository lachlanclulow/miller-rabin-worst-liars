import random
from math import floor


def miller_rabin(n, a):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    if pow(a, d, n) == 1:
        return True
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return True
    return False

def get_bad_witnesses(star_witnesses, target):
    for p_candidate in range(4, target):
        if p_candidate % 2 != 0:
            # check star witnesses
            is_prime = all([miller_rabin(p_candidate, x) for x in star_witnesses])
            #print(f'{p_candidate} prime? {is_prime}')

            if not is_prime:
                for witness in range(2, p_candidate):
                    if miller_rabin(p_candidate, witness):
                        if witness in bad_witnesses:
                            bad_witnesses[witness]['count'] += 1
                            bad_witnesses[witness]['lies'].append(p_candidate)
                        else:
                            bad_witnesses[witness] = {
                                'count': 1,
                                'lies': [p_candidate]
                            }
        if p_candidate % floor(target/100) == 0:
            print(f'{p_candidate}/{target} processed - {floor(p_candidate/target*100)}%')
    return bad_witnesses


if __name__ == '__main__':
    bad_witnesses = {}
    star_witnesses = [2, 3]
    target = 10000

    for k, v in get_bad_witnesses(star_witnesses, target).items():
        print(f'{k}: {v}')


    


