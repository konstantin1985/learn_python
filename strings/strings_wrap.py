

def Wrap(text, width):
    
    breakSymbols = [' ','.', ';', ',']
    
    text = text + ' ' # break symbol at the end
    word = ''
    lines = ['']
    
    for x in text:

        word += x    
                    
        if x in breakSymbols:
            if len(lines[-1]) + len(word) > width:
                lines.append('')               # move to new line
            lines[-1] += word
            word = ''
    
    lines = [line.rstrip() for line in lines] # remove last spaces if any
    return '\r'.join(lines)

s = 'ALS-24111LVT 8/16/24 FE, 2/4 GE fiber 1.0.0.28 Linux 2.6.19 #4 PREEMPT Wed Jun 28 13:35:09 +04 2017'
print Wrap(s, 29)
