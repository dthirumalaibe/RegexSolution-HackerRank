# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

tx = ''
erg = []
for n in range(int(input())):
    tx += input()
    
for n in range(int(input())):
    e = input()
    print(len(re.findall(e[:len(e)-2] + '[sz]e', tx)))
