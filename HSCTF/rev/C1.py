
import socket

class C1:
    def decode(self, sample):
        if sample == '':
            return
        if sample == ": " or sample[0] == "U":
            return
        a = []
        lastIndex = 0
        for i in range(len(sample)):
            if sample[i] == 'm' or sample[i] == 'a':
                a.append(sample[lastIndex:i])
                a.append(sample[i])
                i += 1
                lastIndex = i

        temp = ""
        i = 1
        while True:
            #print(sample[-i])
            if sample[-i] == 'a' or sample[-i] == 'm':
                break
            temp += sample[-i]
            i += 1
        a.append(temp[::-1])
        sample = a
        #print(f"Sample: {sample}")

        i = 0
        while i < len(sample):
            if sample[i] == 'a':
                result = int(sample[i-1]) + int(sample[i+1])
                sample[i] = result
                sample.pop(i+1)
                sample.pop(i-1)
                i = 0
                #sample[i+1] = "_"
                #sample[i-1] = "_"
            i += 1
            #print(f"{i}: {''.join([str(j) for j in sample])}")
        #sample.remove('_')

        
        i = 0
        while i < len(sample):
            if sample[i] == 'm':
                sample.pop(i)
                i = 0
            i += 1

        #print(sample)
        result = 1
        for i in range(len(sample)):
            result *= int(sample[i])
            #print(result)
        return result

    def __init__(self):
        HOST, PORT = "not-really-math.hsc.tf", 1337

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))    
            data = s.recv(1024)
            for i in range(1000):
                data = s.recv(1024)
                #print("data", data)
                data= data.decode("utf-8")

                if "{" in data:
                    print(data)

                if data == ' ' or data == ":":
                    break
                sample = data.split('\n')[0]
                #print('Received', sample)
                result = self.decode(sample)
                if result == None:
                    break
                print("sending", result)
                s.sendall(str(result).encode('utf-8') + b"\n")
            print(data)
            data = s.recv(1024).decode("utf-8")
            print(data)
            data = s.recv(1024).decode("utf-8")
            print(data)
            data = s.recv(1024).decode("utf-8")
            print(data)
            data = s.recv(1024).decode("utf-8")
            print(data)

if __name__ == "__main__":
    c = C1()