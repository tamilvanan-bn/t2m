import sys
import bencodepy
import hashlib
import base64

def torrent_to_magnet(file_name):
    metadata = bencodepy.decode_from_file(file_name)
    torrent_info = metadata[b'info']
    hash_contents = bencodepy.encode(torrent_info)
    digest = hashlib.sha1(hash_contents).digest()
    b32hash = base64.b32encode(digest).decode()

    # Get name
    name = torrent_info[b'name'].decode()

    # Determine total size
    if b'length' in torrent_info:
        size = str(torrent_info[b'length'])  # single-file torrent
    elif b'files' in torrent_info:
        size = str(sum(file[b'length'] for file in torrent_info[b'files']))  # multi-file torrent
    else:
        size = '0'

    # Get tracker (if present)
    tracker = metadata.get(b'announce', b'').decode()

    return (
        f'magnet:?xt=urn:btih:{b32hash}'
        f'&dn={name}'
        f'&tr={tracker}'
        f'&xl={size}'
    )

if __name__ == '__main__':
    magnet = torrent_to_magnet(sys.argv[1])
    print(magnet)
