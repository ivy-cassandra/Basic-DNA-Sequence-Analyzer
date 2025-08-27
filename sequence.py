def read_fasta(file_path):
    sequence = ""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if not line.startswith('>'):
            sequence += ''.join(line.strip())
    return sequence.upper()


def nucleotide_frequency(seq):
    return {
        'A': seq.count('A'),
        'C': seq.count('C'),
        'T': seq.count('T'),
        'G': seq.count('G')
    }


def gc_content(seq):
    g = seq.count('G')
    c = seq.count('C')
    gc = (g + c) / len(seq) * 100
    return round(gc,2)


def reverse_complement(seq):
    rev_comp = ""
    complement = {
        'A': 'T',
        'C': 'G',
        'T': 'A',
        'G': 'C'
    }
    for base in reversed(seq):
        rev_comp += ''.join(complement[base])
    return rev_comp


dna_seq = read_fasta("sequence.fasta")
print(dna_seq)

freq = nucleotide_frequency(dna_seq)
print(freq)

gc = gc_content(dna_seq)
print(gc)

rev_comp = reverse_complement(dna_seq)
print(rev_comp)