# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
import re
p = re.compile('^[Hh][Ii]\s[^dD].*')
for i in range(n):
    x = str(input())
    if(len(re.findall(p, x)) > 0):
        print(x)
