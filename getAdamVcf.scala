import org.bdgenomics.adam.rdd.ADAMContext._

//Load the variants from ADAM
val adam6189388 = sc.loadVariants("s3://path/to/file.variants.adam")
//Select the columns to dataframe then write out to csv file
adam6189388.toDF.select($"contigName", $"end", $"referenceAllele", $"alternateAllele").write.csv("adamOut.csv")
//Load the variants from original VCF
val vcf6189388 = sc.textFile("s3://path/to/file.vcf.gz")
val filteredLines = vcf6189388.filter(line => !line.startsWith("#"))
val outVcf6189388 =  filteredLines.map(line => { 
    val l = line.split("\t")
   // List(l(0),  l(1), l(2), l(3), l(4), l(5)).mkString(",")
    List(l(0),  l(1), l(3), l(4)).mkString(",")
    
})
//Write out to csv file
outVcf6189388.toDF.select($"value").write.csv("vcfOut.csv")

// Download both VCF and ADAM file for the next validation. 
// You might need to join the multiple adam files into one.
// For example: cat adamOut1.csv adamOut2.csv ... > adamOut.csv
