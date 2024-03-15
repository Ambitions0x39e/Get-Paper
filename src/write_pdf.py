import requests
import os

def create_subfolder(filename): # Example: 9709_m20_qp_12
    # Firstly, get year 
    year = '20'+filename[6:8]
    paper_num = filename[12:]
    season = filename[5]
    match season:
        case 'w': season = 'Nov'
        case 's': season = 'May'
        case 'm': season = 'Feb'
    folder_name = f'{year}\ {season}\ {paper_num}'
    os.system(f'mkdir ~/Downloads/Past_Papers/{folder_name} >/dev/null 2>&1')
    return folder_name

def download_pdf(url, filename):
    r = requests.get(url, stream=True)

    with open(f'{filename}.pdf', 'wb') as fd:
        for chunk in r.iter_content(1024):
            fd.write(chunk)

    folder = create_subfolder(filename)
    os.system(f"mv {filename}.pdf ~/Downloads/Past_Papers/{folder} >/dev/null 2>&1")