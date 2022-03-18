library(dplyr)

####################################
# Read coverage of 
####################################

# Load the dataset
original_gene_counts <- read.csv(file = '~/Downloads/Lab-6-Omics/TCGA_BRCA_Gene_ReadCounts.txt', sep = '\t', header = TRUE)

# Remove gene column
original_gene_counts$Gene <- NULL

# Sum the counts for each sample
counts_per_sample <- c(colSums(original_gene_counts))

# Histogram of read coverage
hist(counts_per_sample, col="darkgreen", xlab="Read counts", main="Distribution of read coverage")


######################################
# Read coverage of mean of all samples
######################################

# Load dataset
original_gene_counts <- read.csv(file = '~/Downloads/Lab-6-Omics/TCGA_BRCA_Gene_ReadCounts.txt', sep = '\t', header = TRUE)

# Load dataset for mean calculus
original_gene_counts_without_Gene_name <- read.csv(file = '~/Downloads/Lab-6-Omics/TCGA_BRCA_Gene_ReadCounts.txt', sep = '\t', header = TRUE)
original_gene_counts_without_Gene_name$Gene <- NULL

# Adds mean counts per gene to dataset
original_gene_counts$Mean=rowMeans(original_gene_counts_without_Gene_name)

# Selects Gene and corresponding mean count
mean_counts_per_gene <- select(original_gene_counts, Gene, Mean)

# Sorts the mean counts
sorted_mean_counts_per_gene <- mean_counts_per_gene[order(mean_counts_per_gene$Mean, decreasing = TRUE),]

# Relative cumsum
relative_cumsum <- (cumsum(sorted_mean_counts_per_gene$Mean)/sum(sorted_mean_counts_per_gene$Mean)) * 100

# Plots the relative cumsum
plot(relative_cumsum, type='l', xlab = "Number of genes", ylab = "Relative cumsum (%)")



####################################
# Read coverage of first 10 patients
####################################

library(ggplot2)

# load dataset
original_gene_counts <- read.csv(file = '~/Downloads/Lab-6-Omics/TCGA_BRCA_Gene_ReadCounts.txt', sep = '\t', header = TRUE)

# remove gene name column
original_gene_counts$Gene <- NULL

# select first 10 patients
ten_patient_counts <- original_gene_counts[,1:10]

# sort first 10 patients
ten_patient_counts_sorted <- apply(ten_patient_counts,2,sort,decreasing=T)

# relative cumsum calculus
check<-function(x){ return((cumsum(x)/sum(x))*100) }

# apply relative cumsum 
cumsum_ten_patients <- apply(ten_patient_counts_sorted,2,check)

cumsum_ten_patients <- data.frame(list(cumsum_ten_patients))

# plot the relative cumsum for 10 patients 
ggplot(cumsum_ten_patients, aes(x=as.numeric(row.names(cumsum_ten_patients)))) + 
  geom_line(aes(y = cumsum_ten_patients$TCGA.A1.A0SB.01), color = "cumsum_ten_patients$TCGA.A1.A0SB.01") +
  geom_line(aes(y = cumsum_ten_patients$TCGA.A1.A0SD.01), color = "cumsum_ten_patients$TCGA.A1.A0SD.01") +
  geom_line(aes(y = cumsum_ten_patients$TCGA.A1.A0SE.01), color = "cumsum_ten_patients$TCGA.A1.A0SE.01") +
  geom_line(aes(y = cumsum_ten_patients$TCGA.A1.A0SF.01), color = "cumsum_ten_patients$TCGA.A1.A0SF.01") +
  geom_line(aes(y = cumsum_ten_patients$TCGA.A1.A0SG.01), color = "cumsum_ten_patients$TCGA.A1.A0SG.01") +
  geom_line(aes(y = cumsum_ten_patients$TCGA.A1.A0SH.01), color = "cumsum_ten_patients$TCGA.A1.A0SH.01") +
  geom_line(aes(y = cumsum_ten_patients$TCGA.A1.A0SI.01), color = "blue") +
  geom_line(aes(y = cumsum_ten_patients$TCGA.A1.A0SJ.01), color = "green") +
  geom_line(aes(y = cumsum_ten_patients$TCGA.A1.A0SK.01), color = "white") +
  geom_line(aes(y = cumsum_ten_patients$TCGA.A1.A0SM.01), color = "black") +
  labs(x = "Number of genes", y= "Relative cumsum (%)")




