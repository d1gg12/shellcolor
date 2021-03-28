def shellcolor(str: str,
               forecolor: str = None,
               backcolor: str = None,
               bold: bool = False,
               dim: bool = False,
               italic: bool = False,
               underline: bool = False,
               blink: bool = False,
               inverted: bool = False,
               hidden: bool = False,
               print_raw: bool = False) -> str:
    divide = False
    code = '\033['
    if forecolor is not None:
        if forecolor == 'red':
            code += '31'
        elif forecolor == 'green':
            code += '32'
        elif forecolor == 'yellow':
            code += '33'
        elif forecolor == 'blue':
            code += '34'
        elif forecolor == 'magenta':
            code += '35'
        elif forecolor == 'cyan':
            code += '36'
        elif forecolor == 'grey':
            code += '37'
        divide = True

    if backcolor is not None:
        if divide:
            code += ';'
        else:
            divide = True
        if backcolor == 'red':
            code += '41'
        elif backcolor == 'green':
            code += '42'
        elif backcolor == 'yellow':
            code += '43'
        elif backcolor == 'blue':
            code += '44'
        elif backcolor == 'magenta':
            code += '45'
        elif backcolor == 'cyan':
            code += '46'
        elif backcolor == 'grey':
            code += '47'
    
    if bold:
        code += divide * ';' + '1'
        divide = True
    if dim:
        code += divide * ';' + '2'
        divide = True
    if italic:
        code += divide * ';' + '3'
        divide = True
    if underline:
        code += divide * ';' + '4'
        divide = True
    if blink:
        code += divide * ';' + '5'
        divide = True
    if inverted:
        code += divide * ';' + '6'
        divide = True
    if hidden:
        code += divide * ';' + '7'
        divide = True
    
    code += 'm' + str + '\033[0m'
    if print_raw:
        print(repr(code))
    return code


if __name__ == '__main__':
    print(shellcolor('test',forecolor='green',backcolor='yellow',bold=True, dim=True, underline=True, print_raw=True))
