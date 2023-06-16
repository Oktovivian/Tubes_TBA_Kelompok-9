file = open('test.txt','r').read().split()

def inTerminal(teks, terminal):
    status = True
    i = 0
    while i < len(teks)-1 and status:
        if teks[i] not in terminal:
            status = False
        i+=1
    return status

def FOR(teks):
    terminal=['f','o','r']
    daftarState=['Q0','Q1','Q2','FOR']
    tabel=[['Q1','error','error'],
        ['error','Q2','error'],
        ['error','error','FOR'],
        ['error','error','error']]   
    state='Q0'
    i=0
    teks = ''.join(teks)
    teks+='#'
    status=teks[i] != '#' and inTerminal(teks, terminal)
    while (status and teks[i]!='#'):
        state=tabel[daftarState.index(state)][terminal.index(teks[i])]
        i+=1
        if (state=='error'):
            status=False

    if state != 'FOR':
        state = 'error'
    return state  


def separator(teks):
    terminal=[';']
    daftarState=['Q0','separator']
    tabel=[['separator'], ['error']]
    state='Q0'
    i=0
    teks = ''.join(teks)
    teks+='#'
    status=teks[i] != '#' and inTerminal(teks, terminal)
    while (status and teks[i]!='#'):
        state=tabel[daftarState.index(state)][terminal.index(teks[i])]
        i+=1
        if (state=='error'):
            status=False
    
    if state != 'separator':
        state = 'error'
    return state


def aksi(teks):
    terminal=['a','b','0','1','2','3','+','-','=',':']
    daftarState=['Q0','Q1','Q2','Q3','Q4','Q5','assignment','increment']
    tabel=[['Q1','Q1','error','error','error','error','error','error','error','error'],
        ['error','error','error','error','error','error','Q4','Q5','Q3','Q2'],
        ['error','error','error','error','error','error','error','error','Q3','error'],
        ['assignment','assignment','assignment','assignment','assignment','assignment','error','error','error','error'],
        ['error','error','error','error','error','error','increment','error','error','error'],
        ['error','error','error','error','error','error','error','increment','error','error'],
        ['error','error','error','error','error','error','Q3','error','error','error'],
        ['error','error','error','error','error','error','error','error','error','error']]
    state='Q0'
    i=0
    teks = ''.join(teks)
    teks+='#'
    status=teks[i] != '#' and inTerminal(teks, terminal)
    while (status and teks[i]!='#'):
        state=tabel[daftarState.index(state)][terminal.index(teks[i])]
        i+=1
        if (state=='error'):
            status=False

    if state == 'assignment' or state == 'increment':
        state = 'aksi'
    else:
        state = 'error'

    return state


def kondisi(teks):
    terminal=['a','b','0','1','2','3','=','>','<']
    daftarState=['Q0','Q1','Q2','Q3','Q4','kondisi']
    tabel=[['Q1','Q1','error','error','error','error','error','error','error'],
        ['error','error','error','error','error','error','error','Q2','Q3'],
        ['kondisi','kondisi','kondisi','kondisi','kondisi','kondisi','Q4','error','error'],
        ['kondisi','kondisi','kondisi','kondisi','kondisi','kondisi','Q4','error','error'],
        ['kondisi','kondisi','kondisi','kondisi','kondisi','kondisi','error','error','error'],
        ['error','error','error','error','error','error','error','error','error']]
    
    state='Q0'
    i=0
    teks = ''.join(teks)
    teks+='#'
    status=teks[i] != '#' and inTerminal(teks, terminal)
    while (status and teks[i]!='#'):
        state=tabel[daftarState.index(state)][terminal.index(teks[i])]
        i+=1
        if (state=='error'):
            status=False

    if state != 'kondisi':
        state = 'error'
    return state
#print(kondisi(file))


def kurawalDepan(teks):
    terminal=['{']
    daftarState=['Q0','kurawalDpn']
    tabel=[['kurawalDpn'], ['error']]
    state='Q0'
    i=0
    teks = ''.join(teks)
    teks+='#'
    status=teks[i] != '#' and inTerminal(teks, terminal)
    while (status and teks[i]!='#'):
        state=tabel[daftarState.index(state)][terminal.index(teks[i])]
        i+=1
        if (state=='error'):
            status=False
    
    if state != 'kurawalDpn':
        state = 'error'
    return state

def kurawalBelakang(teks):
    terminal=['}']
    daftarState=['Q0','kurawalBlk']
    tabel=[['kurawalBlk'], ['error']]
    state='Q0'
    i=0
    teks = ''.join(teks)
    teks+='#'
    status=teks[i] != '#' and inTerminal(teks, terminal)
    while (status and teks[i]!='#'):
        state=tabel[daftarState.index(state)][terminal.index(teks[i])]
        i+=1
        if (state=='error'):
            status=False
    
    if state != 'kurawalBlk':
        state = 'error'
    return state


#print(FOR(file[0]))