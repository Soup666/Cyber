import sys
from pathlib import Path
from types import CodeType

src = Path(__file__).read_text()

print(sys.version)
print(src)

codestring = bytes.fromhex(input('Give me your bytecode in hex:'))
assert len(codestring) <= 2000, 'Too long!'

print('Thanks!')
print('I will give you two gifts in exhange, what do you want?')

gift1 = input('gift1: ')
gift2 = input('gift2: ')
assert len(gift1) <= 10, 'Too long!'
assert len(gift2) <= 10, 'Too long!'

code = CodeType(0, 0, 0, 0, 0, 0, codestring, (), (f'__{gift1}__', f'__{gift2}__'), (), '', '', 0, b'')

result = eval(code, {'__builtins__': None}, {})
print('success, bye!')
