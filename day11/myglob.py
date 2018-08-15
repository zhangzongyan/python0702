
import glob

#res = glob.glob("/etc/a*")
#res = glob.glob("/etc/grou?")
res = glob.glob("/etc/^[abc]*")

print(res)




