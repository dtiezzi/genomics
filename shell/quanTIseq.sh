#!/bin/bash

SAMPLESFILES=/path/to/file/listOfSamples
OUTPUTDIR=/path/to/output/dir
QUANTISEQ=/path/to/QUANTISEQ_Pipeline
TOKEN=/path/to/GDC_Download/Tokens/gdc-user-token
STARTFILES=1  
ENDFILES=20 
MANIFEST=/path/to/GDC_Download/Manifest/gdc_manifest
DOWNLOADDIR=/path/to/GDC_Download/Download_Files
FASTQ_Files=/path/to/GDC_Download/FASTQ_Files

for i in {1..20}
do

echo "Downloading files from $STARTFILES to $ENDFILES" | mailx -s 'Startig_Download' user@email ;


	head -n 1 $MANIFEST > tmp_manifest ;
	sed -n $STARTFILES,${ENDFILES}p $MANIFEST >> tmp_manifest ;

	./gdc-client download -m tmp_manifest -t $TOKEN -d $DOWNLOADDIR ;
	
	find $DOWNLOADDIR -name '*.tar.gz' -exec mv -it $FASTQ_Files {} + ;

echo "Files from $STARTFILES to $ENDFILES downloaded" | mailx -s 'Download_Done' user@email ;

	rm -r ${DOWNLOADDIR}/* ;

	find $FASTQ_Files -name '*.tar.gz' -exec tar -xzvf {} \;

	rm ${FASTQ_Files}/* ;

	mv *.fastq $FASTQ_Files ;

	ls -l $FASTQ_Files | awk '{ print $9 }' | sed 1d > samples_file ;

	Rscript quanTIsamples.r ;

	mv quanTIseq_samples.txt $FASTQ_Files ;
	
	rm samples_file ;

	cd FASTQ_Files ;

	bash ${QUANTISEQ}/quanTIseq_pipeline.sh --inputfile="quanTIseq_samples.txt" --prefix="quanTIseq__samples_${STARTFILES}_TO_${ENDFILES}" --threads=8 --outputdir=$OUTPUTDIR ;

	mv quanTIseq_samples.txt quanTIseq_Loop${i}_samples_${STARTFILES}_TO_${ENDFILES}.txt

	mv ${FASTQ_Files}/quanTIseq_Loop${i}_samples_${STARTFILES}_TO_${ENDFILES}.txt $SAMPLESFILES

	rm ./* ; cd ../ ;


echo "QuanTIseq from files $STARTFILES to $ENDFILES done" | mailx -s 'Loop_Done' user@email ;

let "STARTFILES= $STARTFILES + 20"
let "ENDFILES=  $ENDFILES + 20"

done
