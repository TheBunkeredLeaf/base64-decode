import base64
import codecs

b64Str = codecs.encode(input("decode base64: "))
resStr = base64.b64decode(b64Str)

print(resStr)
