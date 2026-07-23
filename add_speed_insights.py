#!/usr/bin/env python3
"""
Script to add Vercel Speed Insights to all HTML files
"""
import os
import re
from pathlib import Path

# Speed Insights script to add
SPEED_INSIGHTS_SCRIPT = '<script type="module" src="/assets/speed-insights.js"></script>\n'

def add_speed_insights(file_path):
    """Add Speed Insights script to an HTML file before </head>"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if Speed Insights is already added
    if 'speed-insights.js' in content:
        print(f"✓ Speed Insights already present in {file_path}")
        return False
    
    # Find </head> and insert the script before it
    if '</head>' in content:
        # Insert the script before </head>
        content = content.replace('</head>', SPEED_INSIGHTS_SCRIPT + '</head>')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Added Speed Insights to {file_path}")
        return True
    else:
        print(f"✗ No </head> tag found in {file_path}")
        return False

def main():
    """Find all HTML files and add Speed Insights"""
    project_root = Path(__file__).parent
    html_files = list(project_root.rglob('*.html'))
    
    # Filter out node_modules
    html_files = [f for f in html_files if 'node_modules' not in str(f)]
    
    print(f"Found {len(html_files)} HTML files")
    print("-" * 60)
    
    modified_count = 0
    for html_file in html_files:
        if add_speed_insights(html_file):
            modified_count += 1
    
    print("-" * 60)
    print(f"Modified {modified_count} files")

if __name__ == '__main__':
    main()
