import serial

def tryExceptError():
    try:
        ser = serial.Serial('COM9',9600)
        print(sre.readline().decode("utf-8").strip('\n').strip('\r'))
    except SyntaxError:
        print("Syntax Error")
    except NameError:
        print("Tidak ada variabel tersebut")
    except TypeError:
        print("Tipe data salah")
    except:
        print("Terjadi sebuah kesalahan")
        
tryExceptError()