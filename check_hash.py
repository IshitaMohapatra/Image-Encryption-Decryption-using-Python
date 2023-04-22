# === Proving the data matches (hash the files and compare the hashes) ===
import hashlib

def get_file_hash(file_path):
    block_size = 65536
    file_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        fb = f.read(block_size)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(block_size)
    return file_hash.hexdigest()

assert get_file_hash('original.jpg') == get_file_hash('decrypted_original.jpg'), 'Files are not identical'