import os
import wget
from rich.progress import track

DOWNLOAD_URL = 'https://files.rcsb.org/download'

filter_pdbid = ['2ZEB', '1MFV', '1HJO', '1CDL']
pdbid_text_path = './data/PDBID.txt'
alphafoldid_path = './data/AlphaFoldID.txt'

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


with open(alphafoldid_path, 'r') as f:
    lines = f.readlines()[1:]
    for line in track(lines):
        id = line.replace('\n', '')
        try:
            if os.path.exists(f'tmp/{uniprot}.pdb'):
                continue
            wget.download(f'https://alphafold.ebi.ac.uk/files/AF-{id}-F1-model_v4.pdb', out=f'tmp/{id}.pdb')
        except:
            print(id)
            continue

