#!/bin/bash

# Salsa Biotechnology Project Setup Script
# This script helps you set up your development environment for biotechnology projects

echo "🧬 Welcome to Salsa Biotechnology Repository Setup!"
echo "================================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    echo "   Visit: https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip is not installed. Please install pip."
    exit 1
fi

echo "✅ pip found: $(pip3 --version)"

# Create virtual environment
echo ""
echo "🔧 Setting up virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install basic requirements
echo ""
echo "📦 Installing basic requirements..."
pip install numpy pandas matplotlib seaborn scipy biopython flask plotly jupyter pytest

echo ""
echo "🎉 Setup complete! Here's what you can do next:"
echo ""
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Try the sample DNA analyzer:"
echo "   python3 dna_analyzer.py"
echo ""
echo "3. Start a Jupyter notebook:"
echo "   jupyter notebook"
echo ""
echo "4. Explore the examples directory:"
echo "   ls examples/"
echo ""
echo "5. Install additional packages as needed:"
echo "   pip install -r requirements.txt"
echo ""
echo "🔬 Happy biotechnology coding!"