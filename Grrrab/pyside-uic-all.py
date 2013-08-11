import glob
from subprocess import call

files = glob.glob("*.ui")
for f in files:
    print "Lets convert", f,"...",
    name = f[:-3]
    call(["pyside-uic.exe", f, "-o", name+".py"])
    print "it's done!"

print "That's all folks!"