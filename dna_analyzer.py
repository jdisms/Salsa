#!/usr/bin/env python3
"""
Salsa - Simple DNA Sequence Analyzer
A basic biotechnology tool for DNA sequence analysis
"""

import re
from typing import Dict, List, Any

class DNAAnalyzer:
    """A simple DNA sequence analyzer for biotechnology applications"""
    
    def __init__(self):
        self.valid_bases = set('ATCG')
        self.codon_table = {
            'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
            'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
            'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
            'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
            'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
            'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
            'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
            'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
            'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
            'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
            'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
            'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
        }
    
    def validate_sequence(self, sequence: str) -> bool:
        """Validate if the sequence contains only valid DNA bases"""
        return set(sequence.upper()) <= self.valid_bases
    
    def clean_sequence(self, sequence: str) -> str:
        """Clean and normalize DNA sequence"""
        # Remove whitespace and convert to uppercase
        cleaned = re.sub(r'\s+', '', sequence.upper())
        
        # Remove non-DNA characters
        cleaned = re.sub(r'[^ATCG]', '', cleaned)
        
        return cleaned
    
    def analyze_composition(self, sequence: str) -> Dict[str, Any]:
        """Analyze the composition of a DNA sequence"""
        sequence = self.clean_sequence(sequence)
        
        if not sequence:
            return {'error': 'Empty or invalid sequence'}
        
        length = len(sequence)
        composition = {
            'A': sequence.count('A'),
            'T': sequence.count('T'),
            'C': sequence.count('C'),
            'G': sequence.count('G')
        }
        
        gc_content = (composition['G'] + composition['C']) / length * 100
        at_content = (composition['A'] + composition['T']) / length * 100
        
        return {
            'length': length,
            'composition': composition,
            'gc_content': round(gc_content, 2),
            'at_content': round(at_content, 2),
            'valid': self.validate_sequence(sequence)
        }
    
    def reverse_complement(self, sequence: str) -> str:
        """Generate the reverse complement of a DNA sequence"""
        sequence = self.clean_sequence(sequence)
        complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        
        complement = ''.join(complement_map[base] for base in sequence)
        return complement[::-1]  # Reverse the complement
    
    def translate_to_protein(self, sequence: str, frame: int = 1) -> str:
        """Translate DNA sequence to protein in the specified reading frame"""
        sequence = self.clean_sequence(sequence)
        
        if frame not in [1, 2, 3]:
            raise ValueError("Frame must be 1, 2, or 3")
        
        # Adjust for reading frame (0-indexed)
        start_pos = frame - 1
        sequence = sequence[start_pos:]
        
        # Translate codons to amino acids
        protein = []
        for i in range(0, len(sequence) - 2, 3):
            codon = sequence[i:i+3]
            if len(codon) == 3:
                amino_acid = self.codon_table.get(codon, 'X')
                protein.append(amino_acid)
                
                # Stop at stop codon
                if amino_acid == '*':
                    break
        
        return ''.join(protein)
    
    def find_orfs(self, sequence: str, min_length: int = 30) -> List[Dict[str, Any]]:
        """Find Open Reading Frames (ORFs) in the DNA sequence"""
        sequence = self.clean_sequence(sequence)
        orfs = []
        
        # Check all three reading frames
        for frame in [1, 2, 3]:
            start_pos = frame - 1
            frame_sequence = sequence[start_pos:]
            
            # Find start codons (ATG)
            for i in range(0, len(frame_sequence) - 2, 3):
                codon = frame_sequence[i:i+3]
                if codon == 'ATG':
                    # Look for stop codon
                    for j in range(i + 3, len(frame_sequence) - 2, 3):
                        stop_codon = frame_sequence[j:j+3]
                        if stop_codon in ['TAA', 'TAG', 'TGA']:
                            orf_length = j - i + 3
                            if orf_length >= min_length:
                                orf_sequence = frame_sequence[i:j+3]
                                protein = self.translate_to_protein(orf_sequence)
                                
                                orfs.append({
                                    'frame': frame,
                                    'start': start_pos + i + 1,  # 1-indexed
                                    'end': start_pos + j + 3,    # 1-indexed
                                    'length': orf_length,
                                    'dna_sequence': orf_sequence,
                                    'protein_sequence': protein
                                })
                            break
        
        return orfs


def main():
    """Example usage of the DNA Analyzer"""
    analyzer = DNAAnalyzer()
    
    # Example DNA sequence
    sample_sequence = """
    ATGAAATTTGCAGCAATCTGCAAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGC
    AAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGC
    AAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGC
    AAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGC
    AAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGC
    AAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGC
    AAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGC
    AAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGC
    AAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGC
    AAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTGCAAGAAATGCAAGCAATCTAG
    """
    
    print("🧬 Salsa DNA Sequence Analyzer")
    print("=" * 40)
    
    # Analyze composition
    print("\n📊 Sequence Composition Analysis:")
    composition = analyzer.analyze_composition(sample_sequence)
    print(f"Length: {composition['length']} bp")
    print(f"A: {composition['composition']['A']}")
    print(f"T: {composition['composition']['T']}")
    print(f"C: {composition['composition']['C']}")
    print(f"G: {composition['composition']['G']}")
    print(f"GC Content: {composition['gc_content']}%")
    print(f"AT Content: {composition['at_content']}%")
    
    # Reverse complement
    print("\n🔄 Reverse Complement:")
    rev_comp = analyzer.reverse_complement(sample_sequence)
    print(f"Original: {analyzer.clean_sequence(sample_sequence)[:50]}...")
    print(f"Rev Comp: {rev_comp[:50]}...")
    
    # Protein translation
    print("\n🧪 Protein Translation (Frame 1):")
    protein = analyzer.translate_to_protein(sample_sequence, frame=1)
    print(f"Protein: {protein}")
    
    # Find ORFs
    print("\n🔍 Open Reading Frames:")
    orfs = analyzer.find_orfs(sample_sequence)
    for i, orf in enumerate(orfs, 1):
        print(f"ORF {i}: Position {orf['start']}-{orf['end']} (Frame {orf['frame']})")
        print(f"  Length: {orf['length']} bp")
        print(f"  Protein: {orf['protein_sequence']}")
        print()


if __name__ == "__main__":
    main()