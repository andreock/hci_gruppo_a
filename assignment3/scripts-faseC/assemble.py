import sys,os
src,tables,out=sys.argv[1:4]
t=open(tables).read().split('\n\n')
s=open(src).read().replace('{{CRITERI}}',t[0].strip()).replace('{{TOP10}}',t[1].strip()).replace('{{PAGINE}}',t[2].strip())
assert '{{' not in s
open(out,'w').write(s)
