import whois

w = whois.whois('binarynote.com')
print(w['domain_name'])
