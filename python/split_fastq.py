import argparse, os
from time import sleep

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True, help = "path to input directory")
ap.add_argument("-o", "--output_dir", required = True, help = "path to output directory")
args= vars(ap.parse_args())

path = args["dataset"]

for file in os.listdir(path):
    with open(path + file, 'r') as fmerge:
        fileName = file[:-6]
        print('[INFO] Spliting the file {}...'.format(fileName))
        with open(args['output_dir'] + '/' + fileName + '_1.fastq', 'a') as r1, open(args['output_dir'] + '/' + fileName + '_2.fastq', 'a') as r2:
            for (i , line) in enumerate(fmerge):
                if i % 8 < 4:
                    r1.write(line)
                else:
                    r2.write(line)
    print('[INFO] Spliting files DONE!')
