import os
import wget
from rich.progress import track

DOWNLOAD_URL = 'https://files.rcsb.org/download'

filter_pdbid = ['2ZEB', '1MFV', '1HJO', '1CDL']
pdbid_text_path = './data/PDBID.txt'

uniprot_pdbid_dict = {}
pdb_urls = []
with open(pdbid_text_path, 'r') as f:
    lines = f.readlines()[1:]
    for line in track(lines):
        uniprot, pdbid = line.split('\t')
        uniprot, pdbid = uniprot.replace('\n', ''), pdbid.replace('\n', '')
        if pdbid not in filter_pdbid:
            # uniprot_pdbid_dict[pdbid] = uniprot
            try:
                if os.path.exists(f'tmp/{uniprot}.pdb'):
                    continue
                wget.download(f'{DOWNLOAD_URL}/{pdbid}.pdb', out=f'tmp/{uniprot}.pdb')
            except:
                print(pdbid)
                continue

#         pdb_urls.append(f'{DOWNLOAD_URL}/{pdbid}.pdb')

# for pdb_url in pdb_urls:
#     wget.download(pdb_url, out=f'./tmp/{uniprot_pdbid_dict[]}')

# print(uniprot_pdbid_dict)