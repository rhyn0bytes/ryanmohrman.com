# YAML-Based LaTeX Resume

This setup allows you to maintain your resume data in a YAML file and automatically generate a LaTeX resume that compiles to PDF.

## Files Overview

- `resume_data.yaml` - Your resume data in YAML format
- `yaml_to_latex.py` - Python script that converts YAML to LaTeX
- `main_template.tex` - LaTeX template file
- `base.tex` - Generated main LaTeX file (auto-generated)
- `resume_content.tex` - Generated LaTeX content from YAML (auto-generated)
- `build_resume.sh` - Build script that automates the entire process
- `Makefile` - Alternative build system using Make

## Quick Start

### Option 1: Using the build script

```bash
./build_resume.sh
```

### Option 2: Using Make

```bash
make all
```

### Option 3: Manual steps

```bash
# 1. Convert YAML to LaTeX
python3 yaml_to_latex.py resume_data.yaml --output resume_content.tex

# 2. Create base LaTeX file
cp main_template.tex base.tex

# 3. Compile PDF
pdflatex base.tex
pdflatex base.tex  # Run twice for proper references
```

## Prerequisites

- Python 3
- PyYAML (`pip3 install PyYAML`)
- LaTeX distribution with pdflatex (e.g., TeX Live, MiKTeX)
- moderncv package (usually included in LaTeX distributions)

## Editing Your Resume

Edit the `resume_data.yaml` file to update your resume content. The YAML structure includes:

### Personal Information

```yaml
personal_info:
  first_name: Your First Name
  last_name: Your Last Name
  title: Your Job Title
  address: Your Address
  phone: Your Phone
  email: your.email@example.com
  homepage: yourwebsite.com
  github: yourgithub
  quote: Your professional quote
```

### Skills

```yaml
skills:
  Category1: Skill1, Skill2, Skill3
  Category2: Skill4, Skill5, Skill6
```

### Experience

```yaml
experience:
  - position: Job Title
    company: Company Name
    location: City, State
    period: Start -- End
    description: Optional description
    achievements:
      - Achievement 1
      - Achievement 2
```

### Projects

```yaml
projects:
  Project Name: Project description
  Another Project: Another description
```

### Education

```yaml
education:
  - degree: Degree Name
    institution: Institution Name
    location: City, State
    year: Year or leave empty
    description: Optional description
```

### Certifications

```yaml
certifications:
  - Certification Name 1
  - Certification Name 2
```

## Build Commands

### Using Make

- `make` or `make all` - Build the complete resume PDF
- `make clean` - Remove generated files (except PDF)
- `make clean-all` - Remove all generated files including PDF
- `make install-deps` - Install Python dependencies
- `make help` - Show available targets

### Manual Python Script

```bash
# Convert YAML to LaTeX (output to stdout)
python3 yaml_to_latex.py resume_data.yaml

# Convert YAML to LaTeX (output to file)
python3 yaml_to_latex.py resume_data.yaml --output resume_content.tex
```

## Customization

### LaTeX Template

Edit `main_template.tex` to customize:

- Document class options
- Package imports
- Styling options
- Color scheme
- Layout settings

### Python Script

Edit `yaml_to_latex.py` to:

- Add new resume sections
- Modify LaTeX output format
- Change escaping behavior
- Add validation

## Tips

1. **Version Control**: Commit the YAML file and scripts, but you may want to `.gitignore` the generated `.tex` and `.pdf` files.

2. **Special Characters**: The script automatically escapes special LaTeX characters. If you need literal LaTeX commands in your YAML, you may need to modify the escaping function.

3. **Multiple Versions**: You can create different YAML files for different versions of your resume (e.g., `resume_tech.yaml`, `resume_management.yaml`).

4. **Continuous Integration**: You can set up CI/CD to automatically generate PDFs when you push changes to your YAML file.

## Troubleshooting

### Common Issues

1. **PyYAML not found**: Install with `pip3 install PyYAML`
2. **pdflatex not found**: Install a LaTeX distribution
3. **moderncv not found**: Install the moderncv package for LaTeX
4. **Special characters**: Check that characters are properly escaped in the output

### File Generation

If the build process fails:

1. Check that `resume_data.yaml` is valid YAML
2. Ensure Python dependencies are installed
3. Verify LaTeX installation
4. Check file permissions

## Example Workflow

1. Edit `resume_data.yaml` with your information
2. Run `make` to build the PDF
3. Review the generated `resume.pdf`
4. Commit changes to version control
5. Repeat as needed

This system allows you to maintain your resume data in a structured, version-controllable format while still producing professional LaTeX output.
