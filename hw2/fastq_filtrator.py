# This function returns GC-content of sequence in percents
def gc_content(read_seq):
    return sum(map(read_seq.upper().count, ['G','C'])) / len(read_seq.strip()) * 100

# This function checks whether GC-content of sequence is in bounds 
def gc_filter(read_seq, gc_bounds):
    if isinstance(gc_bounds, (tuple, list)):
        min_gc, max_gc = gc_bounds
    else:    # Only upper bound is given
        min_gc = 0
        max_gc = gc_bounds
    if gc_content(read_seq) >= min_gc and gc_content(read_seq) <= max_gc:    # GC-content is in bounds
        return 'Pass'
    else:
        return 'Fail'

# This function returns length of sequence
def length(read_seq):
    return len(read_seq.strip())
    
# This function checks whether length of sequence is in bounds 
def len_filter(read_seq, length_bounds):
    if isinstance(length_bounds, (tuple, list)):
        min_len, max_len = length_bounds
    else:    # Only upper bound is given
        min_len = 0
        max_len = length_bounds
    if length(read_seq) >= min_len and length(read_seq) <= max_len:    # Length is in bounds
        return 'Pass'
    else:
        return 'Fail'
    
# This function returns mean q-score of sequence
def mean_q_score(read_qual):
    sum_of_q_scores = 0
    for symbol in read_qual.strip():
        sum_of_q_scores += ord(symbol) - 33
    return sum_of_q_scores / len(read_qual.strip())

# This function checks whether mean q-score of sequence is not less than quality_threshold  
def qual_filter(read_qual, quality_threshold):        
    if mean_q_score(read_qual) >= quality_threshold:
        return 'Pass'
    else:
        return 'Fail'

# This function adds read to output '_passed.fastq' file 
def add_read_to_passed(
        read_header, read_seq,
        read_plus_str, read_qual,
        output_file_prefix):
    with open(output_file_prefix + '_passed.fastq', 'a') as file:
        file.writelines([read_header, read_seq, read_plus_str, read_qual])

# This function adds read to output '_failed.fastq' file 
def add_read_to_failed(
        read_header, read_seq,
        read_plus_str, read_qual,
        output_file_prefix):
    with open(output_file_prefix + '_failed.fastq', 'a') as file:
        file.writelines([read_header, read_seq, read_plus_str, read_qual])
    

    
def main(input_fastq, output_file_prefix, gc_bounds=(0, 100),
         length_bounds=(0, 2**32), quality_threshold=0, save_filtered=False):
    
    # Creating empty output files for passed and filtered reads
    # If file already exists, it becomes empty           
    with open(output_file_prefix + '_passed.fastq', 'w') as file:
        pass
    with open(output_file_prefix + '_failed.fastq', 'w') as file:
        pass
    # Reading input fastq file line by line 
    with open(input_fastq, 'r') as file:
        while True:
            read_header = file.readline()     ## I'm not stripping '\n' here consciously
            read_seq = file.readline()        ## for convenient appending to output files.
            read_plus_str = file.readline()   ## I'm going to take '\n' into account 
            read_qual = file.readline()       ## when I'll be counting length of these strings.
            if read_header == '' or read_header == '\n':    # Reached the end of input file, stop reading
                break                            
            # Checking read
            if (gc_filter(read_seq, gc_bounds) == 'Pass' and
                len_filter(read_seq, length_bounds) == 'Pass' and
                qual_filter(read_qual, quality_threshold) == 'Pass'):
            # Appending read to output files 
                add_read_to_passed(read_header, read_seq,
                                   read_plus_str, read_qual,
                                   output_file_prefix)
            else: 
                if save_filtered == True:
                    add_read_to_failed(read_header, read_seq,
                                       read_plus_str, read_qual,
                                       output_file_prefix)

