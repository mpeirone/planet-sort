def dataora(bollatura):
  return bollatura[8:18]
 
outfilename= "out.txt"
infilename="in.txt"
print("BollaSort by mpeirone V1.0")
print("File di input: "+ infilename) 
print("File di output: "+ outfilename) 

lines_seen = set() # holds lines already seen
outfile = open(outfilename, "w")
for line in open(infilename, "r"):
    if line not in lines_seen: # not a duplicate
        lines_seen.add(line)
lines_seen=sorted(lines_seen, key=dataora)
for line in lines_seen:
       outfile.write(line)
outfile.close()