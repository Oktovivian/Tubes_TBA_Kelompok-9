
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