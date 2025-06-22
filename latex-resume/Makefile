# Makefile for YAML-based LaTeX resume

# Configuration
YAML_FILE = resume_data.yaml
PERSONAL_INFO_FILE = resume_content.tex
SECTIONS_FILE = resume_sections.tex
TEMPLATE_FILE = main_template.tex
OUTPUT_FILE = base.tex
PDF_OUTPUT = resume.pdf

# Default target
all: pdf

# Generate LaTeX content from YAML
$(PERSONAL_INFO_FILE) $(SECTIONS_FILE): $(YAML_FILE) yaml_to_latex.py
	@echo "Converting YAML to LaTeX..."
	python3 yaml_to_latex.py $(YAML_FILE) --personal-info $(PERSONAL_INFO_FILE) --sections $(SECTIONS_FILE)

# Create base LaTeX file
$(OUTPUT_FILE): $(TEMPLATE_FILE) $(PERSONAL_INFO_FILE) $(SECTIONS_FILE)
	@echo "Creating base LaTeX file..."
	cp $(TEMPLATE_FILE) $(OUTPUT_FILE)

# Compile PDF
pdf: $(OUTPUT_FILE)
	@echo "Compiling PDF..."
	pdflatex $(OUTPUT_FILE)
	pdflatex $(OUTPUT_FILE)  # Run twice for references
	mv base.pdf $(PDF_OUTPUT) 2>/dev/null || true
	@echo "PDF generated: $(PDF_OUTPUT)"

# Clean generated files
clean:
	rm -f $(PERSONAL_INFO_FILE) $(SECTIONS_FILE) $(OUTPUT_FILE) *.aux *.log *.out *.fls *.synctex.gz *.fdb_latexmk

# Clean everything including PDF
clean-all: clean
	rm -f $(PDF_OUTPUT)

# Install Python dependencies
install-deps:
	pip3 install PyYAML

# Copy resume.pdf to the assets directory for deployment
publish:
	cp $(PDF_OUTPUT) ../assets/download/Ryan-Mohrman-Resume.pdf && echo "Published resume to ../assets/download/Ryan-Mohrman-Resume.pdf"

# Show help
help:
	@echo "Available targets:"
	@echo "  all (default) - Build the PDF resume"
	@echo "  pdf           - Compile the PDF"
	@echo "  clean         - Remove generated files (except PDF)"
	@echo "  clean-all     - Remove all generated files including PDF"
	@echo "  install-deps  - Install Python dependencies"
	@echo "  publish       - Copy the PDF to the assets directory for deployment"
	@echo "  help          - Show this help message"

.PHONY: all pdf clean clean-all install-deps publish help
