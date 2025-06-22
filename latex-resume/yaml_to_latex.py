#!/usr/bin/env python3
"""
YAML to LaTeX Resume Generator

This script reads resume data from a YAML file and generates LaTeX content
that can be included in a ModernCV template.
"""

import yaml
import argparse
import sys
from pathlib import Path


def escape_latex(text):
    """Escape special LaTeX characters in text."""
    if not text:
        return ""
    
    # Replace special LaTeX characters, but be more conservative
    # Only escape characters that commonly cause issues
    replacements = {
        '\\': r'\textbackslash{}',  # Must be first to avoid double escaping
        '&': r'\&',
        '$': r'\$',
        '#': r'\#',
        '^': r'\textasciicircum{}',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
    }
    
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    
    return text


def generate_personal_info(data):
    """Generate LaTeX for personal information section."""
    personal = data.get('personal_info', {})
    
    latex_lines = []
    latex_lines.append("% Personal info")
    latex_lines.append(f"\\name{{{escape_latex(personal.get('first_name', ''))}}}{{{escape_latex(personal.get('last_name', ''))}}}")
    latex_lines.append(f"\\title{{{escape_latex(personal.get('title', ''))}}}")
    latex_lines.append(f"\\address{{{escape_latex(personal.get('address', ''))}}}{{}}{{}}")
    latex_lines.append(f"\\phone[mobile]{{{escape_latex(personal.get('phone', ''))}}}")
    latex_lines.append(f"\\email{{{escape_latex(personal.get('email', ''))}}}")
    latex_lines.append(f"\\homepage{{{escape_latex(personal.get('homepage', ''))}}}")
    
    if personal.get('github'):
        latex_lines.append(f"\\social[github]{{{escape_latex(personal.get('github', ''))}}}")
    
    if personal.get('quote'):
        latex_lines.append(f"\\quote{{{escape_latex(personal.get('quote', ''))}}}")
    
    return '\n'.join(latex_lines)


def generate_skills(data):
    """Generate LaTeX for skills section."""
    skills = data.get('skills', {})
    
    if not skills:
        return ""
    
    latex_lines = []
    latex_lines.append("\\section{Skills}")
    
    for category, skill_list in skills.items():
        latex_lines.append(f"\\cvitem{{{escape_latex(category)}}}{{{escape_latex(skill_list)}}}")
    
    return '\n'.join(latex_lines)


def generate_experience(data):
    """Generate LaTeX for experience section."""
    experience = data.get('experience', [])
    
    if not experience:
        return ""
    
    latex_lines = []
    latex_lines.append("\\section{Experience}")
    
    for job in experience:
        position = escape_latex(job.get('position', ''))
        company = escape_latex(job.get('company', ''))
        location = escape_latex(job.get('location', ''))
        period = escape_latex(job.get('period', ''))
        description = escape_latex(job.get('description', ''))
        
        achievements = job.get('achievements', [])
        if achievements:
            # Start the cventry with the sixth argument open
            latex_lines.append(f"\\cventry{{{period}}}{{{position}}}{{{company}}}{{{location}}}{{}}")
            latex_lines.append("{")  # Open the 6th argument
            latex_lines.append("\\begin{itemize}")
            for achievement in achievements:
                latex_lines.append(f"    \\item {escape_latex(achievement)}")
            latex_lines.append("\\end{itemize}")
            latex_lines.append("}")  # Close the 6th argument
        else:
            # Complete cventry with empty sixth argument
            latex_lines.append(f"\\cventry{{{period}}}{{{position}}}{{{company}}}{{{location}}}{{}}{{}}")
        
        latex_lines.append("")  # Add spacing between jobs
    
    return '\n'.join(latex_lines)


def generate_projects(data):
    """Generate LaTeX for projects section."""
    projects = data.get('projects', {})
    
    if not projects:
        return ""
    
    latex_lines = []
    latex_lines.append("\\section{Projects}")
    
    for project_name, description in projects.items():
        latex_lines.append(f"\\cvitem{{{escape_latex(project_name)}}}{{{escape_latex(description)}}}")
    
    return '\n'.join(latex_lines)


def generate_education(data):
    """Generate LaTeX for education section."""
    education = data.get('education', [])
    
    if not education:
        return ""
    
    latex_lines = []
    latex_lines.append("\\section{Education}")
    
    for edu in education:
        year = escape_latex(edu.get('year', ''))
        degree = escape_latex(edu.get('degree', ''))
        institution = escape_latex(edu.get('institution', ''))
        location = escape_latex(edu.get('location', ''))
        description = escape_latex(edu.get('description', ''))
        
        latex_lines.append(f"\\cventry{{{year}}}{{{degree}}}{{{institution}}}{{{location}}}{{}}{{{description}}}")
    
    return '\n'.join(latex_lines)


def generate_certifications(data):
    """Generate LaTeX for certifications section."""
    certifications = data.get('certifications', [])
    
    if not certifications:
        return ""
    
    latex_lines = []
    latex_lines.append("\\section{Certifications}")
    
    for cert in certifications:
        latex_lines.append(f"\\cvitem{{}}{{{escape_latex(cert)}}}")
    
    return '\n'.join(latex_lines)


def generate_latex_content(yaml_data):
    """Generate complete LaTeX content from YAML data."""
    # Generate personal info (for preamble)
    personal_info = generate_personal_info(yaml_data)
    
    # Generate sections (for document body)
    sections = []
    skills = generate_skills(yaml_data)
    experience = generate_experience(yaml_data)
    projects = generate_projects(yaml_data)
    education = generate_education(yaml_data)
    certifications = generate_certifications(yaml_data)
    
    # Add non-empty sections
    if skills:
        sections.append(skills)
    if experience:
        sections.append(experience)
    if projects:
        sections.append(projects)
    if education:
        sections.append(education)
    if certifications:
        sections.append(certifications)
    
    sections_content = '\n\n'.join(sections)
    
    return personal_info, sections_content


def main():
    parser = argparse.ArgumentParser(description='Convert YAML resume data to LaTeX')
    parser.add_argument('yaml_file', help='Path to YAML resume data file')
    parser.add_argument('--output', '-o', help='Output LaTeX file (default: stdout)')
    parser.add_argument('--personal-info', help='Output file for personal info (preamble)')
    parser.add_argument('--sections', help='Output file for sections (document body)')
    
    args = parser.parse_args()
    
    # Read YAML file
    try:
        with open(args.yaml_file, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: File '{args.yaml_file}' not found.", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Generate LaTeX content
    personal_info, sections_content = generate_latex_content(yaml_data)
    
    # Handle output
    if args.personal_info and args.sections:
        # Write to separate files
        try:
            with open(args.personal_info, 'w', encoding='utf-8') as f:
                f.write(personal_info)
            print(f"Personal info written to {args.personal_info}")
            
            with open(args.sections, 'w', encoding='utf-8') as f:
                f.write(sections_content)
            print(f"Sections written to {args.sections}")
        except IOError as e:
            print(f"Error writing to file: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.output:
        # Write combined content to single file (backward compatibility)
        combined_content = personal_info + '\n\n' + sections_content
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(combined_content)
            print(f"LaTeX content written to {args.output}")
        except IOError as e:
            print(f"Error writing to file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Output to stdout (combined content)
        combined_content = personal_info + '\n\n' + sections_content
        print(combined_content)


if __name__ == '__main__':
    main()
