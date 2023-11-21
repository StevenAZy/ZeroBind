import os
import wget

from rich.progress import track

# path = os.getcwd() + os.sep + 'data' +  os.sep + 'AlphaFoldID.txt'

# with open(path, 'r') as f:
#     uniprotnames = f.readlines()[1:]
#     for uniprotname in uniprotnames:
#         url = f'https://alphafold.ebi.ac.uk/files/AF-{uniprotname[:-2]}-F1-model_v4.pdb'
#         out_path = os.getcwd() + os.sep + 'tmp' +  os.sep + f'AF-{uniprotname[:-2]}-F1-model_v4.pdb'
#         wget.download(url, out=out_path)



path = os.getcwd() + os.sep + 'data' +  os.sep + 'PDBID.txt'

with open(path, 'r') as f:
    lines = f.readlines()[1:]
    lines = [line.replace('\n', '').replace('\r', '') for line in lines]

print(lines)
for line in track(lines):
    with open('tmp.txt', 'a') as f:
        f.write(line.split('\t')[-1] + ' ')




