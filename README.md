# Analysis of Human Gut Microbiome Reference Genome Catalog (HGMRGC) and microbial differences between the Han Chinese and non-Chinese populations

## scripts/
* `hgmrgc_sample_geo_distribution.py`: Plot the geographic distribution of metagenomic samples collected from 22 countries and 29 provinces or regions across the mainland China.

* `hgmrgc_lowest_taxonomic_level.py`: Plot the number of representative genomes annotated at the lowest taxonomic levels in HGMRGC and UHGG. 

* `hgmrgc_compare_catalog_stats.py`: Compare the completeness, contamination, N50, length of the representative genomes in HGMRGC and UHGG.

* `hgmrgc_compare_cluster_size.py`: Compare the genome cluster size in HGMRGC and UHGG.

* `hgmrgc_compare_mapping_rate.py`: Compare the read mapping rates for 200 external metagenomic sequencing samples.

* `hgmrgc_phylum.py`: Plot the proportion of HGMRGC representative genomes, categorized by phylum.

* `hgmrgc_phylum_quality.py`: Plot the proportion of high-quality and medium-quality HGMRGC representative genomes in each phylum.

* `hgmrgc_phylogenetic_diversity.py`: The phylogenetic diversity of each phylum in HGMRGC.

* `collinsella_enriched_gene_heatmap.r`: Plot the heatmap of the gene expression across the 238 novel representative genomes from the Collinsella genus. 

* `prevalence_species_distribution.py`: Plot the distribution of annotated families for the 126 population-specific prevalent genomes. 

* `prevalence_sig_gene.py`: Plot the KEGG modules for genes show significant differences in gene frequency between HC-PSPGs and NC-PSPGs. 

* `microbial_variance_explained.py`: Plot the variance explained by geography, age, sex and BMI based on microbial abundance and SNP in the discovery and replication cohorts.

* `beta_diversity.py`: Compare the abundance-based beta diversity and SNP-based beta diversity within HC population, within NC population and between HC and NC populations. 

* `alpha_diversity_species_distribution.py`: Plot the distribution of annotated families for the 90 representative genomes with significant differences in SNP-based alpha diversity.

* `alpha_diversity.py`: Compare the abundance-based, SNP-based, and SV-based alpha diversity between the HC and NC populations.



## phylogenetic_trees/
* `bacterial_5740/`: Annotation files for the maximum-likelihood phylogenetic tree comprising 5,740 representative genomes from bacteria.

* `novel_238/`: Annotation files for the maximum-likelihood phylogenetic tree comprising 238 novel representative genomes from the Collinsella genus.

* `prevence_126/`: Annotation files for the maximum-likelihood phylogenetic tree comprising 126 population-specific prevalent genomes.

* `variance_explained_27/`: Annotation files for the maximum-likelihood phylogenetic tree for 27 genomes that geography can explain more variance (≥ 5%) than the other factors.

* `fst_86/`: Annotation files for the maximum-likelihood phylogenetic tree comprising the 86 eligible representative genomes for the analysis of selection pressure between the HC and NC populations. 

* `alpha_90/: Annotation files for the maximum-likelihood phylogenetic tree comprising the 90 representative genomes with significant differences in SNP-based alpha diversity in both discovery and replication cohorts. 

## data/
All data used in `scripts/`.



