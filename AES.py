
class AES:
    def __init__(self):
        self.keygen = AES_keygen()
        self.keygen.generateKeys()
        pass

class AES_keygen:
    def __init__(self,initkey):
        self.momentaneTransformation = 0
        self.RC = 0 # TODO MAY DELETE LATER (NOT NEEDED)
        self.keylist = []
        if (len(initkey)%128!=0): raise CustomError("Key len does not match 128/256/512 bit")
        self.mode = len(initkey)/128 # 1 for 128 2 for 256 etc
        self.keylist.append(initkey)

    def generateKeys(self):
        keysections=self.__splitkey32()
        nextkeysections=[]
        for _ in range():
            nextkeysections.append(self.__32bitxor(keysections[0], self.__G(keysections[-1])))
            for i in range(len(keysections) - 1):
                nextkeysections.append(self.__32bitxor(keysections[i], keysections[i + 1]))
            retlist = []
            for i in nextkeysections:
                retlist += i
            self.keylist.append(retlist)
            keysections = nextkeysections

    def __G(self,bitpair32):
        def __applyroundRC():
            if (self.momentaneTransformation == 1):
                rc = 1
            if (self.momentaneTransformation ):
                rc = 2**(self.momentaneTransformation-1)
           #if ()
        eightbitlist = [bitpair32[i*8:i*8+8] for i in range(4)]
        afterG8bitlist = []
        afterG8bitlist.append(eightbitlist[-1])
        for i in range(len(eightbitlist), 1, -1):
            afterG8bitlist.append(eightbitlist[i])
        afterG8bitlist[0]=__applyroundRC(afterG8bitlist[0])
        return afterG8bitlist

    def __8bitxor(self,A,B):
        for a,b in zip(A,B):
            a = a^b
        return A
    def __32bitxor(self,A,B):
        for a,b in zip(A,B):
            a = a^b
        return A
    def __splitkey32(self):
        splitlist = []
        for i in range(self.mode*4):
            splitlist.append(self.keylist[i*32:i*32+32])
        return splitlist

    def getkeyno(self, no):
        if (len(self.keylist) < 2): raise CustomError("No keys generated")
        if not (len(self.keylist) >= no): raise IndexError
        return self.keylist[no]

    def getkey(self):
        if (len(self.keylist)<2): raise CustomError("No keys generated")
        retval = self.keylist[self.momentaneTransformation]
        self.momentaneTransformation+=1
        return retval

class CustomError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Error: %s" % self.value

