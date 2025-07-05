"""
Simple Flask web application for DNA sequence analysis
This demonstrates how to create web-based biotechnology tools
"""

from flask import Flask, render_template, request, jsonify
import json
from dna_analyzer import DNAAnalyzer

app = Flask(__name__)
analyzer = DNAAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_sequence():
    """Analyze DNA sequence and return results"""
    try:
        data = request.get_json()
        sequence = data.get('sequence', '')
        
        if not sequence:
            return jsonify({'error': 'No sequence provided'}), 400
        
        # Perform various analyses
        composition = analyzer.analyze_composition(sequence)
        
        # Get reverse complement
        reverse_complement = analyzer.reverse_complement(sequence)
        
        # Translate to protein (frame 1)
        protein = analyzer.translate_to_protein(sequence, frame=1)
        
        # Find ORFs
        orfs = analyzer.find_orfs(sequence)
        
        # Prepare results
        results = {
            'composition': composition,
            'reverse_complement': reverse_complement,
            'protein_translation': protein,
            'orfs': orfs,
            'status': 'success'
        }
        
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'Salsa DNA Analyzer'})

if __name__ == '__main__':
    # Create templates directory and file
    import os
    templates_dir = 'templates'
    if not os.path.exists(templates_dir):
        os.makedirs(templates_dir)
    
    # Create simple HTML template
    html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Salsa DNA Analyzer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        .input-section {
            margin-bottom: 30px;
        }
        label {
            display: block;
            margin-bottom: 10px;
            font-weight: bold;
            color: #34495e;
        }
        textarea {
            width: 100%;
            height: 150px;
            padding: 10px;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-family: monospace;
            font-size: 14px;
            resize: vertical;
        }
        button {
            background: #3498db;
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background 0.3s;
        }
        button:hover {
            background: #2980b9;
        }
        button:disabled {
            background: #bdc3c7;
            cursor: not-allowed;
        }
        .results {
            margin-top: 30px;
            padding: 20px;
            background: #ecf0f1;
            border-radius: 5px;
            display: none;
        }
        .result-section {
            margin-bottom: 20px;
            padding: 15px;
            background: white;
            border-radius: 5px;
            border-left: 4px solid #3498db;
        }
        .result-section h3 {
            margin-top: 0;
            color: #2c3e50;
        }
        .sequence-display {
            font-family: monospace;
            background: #2c3e50;
            color: #ecf0f1;
            padding: 10px;
            border-radius: 3px;
            word-break: break-all;
            font-size: 12px;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 15px 0;
        }
        .stat-item {
            background: #3498db;
            color: white;
            padding: 15px;
            border-radius: 5px;
            text-align: center;
        }
        .stat-value {
            font-size: 24px;
            font-weight: bold;
        }
        .stat-label {
            font-size: 14px;
            opacity: 0.9;
        }
        .orf-item {
            background: #e8f5e8;
            padding: 10px;
            margin: 10px 0;
            border-radius: 3px;
            border-left: 3px solid #27ae60;
        }
        .loading {
            text-align: center;
            color: #7f8c8d;
        }
        .error {
            color: #e74c3c;
            background: #fdf2f2;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #e74c3c;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🧬 Salsa DNA Sequence Analyzer</h1>
        
        <div class="input-section">
            <label for="sequence">Enter DNA Sequence:</label>
            <textarea id="sequence" placeholder="Enter your DNA sequence here (A, T, G, C only)...
Example: ATGCGATCGATCGATCGATCGATCGATCGATCGATCGTAG"></textarea>
            <button onclick="analyzeSequence()" id="analyzeBtn">Analyze Sequence</button>
        </div>
        
        <div id="results" class="results">
            <div id="loading" class="loading" style="display: none;">
                <p>🔬 Analyzing sequence...</p>
            </div>
            <div id="analysis-results"></div>
        </div>
    </div>

    <script>
        async function analyzeSequence() {
            const sequence = document.getElementById('sequence').value.trim();
            const resultsDiv = document.getElementById('results');
            const loadingDiv = document.getElementById('loading');
            const analysisResults = document.getElementById('analysis-results');
            const analyzeBtn = document.getElementById('analyzeBtn');
            
            if (!sequence) {
                alert('Please enter a DNA sequence');
                return;
            }
            
            // Show loading
            resultsDiv.style.display = 'block';
            loadingDiv.style.display = 'block';
            analysisResults.innerHTML = '';
            analyzeBtn.disabled = true;
            
            try {
                const response = await fetch('/analyze', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ sequence: sequence })
                });
                
                const data = await response.json();
                
                if (data.error) {
                    throw new Error(data.error);
                }
                
                displayResults(data);
                
            } catch (error) {
                analysisResults.innerHTML = `<div class="error">Error: ${error.message}</div>`;
            } finally {
                loadingDiv.style.display = 'none';
                analyzeBtn.disabled = false;
            }
        }
        
        function displayResults(data) {
            const analysisResults = document.getElementById('analysis-results');
            
            let html = '';
            
            // Composition Analysis
            if (data.composition) {
                const comp = data.composition;
                html += `
                    <div class="result-section">
                        <h3>📊 Sequence Composition</h3>
                        <div class="stats-grid">
                            <div class="stat-item">
                                <div class="stat-value">${comp.length}</div>
                                <div class="stat-label">Length (bp)</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value">${comp.gc_content}%</div>
                                <div class="stat-label">GC Content</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value">${comp.at_content}%</div>
                                <div class="stat-label">AT Content</div>
                            </div>
                        </div>
                        <div class="stats-grid">
                            <div class="stat-item">
                                <div class="stat-value">${comp.composition.A}</div>
                                <div class="stat-label">A Count</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value">${comp.composition.T}</div>
                                <div class="stat-label">T Count</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value">${comp.composition.G}</div>
                                <div class="stat-label">G Count</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value">${comp.composition.C}</div>
                                <div class="stat-label">C Count</div>
                            </div>
                        </div>
                    </div>
                `;
            }
            
            // Reverse Complement
            if (data.reverse_complement) {
                html += `
                    <div class="result-section">
                        <h3>🔄 Reverse Complement</h3>
                        <div class="sequence-display">${data.reverse_complement}</div>
                    </div>
                `;
            }
            
            // Protein Translation
            if (data.protein_translation) {
                html += `
                    <div class="result-section">
                        <h3>🧪 Protein Translation (Frame 1)</h3>
                        <div class="sequence-display">${data.protein_translation}</div>
                    </div>
                `;
            }
            
            // ORFs
            if (data.orfs && data.orfs.length > 0) {
                html += `
                    <div class="result-section">
                        <h3>🔍 Open Reading Frames (ORFs)</h3>
                `;
                
                data.orfs.forEach((orf, index) => {
                    html += `
                        <div class="orf-item">
                            <strong>ORF ${index + 1}:</strong> Position ${orf.start}-${orf.end} (Frame ${orf.frame})<br>
                            <strong>Length:</strong> ${orf.length} bp<br>
                            <strong>Protein:</strong> <span style="font-family: monospace;">${orf.protein_sequence}</span>
                        </div>
                    `;
                });
                
                html += `</div>`;
            }
            
            analysisResults.innerHTML = html;
        }
        
        // Allow Enter key to trigger analysis
        document.getElementById('sequence').addEventListener('keypress', function(e) {
            if (e.key === 'Enter' && e.ctrlKey) {
                analyzeSequence();
            }
        });
    </script>
</body>
</html>
    '''
    
    with open(os.path.join(templates_dir, 'index.html'), 'w') as f:
        f.write(html_template)
    
    print("🧬 Starting Salsa DNA Analyzer Web Application...")
    print("📡 Server will be available at: http://localhost:5000")
    print("🔬 Ready to analyze DNA sequences!")
    
    app.run(debug=True, host='0.0.0.0', port=5000)