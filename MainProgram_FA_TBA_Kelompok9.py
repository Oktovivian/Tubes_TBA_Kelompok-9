import FA_TBA_Kelompok9 as FA
file = open('test.txt','r').read().split()

statement = list()
statement.append(FA.FOR(file[0]))
statement.append(FA.kondisi(file[1]))
statement.append(FA.kurawalDepan(file[2]))
statement.append(FA.aksi(file[3]))
statement.append(FA.kurawalBelakang(file[4]))

'''
<statement>	-> for<kondisi>{<aksi>}
'''
test1 = ['FOR', 'kondisi', 'kurawalDpn', 'aksi', 'kurawalBk']

i = 0
status = True
while i < len(test1)-1 and status:
    if test1[i] != statement[i]:
        status = False
    i+=1
print(file)
if status:
    print('Input Valid')
else:
    print('Input Tidak Valid')