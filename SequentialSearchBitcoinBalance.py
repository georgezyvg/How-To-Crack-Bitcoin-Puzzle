import bit
x=int(input("'start range Min 1180591620717411303424-1461501637330902918203684832716283019655932542975 -> "))
y=int(input("stop range Max 1461501637330902918203684832716283019655932542975 -> "))
k = 1
F = []
P = x
while P<y:
    P+=1
    ran = P 
    key = bit.Key.from_int(ran)
    seq = 0
    print(key.address + ' : ' + key.to_hex() + ' : ' + key.get_balance('mbtc')) # btc mbtc usd
    if key.get_balance('mbtc') > str(seq) :
        print("Matching Key ==== Found!!!\n PrivateKey: " + key.to_wif())
        f=open(u"winner.txt","a")
        f.write('\nBitcoin Address: ' + key.address)
        f.write('\nPrivateKey (hex): ' + key.to_hex())
        f.write('\nPrivateKey (wif): ' + key.to_wif())
        f.write('\n==================================')
        f.close()
    k += 1