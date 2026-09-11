import io, re, importlib.util
spec = importlib.util.spec_from_file_location('m', 'md_to_article.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
f = 'drafts/canton-fair-autumn-2026-final-2026-09-11.md'
t = io.open(f, encoding='utf-8').read()
toc, html = m.md_to_html(t)
print('sections', len(toc))
print('h3', html.count('<h3>'))
print('tables', html.count('table-wrap'))
print('tips', html.count('article-tip'))
print('nonascii_html', sum(1 for c in html if ord(c) > 127))
print('external_links_preserved', 'https://www.cantonfair.org.cn' in html, 'https://www.mofcom.gov.cn' in html)
low = t.lower()
for tok in ['%', '->', '=>', 'commission', '+20', 'markup', ' jade', 'feicui', '100%', 'guarantee']:
    print('token', repr(tok), low.count(tok))
print('dashes', any(c in t for c in ['\u2013', '\u2014', '\u2018', '\u2019', '\u201c', '\u201d', '\u2022', '\u2192']))
print('faq_count', t.count('### '))
