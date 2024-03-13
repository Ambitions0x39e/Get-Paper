import os
from src.info import subjects
from src.write_pdf import download_pdf
# Example Link: https://cie.fraft.cn/obj/Fetch/redir/9709_m20_ms_22.pdf

def download_path(): # /Users/username/Downloads
    return '/Users/'+os.environ.get('USER')+'/Downloads'

print('Subject Year Seasons Paper')
code, year, time, paper_code = input().split()

if len(year) == 2:
    year = '20'+year

seasons=' '
if time.lower() in ['march', 'mar', 'feb', 'february']:
    seasons='m'
elif time.lower() in ['may', 'june', 'jun']:
    seasons='s'
elif time.lower() in ['oct', 'october', 'nov', 'november']:
    seasons='w'
    
src_qp= 'https://cie.fraft.cn/obj/Fetch/redir/'+f'{code}_{seasons}{year[2:]}_qp_{paper_code}.pdf'
src_ms= 'https://cie.fraft.cn/obj/Fetch/redir/'+f'{code}_{seasons}{year[2:]}_ms_{paper_code}.pdf'
print(f"Downloading paper from Year {year}: ")   
print(f'Paper of {subjects[code]}, Number {paper_code}')

download_pdf(src_qp, f'{code}_{seasons}{year[2:]}_qp_{paper_code}')
download_pdf(src_ms, f'{code}_{seasons}{year[2:]}_ms_{paper_code}')