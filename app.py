import streamlit as st
# from analyzer import find_orfs

from analyzer import analyze_sequence, reverse_complement, translate_sequence
from Bio import SeqIO

records = list(SeqIO.parse("gene.fna", "fasta"))

st.write(f"Total sequences found: {len(records)}")

sequence = str(records[0].seq)  # first sequence


st.title("🧬 Gene Sequence Analyzer")

# Upload FASTA
uploaded_file = st.file_uploader("Upload FASTA file", type=["fasta", "fa", "fna"])

sequence = ""

# If file uploaded
if uploaded_file:
    records = list(SeqIO.parse("gene.fna", "fasta"))
    sequence = str(records[0].seq)

# Manual input
else:
    sequence = st.text_area("Enter DNA Sequence")

# Analyze button
if st.button("Analyze"):

    if not sequence:
        st.error("Please enter or upload a sequence")
    else:
        st.write(f"### Length: {len(sequence)} bases")

        st.write("### Preview")
        st.write(sequence[:100] + "...")

        result = analyze_sequence(sequence)
        st.write("### Analysis")
        st.json(result)

        st.write("### Reverse Complement")
        st.write(reverse_complement(sequence)[:100] + "...")

        st.write("### Protein Translation")
        st.write(translate_sequence(sequence)[:100] + "...")


# st.write("### ORFs (Open Reading Frames)")

# orfs = find_orfs(sequence)

# if len(orfs) == 0:
#     st.write("No ORFs found")
# else:
#     st.write(f"Total ORFs found: {len(orfs)}")

#     for i, orf in enumerate(orfs[:5]):  # show first 5
#         st.write(f"ORF {i+1}")
#         st.write(f"Start: {orf['start']} | End: {orf['end']} | Length: {orf['length']}")
#         st.write(orf['sequence'][:60] + "...")
