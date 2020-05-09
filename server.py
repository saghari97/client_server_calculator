import math
import socket
from time import perf_counter

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)

print("Server is up and running")

while True:
    c, addr = s.accept()
    print("got conection from", addr)

    while True:
        sep=""
        num = 0
        try:

            data = c.recv(1024).decode()
            if data == "Q" or data == "q" or data == "Quit" or data == "quit" or data == "quit()":
                c.send("Quit".encode())
                break
            elif 'sin' in data:
                t1 = perf_counter()
                print("You gave me the equation:", data)
                data= data.split('$')
                x=math.sin(float(data[2])*0.01745329)
                result = round(float(x), 2)
                t2 = perf_counter()
                t = t2 - t1
                print(t)
            elif 'cos' in data:
                t1 = perf_counter()
                print("You gave me the equation:", data)
                data = data.split('$')
                x = math.cos(float(data[2]) * 0.01745329)
                result = round(float(x), 2)
                t2 = perf_counter()
                t = t2 - t1
                print(t)
            elif 'tan' in data:
                t1 = perf_counter()
                print("You gave me the equation:", data)
                data = data.split('$')
                x = math.tan(float(data[2]) * 0.01745329)
                result = round(float(x), 2)
                t2 = perf_counter()
                t = t2 - t1
                print(t)
            elif 'cot' in data:
                t1=perf_counter()
                print("You gave me the equation:", data)
                data = data.split('$')
                x=math.cos(float(data[2])* 0.01745329)/math.sin(float(data[2])* 0.01745329)
                result = round(float(x), 2)
                t2 = perf_counter()
                t = t2 - t1
                print(t)
            elif 'Add' in data:
                if ' $ ' in data:
                    data = data.split(" ")
                    for i in data:
                        sep+=i
                    sep=sep.split('$')
                    t1 = perf_counter()

                    op1 = float(sep[2])
                    op2 = float(sep[3])
                    print('Calculation Request:\n $ {}  $ {} $ {} $ '.format(sep[1],op1,op2))
                    x = op1 + op2
                    result = x
                    print(result)
                    t2 = perf_counter()
                    t = t2 - t1
                    print('Calculation Response:\n $ {}  $ {} $'.format(t , result))
                    print(t)
            elif 'Subtract' in data:
                t1 = perf_counter()
                print("You gave me the equation:", data)
                data = data.split('$')
                op1 = float(data[2])
                op2 = float(data[3])
                x = op1 - op2
                result = x
                print(result)
                t2 = perf_counter()
                t = t2 - t1
                print(t)
            elif 'Multiply' in data:
                t1 = perf_counter()
                print("You gave me the equation:", data)
                data = data.split('$')
                op1 = float(data[2])
                op2 = float(data[3])
                x = op1 * op2
                result = x
                print(result)
                t2 = perf_counter()
                t = t2 - t1
                print(t)
            elif 'Divide' in data:
                t1 = perf_counter()
                print("You gave me the equation:", data)
                data = data.split('$')
                op1 = float(data[2])
                op2 = float(data[3])
                x = op1 - op2
                result = x
                print(result)
                t2 = perf_counter()
                t = t2 - t1
                print(t)
            c.send(str(result).encode())
            #c.send(str(t).encode())

        except (ZeroDivisionError):
            c.send("ZeroDiv".encode())
        except (ArithmeticError):
            c.send("MathError".encode())
        except (SyntaxError):
            try:
                c.send("SyntaxError".encode())
            except (BrokenPipeError):
                break
        except (NameError):
            c.send("NameError".encode())
    print("Connection Closed with Client : ",addr)
    c.close()
