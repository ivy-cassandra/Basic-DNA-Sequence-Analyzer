import matplotlib.pyplot as plt


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


def gc_content_window(seq, window_size=50):
    gc_values = []
    positions = []
    for i in range(0, len(seq) - window_size + 1, window_size):
        window = seq[i:i+window_size]
        gc = (window.count('G') + window.count('C')) / window_size * 100
        gc_values.append(gc)
        positions.append(i + window_size // 2)  # center of window
    return positions, gc_values

def plot_gc_content(positions, gc_values):
    plt.figure(figsize=(10, 5))
    plt.plot(positions, gc_values, marker='o', linestyle='-', color='blue')
    plt.title("GC Content Across Sequence")
    plt.xlabel("Position (bp)")
    plt.ylabel("GC Content (%)")
    plt.grid(True)
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()


dna_seq = read_fasta("sequence.fasta")
print(dna_seq)

freq = nucleotide_frequency(dna_seq)
print(freq)

gc = gc_content(dna_seq)
print(gc)

rev_comp = reverse_complement(dna_seq)
print(rev_comp)

positions, gc_values = gc_content_window(dna_seq, window_size=10)
plot_gc_content(positions, gc_values)