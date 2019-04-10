def tryExceptError():
    try:
        from p1174050_scatter import scatter as sct
    except SyntaxError:
        print("ERRROOOOOOOOOOOOOOOR")

tryExceptError()