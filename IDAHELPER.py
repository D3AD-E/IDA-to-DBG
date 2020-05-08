idaBase = input("IDA starting offset ")
dbgBase = input("Olly starting offset ")

diff = int(idaBase,16) - int(dbgBase, 16)

while 1:
    idaFunc = input("Offset of function in IDA ");
    dbgFunc = int(idaFunc,16) + diff
    print(hex(dbgFunc))