# Early-Human-Admixture
Re-creation of a Nobel Prize winning analysis to detect admixture between early humans, Neanderthals, and Denisovans. Mixture is determined by calculating the D-statistic.

The D-statistic is found using abba baba methods. The humanGeno dataset is split into five datasets in order to find the jackknife mean and standard error.

Both files that start with 'project4' are essentially the same. One is in a jupyter notebook format (preferred) and one is in a typical python format. Neither will run if they are not in the same directory as the input file 'humanGeno.txt'

humanGeno.txt contains several columns and around 100,000 rows. The first column represents a position on a chromosome. The following columns represent whether each species has a matching nucleotide at that chromosome, '0', a differing nucleotide '2', or missing information, 'NA'.
