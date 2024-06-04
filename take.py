import sys
from Bio import SeqIO

def filter_fasta(input_fasta, search_string, output_fasta):
    with open(input_fasta, "r") as input_handle, open(output_fasta, "w") as output_handle:
        for record in SeqIO.parse(input_handle, "fasta"):
            if search_string in record.description:
                SeqIO.write(record, output_handle, "fasta")
    print(f"Filtered sequences containing '{search_string}' have been saved to {output_fasta}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python filter_fasta.py <input_fasta> <search_string> <output_fasta>")
        sys.exit(1)

    input_fasta = sys.argv[1]
    search_string = sys.argv[2]
    output_fasta = sys.argv[3]

    filter_fasta(input_fasta, search_string, output_fasta)
