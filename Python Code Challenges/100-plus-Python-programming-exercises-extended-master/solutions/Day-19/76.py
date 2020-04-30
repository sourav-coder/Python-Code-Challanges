s=b'hello world!hello world!hello world!hello world!'
import zlib
p=zlib.compress(s)
q=zlib.decompress(p)
print(p,q)
