# [%#@<FILEHASH: SIZE:EKo,FNV1A:UuL/tCRiGQo >@%#]
# [%#@<FILEHASH: SIZE:EKo,SHA3_256:MCGNCxMA7aP4P7ILqdArinoCtIrFztT+Xs7WGNkJ9us >@%#]
# [%#@<FILEHASH: SHA3_512:7DPc2oC7UpnYXBxvSAPQrsAmuh86K/X77LRNXCRZLM9ZitcJep4tlV4/jSdjnWIvikypYtIomftCNiD8rpRHGQ >@%#]

import hashlib
import os
import re
import sys
import base64

# Use some arbitrary string combination to reduce chance of false positive matching
LMAGIC = '%#' + '@<FILEHASH: '
RMAGIC = ' >@' + '%#'
hash_tag_pattern_str = "".join([
    r'\['+ LMAGIC,    # Matches literal (without spaces): [ ! @ FILEHASH:
    r'([^\]]+)',     # Matches any content except the closing bracket
    RMAGIC + r'\]'   # Matches literal (without spaces): ! @ ]
])
hash_tag_pattern = re.compile(hash_tag_pattern_str)

def val_as_b64(val:int):
    bytelen = 1
    while True:
        try:
            return base64.b64encode(val.to_bytes(bytelen)).decode().rstrip('=')
        except:
            bytelen = bytelen + 1

def fnv1a_hash(data: bytes, bits: int = 64) -> str:
    """Calculate FNV1-a hash of data with specified bit length (32 or 64)."""
    if bits == 32:
        FNV_PRIME = 16777619
        FNV_OFFSET = 2166136261
        mask = 0xFFFFFFFF
        byte_length = 4
    elif bits == 64:
        FNV_PRIME = 1099511628211
        FNV_OFFSET = 14695981039346656037
        mask = 0xFFFFFFFFFFFFFFFF
        byte_length = 8
    else:
        raise ValueError("bits must be either 32 or 64")
    
    hash_value = FNV_OFFSET
    for byte in data:
        hash_value = hash_value ^ byte
        hash_value = (hash_value * FNV_PRIME) & mask
    
    return base64.b64encode(hash_value.to_bytes(byte_length, 'big')).decode().rstrip('=')

def calculate_file_hashes(file_path: str) -> dict[str, str]:
    """Calculate various hashes of file contents, excluding existing hash tags."""
    
    with open(file_path, 'rb') as f:
        content = f.read()
        content_str = content.decode('utf-8', errors='ignore')
        clean_content = hash_tag_pattern.sub('', content_str)
        clean_bytes = clean_content.encode('utf-8')
        
        hashes = {
            'SIZE': val_as_b64(len(clean_content)),
            'FNV1A_32': fnv1a_hash(clean_bytes, 32),
            'FNV1A': fnv1a_hash(clean_bytes, 64),
            'SHA256': base64.b64encode(hashlib.sha256(clean_bytes).digest()).decode().rstrip('='),
            'SHA3_256': base64.b64encode(hashlib.sha3_256(clean_bytes).digest()).decode().rstrip('='),
            'SHA3_512': base64.b64encode(hashlib.sha3_512(clean_bytes).digest()).decode().rstrip('='),
        }
        return hashes

def update_file_with_hashes(file_path: str):
    """Add missing hash values to the file, preserving existing hash locations."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    hashes = calculate_file_hashes(file_path)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for existing hashes
    has_existing_hashes = hash_tag_pattern.search(content) is not None
    
    if not has_existing_hashes:
        # Create new hash tags if none exist
        new_hashes = '\n'.join(f"# [{LMAGIC}{key}:{value}{RMAGIC}]" for key, value in hashes.items())
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_hashes + '\n' + content)
    else:
        # Update existing hashes in place
        updated_content = content
        
        def replace_hash(match):
            parts = match.group(1).split(',')
            old_values = {k.strip():v.strip() for k,v in [p.split(':') for p in parts]}
            new_values = {t: hashes[t] for t in old_values}
            if old_values == new_values:
                print(f"Unchanged: {new_values}")
            else:
                print(f'Replacing: {old_values}\n -> {new_values}')
            
            res = ",".join(f"{k}:{v}" for k,v in new_values.items())
            return f"[{LMAGIC}{res}{RMAGIC}]"
        
        updated_content = hash_tag_pattern.sub(replace_hash, updated_content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python calculate_hash.py <file_path>")
        sys.exit(1)

    update_file_with_hashes(sys.argv[1])
    print("File hash tags updated successfully.")