library(vegan)

species_data <- read.csv("/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/Writing/2_Compare_UHGG/accumulate_curve/highfreq_species_accumulation_curve.csv", row.names = 1)
species_data <- as.matrix(species_data)

# Calculate species accumulation
accumulation_curve <- specaccum(species_data, method = "random")  # You can also use "exact" or "rarefaction"
# Plot the accumulation curve
plot(accumulation_curve, xlab = "Number of Samples", ylab = "Number of common species",
     main = "", col = "blue", lwd = 2,ci=0,ci.type = c("line"))



species_data <- read.csv("/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/Writing/2_Compare_UHGG/accumulate_curve/lowfreq_species_accumulation_curve.csv", row.names = 1)
species_data <- as.matrix(species_data)

# Calculate species accumulation
accumulation_curve <- specaccum(species_data, method = "random")  # You can also use "exact" or "rarefaction"
# Plot the accumulation curve
plot(accumulation_curve, xlab = "Number of Samples", ylab = "Number of rare species",
     main = "", col = "blue", lwd = 2,ci=0,ci.type = c("line"))

