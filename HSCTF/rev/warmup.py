### encode

def cold(pwd):
        ret = pwd[17:] + pwd[:17]
        return ret

def cool(pwd):
        ret = b""
        for i,char in enumerate(pwd):
                if i % 2 == 0:
                        ret += bytes([char + 3*(i//2)])
                else:
                        ret += bytes([char])
        return ret


def warm(pwd):
        l = pwd.find(b"l")+1
        a = pwd[:l]
        pwd_end = pwd[l:]

        l = pwd_end.find(b"l")+1
        b = pwd_end[:l]
        c = pwd_end[l:]
        return c + b + a

def hot(pwd):
        adj = [-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 
                                21, 14, -45, -11, -48, -7, -1, 3, 47, -65, 3, -18, 
                                -73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13]
        ret = b""
        for i in range(len(pwd)):
                num = pwd[i] + adj[i]
                if num not in range(0, 256):
                        print("wrap around")
                num &= 0xff
                ret += bytes([num])
        return ret

def encode(pwd):
        print("encode:")

        stage1 = cold(pwd)
        print(stage1)

        stage2 = cool(stage1)
        print(stage2)

        stage3 = warm(stage2)
        print(stage3)

        stage4 = hot(stage3)
        print(stage4)

        return stage4

### decode

def rev_cold(pwd):
        ret = pwd[16:] + pwd[:16]
        return ret

def rev_cool(pwd):
        ret = b""
        for i,char in enumerate(pwd):
                if i % 2 == 0:
                        ret += bytes([(char - 3*(i//2)) & 0xff])
                else:
                        ret += bytes([char])
        return ret

def rev_warm(pwd):
        l = pwd.find(b"l")+1
        a = pwd[:l]
        pwd_end = pwd[l:]

        l = pwd_end.find(b"l")+1
        b = pwd_end[:l]
        c = pwd_end[l:]

        if not a or not b or not c:
                print("invalid")

        return c + b + a

def rev_hot(pwd):
        adj = [-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 
                                21, 14, -45, -11, -48, -7, -1, 3, 47, -65, 3, -18, 
                                -73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13]
        ret = b""
        for i in range(len(pwd)):
                num = pwd[i] - adj[i]
                if num not in range(0, 256):
                        print("wrap around")
                num &= 0xff
                ret += bytes([num])
        return ret


def reverse(pwd):
        print("decode:")
        stage3 = rev_hot(pwd)
        print(stage3)
        stage2 = rev_warm(stage3)
        print(stage2)
        stage1 = rev_cool(stage2)
        print(stage1)
        dec = rev_cold(stage1)
        print(dec)
        return dec
#enc = encode(b"aaaaaaaaaaaaaaaalbbbbbbbbbbbblccc")
#enc = encode(b"aaaaaaaaaaaalbbbbbbbblccccccccccc")
#print()
#dec = reverse(enc)
#print(dec)
reverse(b"4n_3nd0th3rm1c_rxn_4b50rb5_3n3rgy")