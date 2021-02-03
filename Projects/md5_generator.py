import hashlib
import base64

text = 'This is me and this is my forst attempt in md5'
md_result = hashlib.md5(text.encode())
base64_result = base64.b64encode(text.encode())
sha384_result  = hashlib.sha384(text.encode())

print(md_result.hexdigest())
print(base64_result.hex())
print(sha384_result.hexdigest())
