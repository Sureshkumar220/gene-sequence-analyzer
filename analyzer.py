from Bio.Seq import Seq

def clean_sequence(seq):
    seq = seq.replace("\n", "").upper()
    valid = set("ATGC")
    return "".join([base for base in seq if base in valid])


def analyze_sequence(seq):
    seq = clean_sequence(seq)
    length = len(seq)

    if length == 0:
        return {"Error": "Invalid sequence"}

    gc = (seq.count('G') + seq.count('C')) / length * 100

    return {
        "Length": length,
        "GC_Content (%)": round(gc, 2),
        "A": seq.count('A'),
        "T": seq.count('T'),
        "G": seq.count('G'),
        "C": seq.count('C')
    }


def reverse_complement(seq):
    seq = clean_sequence(seq)
    return str(Seq(seq).reverse_complement())


def translate_sequence(seq):
    seq = clean_sequence(seq)
    return str(Seq(seq).translate())

#ORF finder

# def find_orfs(seq):
#     seq = seq.upper()
#     start_codon = "ATG"
#     stop_codons = ["TAA", "TAG", "TGA"]

#     orfs = []

#     for frame in range(3):  # 3 reading frames
#         for i in range(frame, len(seq) - 2, 3):
#             codon = seq[i:i+3]

#             if codon == start_codon:
#                 for j in range(i, len(seq) - 2, 3):
#                     stop = seq[j:j+3]

#                     if stop in stop_codons:
#                         orf_seq = seq[i:j+3]
#                         orfs.append({
#                             "start": i,
#                             "end": j+3,
#                             "length": len(orf_seq),
#                             "sequence": orf_seq
#                         })
#                         break

#     return orfs
