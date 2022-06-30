from pwn import *
import math
import decimal

D = decimal.Decimal

e = D(67232005046673182936686667923618923423886014608739025121716376103403182731380352946546332831299352999141914227463085948272873360071831867519614801255948512968846308007947813589885305604963617306081740208208033450335195208581671402514189934777652268432484943322697597085569395632441709734720659593362335123721
)
N = D(71622257283030712757462534811738321339212590924025026669337442399246463401151176946623890787966455936203101729868331984360445587899601712434170134988165856031487439310686050761358882417932295210474942534604705275085254757381954493038767359129679143424763702089338890628904544717375498905965552686141674223153
)
c_m = 70392135098931085689522070946877176805313729254096716186124207686975372753169838497849133241585441405460365032299386010703343280268866799222685273265703128564124276532355688744322432972170488397526586230404293620919860965261833093427235752879836968482193570968713722051418427436508205506323239097818169652051

#Continued fraction expansion of e/N (see https://en.wikipedia.org/wiki/Continued_fraction):
n_fe = e #nominator
d_fe = N #denominator
fraction_list = []

def expand_fraction_list(n_fe, d_fe):
    with decimal.localcontext() as ctx:
        ctx.prec = 350    
        cap = math.floor(n_fe/d_fe)
        rest = n_fe%d_fe
        fraction_list.append(cap)
        
        n_fe = d_fe
        d_fe = rest
    return (n_fe, d_fe)

def cfe(a_list, j): #Calculate fraction from fraction_list
    n_next = 0
    d_next = 1
    while j >= 0:
        d = d_next
        k = a_list[j]*d_next+n_next
        n_next = d
        d_next = k
        j = j-1
    return k,d #returns guess for k and d. d is the private key.



#Perform Wieners Attack (see https://en.wikipedia.org/wiki/Wiener%27s_attack)

n_fe, d_fe = expand_fraction_list(n_fe, d_fe) #creates 0th element in fraction list

for i in range(1,1000):   
    n_fe, d_fe = expand_fraction_list(n_fe, d_fe) #adds new element to fraction list
    k,d = cfe(fraction_list, i) #calculates the fraction for the i'th fraction expansion
    with decimal.localcontext() as ctx:
        ctx.prec = 10000
        PhiN = D((e*d-1)/k)
        if PhiN%1 == 0 and d%2 == 1: #Checks if phi(N) is a natural number and if d is odd
            with decimal.localcontext() as ctx: #try to solve square equation x2 + bx + c == 0
                ctx.prec = 1000
                b = -(N-PhiN+1)
                c = N
                sqr2 = b**2-4*c
                if sqr2 > 0: #checks if squareroot therm is larger than 0
                    sqr = D(sqr2.sqrt())
                    if sqr%1 == 0 and ((-b+sqr)/2)%1 == 0 and ((-b-sqr)/2)%1 == 0: #checks if squareroot-therm and the two solutions are all natural numbers
                        break

print("d = ", d)            

N = int(N)

m_c = pow(c_m, d, N)
print("Decrypted message: ", m_c)

from Crypto.Util.number import long_to_bytes
text = long_to_bytes(m_c)

print("Plain text: ", text)