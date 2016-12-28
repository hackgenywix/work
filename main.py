
if __name__ == '__main__':
    pass
def read_code_parts(text_file="",spliter="$%#@"):
    lines =  open(text_file, 'r').readlines()
    agg = []
    code_parts = []
    for item in lines:
        if item == spliter:
            code_parts += ['\n'.join(agg)]
            agg = []
        else:
            agg += [item]
    return code_parts

