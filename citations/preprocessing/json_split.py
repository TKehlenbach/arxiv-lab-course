import numpy as np
import logging

logging.basicConfig(filename='json_split.log', format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

total_lines = 409129302
num_objects = 5354309
per_file = 100000
num_files = int(np.ceil(num_objects/per_file))

logger.info('Split into %s files', num_files)

counter_boundaries = []
for i in range(0, num_files+1):
    if per_file*i < num_objects:
        counter_boundaries.append(per_file*i)
    else:
        counter_boundaries.append(num_objects-1)

f_read = open('../citation-network-dataset/edited_dblp.v13.json', 'r')

f_numerator = enumerate(f_read)
objects = 0
for file in range(0, num_files):
    filename = 'citation-network-dataset/split-dataset/dblp' + str(file) + '.v13.json'
    f_write = open(filename, 'w')
    logger.info('Open file %s', filename)
    bound = counter_boundaries[file + 1]
    if file != 0:
        f_write.write('[')
    while objects < bound:
        i, line = next(f_numerator)
        if line == '},\n':
            if objects != bound-1:
                f_write.write(line)
                objects += 1
                print('Add object number ', objects+1, ' to the file')
                continue
            elif objects == bound-1:
                new_line = line.replace(',', '')
                f_write.write(new_line)
                f_write.write(']')
                objects += 1
                print('Add last object number ', objects+1, ' to the file')
                continue
        f_write.write(line)
    f_write.close()
