#!/usr/bin/env python3
"""
Script to compile .po files to .mo files for Flask-Babel
"""
import os
import struct

def read_po_file(po_file_path):
    """Read a .po file and return its content"""
    with open(po_file_path, 'r', encoding='utf-8') as f:
        return f.read()

def parse_po_data(po_content):
    """Parse .po file content into a dictionary"""
    messages = {}
    lines = po_content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if line.startswith('msgid '):
            msgid = line[7:-1]  # Remove 'msgid ' and trailing quote
            msgid = msgid.strip('"')
            
            # Skip to msgstr
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('msgstr '):
                i += 1
            
            if i < len(lines):
                msgstr = lines[i].strip()[8:-1]  # Remove 'msgstr ' and trailing quote
                msgstr = msgstr.strip('"')
                messages[msgid] = msgstr
        
        i += 1
    
    return messages

def create_mo_file(po_file_path, mo_file_path):
    """Create a .mo file from a .po file"""
    po_content = read_po_file(po_file_path)
    messages = parse_po_data(po_content)
    
    # .mo file format
    keys = sorted(messages.keys())
    koffsets = []
    voffsets = []
    kencoded = []
    vencoded = []
    
    # Build the catalog
    for key in keys:
        kencoded.append(key.encode('utf-8'))
        vencoded.append(messages[key].encode('utf-8'))
    
    # Calculate offsets
    koffsets.append(len(keys) * 8)  # Header size
    for kdata in kencoded:
        koffsets.append(koffsets[-1] + len(kdata))
    
    voffsets.append(koffsets[-1])
    for vdata in vencoded:
        voffsets.append(voffsets[-1] + len(vdata))
    
    # Write .mo file
    with open(mo_file_path, 'wb') as f:
        # Magic number
        f.write(struct.pack('<I', 0x950412de))
        # Version
        f.write(struct.pack('<I', 0))
        # Number of entries
        f.write(struct.pack('<I', len(keys)))
        # Offset of key table
        f.write(struct.pack('<I', 7 * 4))
        # Offset of value table
        f.write(struct.pack('<I', (7 + len(keys) * 2) * 4))
        # Hash table size (unused)
        f.write(struct.pack('<I', 0))
        # Offset of hash table (unused)
        f.write(struct.pack('<I', 0))
        
        # Key offsets
        for i in range(len(keys)):
            f.write(struct.pack('<I', koffsets[i]))
        
        # Value offsets
        for i in range(len(keys)):
            f.write(struct.pack('<I', voffsets[i]))
        
        # Keys
        for kdata in kencoded:
            f.write(kdata)
        
        # Values
        for vdata in vencoded:
            f.write(vdata)

if __name__ == '__main__':
    po_files = [
        ('app/translations/en/LC_MESSAGES/messages.po', 'app/translations/en/LC_MESSAGES/messages.mo'),
        ('app/translations/id/LC_MESSAGES/messages.po', 'app/translations/id/LC_MESSAGES/messages.mo')
    ]
    
    for po_file, mo_file in po_files:
        if os.path.exists(po_file):
            create_mo_file(po_file, mo_file)
            print(f'Generated {mo_file} from {po_file}')
        else:
            print(f'File not found: {po_file}')