# Bioinformatics Examples

This directory contains examples for bioinformatics applications.

## Example Projects

### DNA Sequence Analyzer
- Analyze DNA sequences for patterns
- Calculate GC content
- Find open reading frames (ORFs)
- Translate DNA to protein sequences

### Protein Structure Tools
- Parse PDB files
- Analyze protein secondary structure
- Calculate molecular properties

### Phylogenetic Analysis
- Build evolutionary trees
- Sequence alignment tools
- Distance matrix calculations

## Getting Started

```python
# Example: Simple DNA analysis
def gc_content(dna_sequence):
    """Calculate GC content of DNA sequence"""
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    return (gc_count / len(dna_sequence)) * 100

# Example usage
sequence = "ATCGATCGATCG"
print(f"GC Content: {gc_content(sequence):.2f}%")
```

## Required Libraries
- BioPython: `pip install biopython`
- NumPy: `pip install numpy`
- Pandas: `pip install pandas`