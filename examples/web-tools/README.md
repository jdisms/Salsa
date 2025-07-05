# Web Tools Examples

This directory contains examples for web-based biotechnology applications.

## Example Projects

### Sequence Analysis Web App
- Upload and analyze DNA/RNA sequences
- Real-time sequence translation
- Interactive sequence visualization
- Export results in multiple formats

### Data Visualization Dashboard
- Interactive charts for experimental data
- Real-time lab monitoring
- Collaborative data sharing
- Custom report generation

### Laboratory Portal
- Sample submission system
- Results delivery platform
- Protocol sharing community
- Equipment booking system

## Getting Started

### HTML/CSS/JavaScript Example
```html
<!DOCTYPE html>
<html>
<head>
    <title>DNA Sequence Analyzer</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .input-section { margin: 20px 0; }
        .results { background: #f5f5f5; padding: 15px; border-radius: 5px; }
        textarea { width: 100%; height: 100px; }
        button { background: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 3px; }
    </style>
</head>
<body>
    <h1>DNA Sequence Analyzer</h1>
    
    <div class="input-section">
        <label>Enter DNA Sequence:</label>
        <textarea id="sequence" placeholder="Enter DNA sequence (A, T, G, C)"></textarea>
        <button onclick="analyzeSequence()">Analyze</button>
    </div>
    
    <div id="results" class="results" style="display: none;"></div>
    
    <script>
        function analyzeSequence() {
            const sequence = document.getElementById('sequence').value.toUpperCase();
            const resultsDiv = document.getElementById('results');
            
            if (!sequence) {
                alert('Please enter a DNA sequence');
                return;
            }
            
            // Calculate GC content
            const gcCount = (sequence.match(/[GC]/g) || []).length;
            const gcContent = (gcCount / sequence.length * 100).toFixed(2);
            
            // Display results
            resultsDiv.innerHTML = `
                <h3>Analysis Results</h3>
                <p><strong>Sequence Length:</strong> ${sequence.length} base pairs</p>
                <p><strong>GC Content:</strong> ${gcContent}%</p>
                <p><strong>A Count:</strong> ${(sequence.match(/A/g) || []).length}</p>
                <p><strong>T Count:</strong> ${(sequence.match(/T/g) || []).length}</p>
                <p><strong>G Count:</strong> ${(sequence.match(/G/g) || []).length}</p>
                <p><strong>C Count:</strong> ${(sequence.match(/C/g) || []).length}</p>
            `;
            resultsDiv.style.display = 'block';
        }
    </script>
</body>
</html>
```

### Node.js/Express Backend Example
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.static('public'));

// Analyze DNA sequence endpoint
app.post('/analyze', (req, res) => {
    const { sequence } = req.body;
    
    if (!sequence) {
        return res.status(400).json({ error: 'Sequence is required' });
    }
    
    const analysis = {
        length: sequence.length,
        gcContent: ((sequence.match(/[GC]/gi) || []).length / sequence.length * 100).toFixed(2),
        composition: {
            A: (sequence.match(/A/gi) || []).length,
            T: (sequence.match(/T/gi) || []).length,
            G: (sequence.match(/G/gi) || []).length,
            C: (sequence.match(/C/gi) || []).length
        }
    };
    
    res.json(analysis);
});

app.listen(port, () => {
    console.log(`Biotechnology web app listening at http://localhost:${port}`);
});
```

## Technology Stack Suggestions
- **Frontend**: React, Vue.js, Angular, or vanilla JavaScript
- **Backend**: Node.js/Express, Python/Flask, or Python/Django
- **Database**: MongoDB, PostgreSQL, or MySQL
- **Visualization**: D3.js, Chart.js, or Plotly.js
- **Deployment**: Heroku, Vercel, or AWS