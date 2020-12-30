HELP = '''
Usage:
- Script version:
    
    python unoffice.py "path\\to\\example.docx" "path\\to\\example2.xlsx" ...

- Binary version:
    
    unoffice  "path\\to\\example.docx" "path\\to\\example2.xlsx" ...
    
or for (Powershell)
    
    ./unoffice  "path\\to\\example.docx" "path\\to\\example2.xlsx" ...
'''

DOCX = (
    # Path inside MS Word archive
    'word/settings.xml',
    # Partial Read-only and Full Read-only
    r'(<w:documentProtection .*?/>)?(<w:writeProtection .*?/>)?'
)

PPTX = (
    'ppt/presentation.xml',
    r'<p:modifyVerifier .*?/>'
)

XLSX = (
    'xl/workbook.xml',
    r'(<fileSharing .*?/>)?(<sheetProtection .*?/>)?'
)

EXTS = {'docx': DOCX, 'pptx': PPTX, 'xlsx': XLSX}