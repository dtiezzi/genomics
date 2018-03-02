samples <- read.delim("samples_file", header= FALSE)
library(stringr)

ids_list= list()
fastq1_list= list()
fastq2_list= list()
for (i in seq(1, nrow(samples) - 1, 2)) {
	id <- str_sub(samples[i ,1],1, -9)
	ids_list[[paste0(i)]] <- id
	fastq1 <- samples[i ,1]
	fastq1_list[[paste0(i)]] <- fastq1
	fastq2 <- samples[i+1 ,1]
	fastq2_list[[paste0(i)]] <- fastq2
} 

df <- data.frame(Ids= unlist(ids_list),
                 fastq1= unlist(fastq1_list), 
                 fastq2= unlist(fastq2_list))
write.table(df, file= "quanTIseq_samples.txt",sep= "\t" ,row.names= FALSE, col.names= FALSE, quote= FALSE)
