import whois 
domain = whois.query("binarynote.com")
print(domain.dict)