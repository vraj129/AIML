print("***********")
word_stats = {}
f = open("C://Users//Vraj.Patel//Desktop//Vraj Patel//AIML//week2_3//file//poem.txt","r")
for line in f:
    words = line.split(" ")
    for w in words:
        if w in word_stats:
            word_stats[w] += 1
        else:
            word_stats[w] = 1

print(word_stats)

max_count = max(list(word_stats.values()))
print(max_count)
f.close()

print("***********")
f = open("path to the file","r")
f_out = open("path to the file","w")
f_out.write("Company Name,PE Ratio,PB Ratio\n")
for line in f:
    words = line.split(",")
    companyname = words[0]
    pe_ratio = float(words[1])/float(words[2])
    pb_ratio = float(words[1])/float(words[3])
    f_out.write(f"{companyname},{pe_ratio},{pb_ratio}")
    f_out.write("\n")
f.close()
f_out.close()
