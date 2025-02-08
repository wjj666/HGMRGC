library(pheatmap)

setwd('/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/12_novel_species')


df <- read.csv('collinsella_enriched_gene_heatmap_sort.csv', row.names = 1)
species_anno <- read.csv('collinsella_species_anno.csv', row.names = 1)
gene_anno <- read.csv('collinsella_gene_anno.csv', row.names = 1)

tdf <- t(df)

gene_anno$Direction <- ifelse(gene_anno$Direction == "Chinese > Non-Chinese", "Chinese enriched",ifelse(gene_anno$Direction == "Non-Chinese > Chinese", "Non-Chinese enriched", gene_anno$Direction))


#gene_anno$Direction <- factor(gene_anno$Direction, levels = c("Chinese enriched", "Non-Chinese enriched"))
species_anno$Source <- factor(species_anno$Source, levels = c("Chinese Collinsella species", "Non-Chinese Collinsella species"))

annotation_col <- data.frame(Source = species_anno$Source)
rownames(annotation_col) <- rownames(species_anno)

annotation_row <- data.frame(Direction = gene_anno$Direction)
rownames(annotation_row) <- rownames(gene_anno)


annotation_colors <- list(
  Source = c("Chinese Collinsella species" = "#DC0000B2", "Non-Chinese Collinsella species" = "#009E73"),
  #Direction = c("Chinese enriched" = "orange", "Non-Chinese enriched" = "#4DBBD5B2")
)

pheatmap(tdf,
         cluster_rows = FALSE,
         cluster_cols = FALSE,
         show_rownames = TRUE,
         show_colnames = FALSE,
         annotation_col = annotation_col,
         #annotation_row = annotation_row,
         annotation_names_col = FALSE, # 不显示列注释的标题
         annotation_colors = annotation_colors,
         show_legend = TRUE,
         legend = TRUE,
         legend_title = "Gene count",
         annotation_legend = FALSE,
         color = colorRampPalette(c("white", "#8264CC"))(50))


