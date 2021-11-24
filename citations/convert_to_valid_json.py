problem = 'NumberInt'
total_lines = 409129302
f_read = open('citation-network-dataset/dblp.v13.json', 'r')
f_write = open('citation-network-dataset/edited_dblp.v13.json', 'w')
for pos, line in enumerate(f_read):
    print(pos, ' out of ', total_lines, ' (', pos/total_lines*100, '%)')
    if problem in line:
        line = line.replace(problem, '')
        line = line.replace('(', '')
        line = line.replace(')', '')
        print(line)
    f_write.write(line)
