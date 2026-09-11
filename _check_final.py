import io, re
f = 'drafts/canton-fair-autumn-2026-final-2026-09-11.md'
t = io.open(f, encoding='utf-8').read()
lines = t.split('\n')
body = '\n'.join(l for l in lines if not re.match(r'^Meta\s', l))
print('WORDS', len(re.findall(r"[A-Za-z0-9']+", body)))
print('NONASCII', sum(1 for c in t if ord(c) > 127))
print('H1_LINE', lines[5])
print('H1_CHARS', repr(lines[5]))
print('--- contrast ---')
print('comma_not', len(re.findall(r', not ', body)))
print('rather_than', len(re.findall(r'rather than', body)))
print('instead_of', len(re.findall(r'instead of', body)))
for m in re.finditer(r'[^.]*, not [^.]*\.', body):
    print('  CN:', m.group(0).strip()[:120])
for m in re.finditer(r'[^.]*rather than[^.]*\.', body):
    print('  RT:', m.group(0).strip()[:120])
for m in re.finditer(r'[^.]*instead of[^.]*\.', body):
    print('  IO:', m.group(0).strip()[:120])
print('--- links ---')
for a in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', t):
    print('  ', a[1], '||', a[0])
print('phrase_CantonFairOctober2026', body.lower().count('canton fair october 2026'))
orig = io.open('drafts/canton-fair-autumn-2026-2026-09-11.md', encoding='utf-8').read()
print('ORIGINAL_H1', orig.split('\n')[5])
