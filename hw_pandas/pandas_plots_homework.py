import pandas as pd
import re
import matplotlib as plt

# Function for reading gff files
def read_gff(path_to_gff):
    gff_header = ['chromosome', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes']
    return pd.read_csv(path_to_gff, sep='\t', names=gff_header, comment = '#')

# Function for reading bed files
def read_bed(path_to_bed):
    bed_header = ['chromosome', 'start', 'end', 'name', 'score', 'strand']
    return pd.read_csv(path_to_bed, sep='\t', names=bed_header)

# Creating dataframes from our input files
rrna_gff_df = read_gff('data/rrna_annotation.gff')
alignment_bed_df = read_bed('data/alignment.bed')

# Extracting rRNA type from attributes column
rrna_gff_df['attributes'] = rrna_gff_df['attributes'].apply(lambda attribute: re.split('=|_', attribute)[1])

# Counting rRNAs for every chromosome
rrnas_by_types = pd.DataFrame({'count' : rrna_gff_df.groupby(['chromosome','attributes']).size()}).reset_index()

# Merging gff and bed files
merged_df = pd.merge(rrna_gff_df, alignment_bed_df, how='outer', left_on=['chromosome'], right_on=['chromosome'])

# Creating barplot
fig = plt.figure()
sns.barplot(x='chromosome', y='count', hue='attributes', data=rrnas_by_types)
plt.legend(title='rRNA type', loc='upper left')
plt.xlabel('chromosome', size=10)
plt.ylabel('count', size=10)
plt.xticks(rotation=90, size=10);

# Extracting rRNAs which intersect with alignment
rrnas_align_intersect = merged_df[(merged_df['start_x'] >= merged_df['start_y']) & (merged_df['end_x'] <= merged_df['end_y'])]
rrnas_align_intersect.drop_duplicates()