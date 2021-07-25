#!/usr/bin/env python3

from os import getcwd
from weasyprint import HTML, CSS
doc_pdf = HTML(f'file://{getcwd()}/cv.html').write_pdf(
    'cv.pdf', stylesheets=[CSS(f'file://{getcwd()}/styles.css')])
