import os
from src.info import subjects
from src.write_pdf import download_pdf
# from init_tk import init_tk, write_info
# Example Link: https://cie.fraft.cn/obj/Fetch/redir/9709_m20_ms_22.pdf

def download_path(): # Pair path to download the past paper
    return '/Users/'+os.environ.get('USER')+'/Downloads'

if __name__ == '__main__':
    get_line = input()
    qp_ms: str = None
    try:
        code, year, time, paper_code, qp_ms = get_line.split()
    except ValueError:
        code, year, time, paper_code = get_line.split()


    if len(year) == 2: year = '20'+year

    seasons=' '
    seasons = 'm' if time.lower() in ['march', 'mar', 'feb', 'february', 'spring'] \
        else 's' if time.lower() in ['may', 'june', 'jun', 'summer'] \
        else 'w' if time.lower() in ['oct', 'october', 'nov', 'november', 'winter'] \
        else ' '
    if seasons==' ': print("Error: Seasons not exist"); exit()
    qp_name = f'{code}_{seasons}{year[2:]}_qp_{paper_code}'
    ms_name = f'{code}_{seasons}{year[2:]}_ms_{paper_code}'
    # print(qp_name, ms_name)

    src_qp= 'https://cie.fraft.cn/obj/Fetch/redir/'+f'{qp_name}.pdf'
    src_ms= 'https://cie.fraft.cn/obj/Fetch/redir/'+f'{ms_name}.pdf'
    print(f"Downloading paper of Year {year}: ")
    print(f'Paper of {subjects[code]}, Number {paper_code}')
    if qp_ms == None:
        try:
            download_pdf(src_qp, qp_name)
            download_pdf(src_ms, ms_name)
        except ConnectionResetError:
            print('Wrong Network Connection or Wrong Paper Name!')
            print('Please check the paper name, and if you use any network proxy')
    else:
        if qp_ms.lower() == 'qp':  
                try: 
                    download_pdf(src_qp, qp_name)
                except ConnectionResetError: 
                    print('Wrong Network Connection or Wrong Paper Name!')
                    print('Please check the paper name, and if you use any network proxy')
        elif qp_ms.lower() == 'ms':
                try:
                    download_pdf(src_ms, ms_name)
                except ConnectionResetError:
                    print('Wrong Network Connection or Wrong Paper Name!')
                    print('Please check the paper name, and if you use any network proxy')