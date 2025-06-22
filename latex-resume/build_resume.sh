#!/bin/bash

# Build script for YAML-based LaTeX resume
# This script converts YAML data to LaTeX and compiles the PDF

set -e

# Configuration
YAML_FILE="resume_data.yaml"
PERSONAL_INFO_FILE="resume_content.tex"
SECTIONS_FILE="resume_sections.tex"
TEMPLATE_FILE="main_template.tex"
OUTPUT_FILE="main.tex"
PDF_OUTPUT="resume.pdf"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    exit 1
fi

# Check if PyYAML is installed
if ! python3 -c "import yaml" 2>/dev/null; then
    echo "Installing PyYAML..."
    pip3 install PyYAML
fi

# Generate LaTeX content from YAML
echo "Converting YAML to LaTeX..."
python3 yaml_to_latex.py "$YAML_FILE" --personal-info "$PERSONAL_INFO_FILE" --sections "$SECTIONS_FILE"

if [ ! -f "$PERSONAL_INFO_FILE" ] || [ ! -f "$SECTIONS_FILE" ]; then
    echo "Error: Failed to generate LaTeX content from YAML"
    exit 1
fi

# Create the main LaTeX file by combining template and generated content
echo "Creating main LaTeX file..."
cp "$TEMPLATE_FILE" "$OUTPUT_FILE"

# Check if pdflatex is available
if command -v pdflatex &> /dev/null; then
    echo "Compiling PDF..."
    pdflatex "$OUTPUT_FILE"
    
    # Run twice to resolve references
    pdflatex "$OUTPUT_FILE"
    
    # Rename the PDF to the desired output name
    if [ -f "main.pdf" ]; then
        mv main.pdf "$PDF_OUTPUT"
    fi
    
    # Clean up auxiliary files
    rm -f *.aux *.log *.out
    
    echo "PDF generated: $PDF_OUTPUT"
else
    echo "Warning: pdflatex not found. LaTeX files generated but PDF not compiled."
    echo "To compile the PDF manually, run: pdflatex $OUTPUT_FILE"
fi

echo "Build complete!"
echo "Files generated:"
echo "  - $PERSONAL_INFO_FILE (personal info for preamble)"
echo "  - $SECTIONS_FILE (resume sections for document body)"
echo "  - $OUTPUT_FILE (main LaTeX file)"
if [ -f "$PDF_OUTPUT" ]; then
    echo "  - $PDF_OUTPUT (compiled PDF)"
fi
