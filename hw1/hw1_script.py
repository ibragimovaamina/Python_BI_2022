# This function checks whether input sequence is valid. If so, decides whether it's DNA or RNA
def check(seq):
    if {'t', 'u'} <= set(seq.lower()):
        return 'Invalid' #contains T and U simultaneously
    elif set(seq.lower()).issubset({'a', 'c', 'g', 't', 'u'}) == False:
        return 'Invalid' #contains symbols besides nucleobases
    elif 'u' in seq.lower():
        return 'RNA' 
    else:
        return 'DNA'

# This function returns transcribed sequence for DNA
def transcribe(seq):
    t_nucl = 'Tt'
    u_nucl = 'Uu'
    transcribe_table = seq.maketrans(t_nucl, u_nucl)
    return seq.translate(transcribe_table)
    
# This function returns reversed sequence for DNA or RNA
def reverse(seq):
    return seq[::-1]

# This function makes complementary sequence for DNA
def dna_complement(seq):
    dna_nucl_ref = 'ACGTacgt'
    dna_nucl_compl = 'TGCAtgca'
    complement_table = seq.maketrans(dna_nucl_ref, dna_nucl_compl)
    return seq.translate(complement_table)

# This function makes complementary sequence for RNA
def rna_complement(seq):
    rna_nucl_ref = 'ACGUacgu'
    rna_nucl_compl = 'UGCAugca'
    complement_table = seq.maketrans(rna_nucl_ref, rna_nucl_compl)
    return seq.translate(complement_table)

    
while True:
    command = input('Enter command: ')
    if command.lower() == 'exit':
        print('Good luck!')
        break
    elif command.lower() == 'transcribe':
        while True:
            seq = input('Enter sequence: ')
            if check(seq) == 'Invalid':
                print('Invalid sequence. Try again!')
            elif check(seq) == 'RNA':
                print('Input sequence is RNA. DNA is expected. Try again!')
            else:
                print(transcribe(seq))
                break
    elif command.lower() == 'reverse':
        while True:
            seq = input('Enter sequence: ')
            if check(seq) == 'Invalid':
                print('Invalid sequence. Try again!')
            else:
                print(reverse(seq))
                break
    elif command.lower() == 'complement':
        while True:
            seq = input('Enter sequence: ')
            if check(seq) == 'Invalid':
                print('Invalid sequence. Try again!')
            elif check(seq) == 'RNA':
                print(rna_complement(seq))
                break
            else:
                print(dna_complement(seq))
                break
    elif command.lower() == 'reverse complement':
        while True:
            seq = input('Enter sequence: ')
            if check(seq) == 'Invalid':
                print('Invalid sequence. Try again!')
            elif check(seq) == 'RNA':
                print(rna_complement(reverse(seq)))
                break
            else:
                print(dna_complement(reverse(seq)))
                break
    else:
        print('Unknown command!')   
