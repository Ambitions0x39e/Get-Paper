# from .write_pdf import download_pdf
import os, sys

# Paper Structure: Year Season PPn

def read_file(lnk):
    # Read from local link lnk
    lst = []
    with open(lnk, 'r') as f:
        lst.append(f.readlines())
    
    return lst

if __name__ == '__main__':
    file_path = '~/Desktop/s1_pp.md'
    os.system(f'cp {file_path} /')
    content = read_file(file_path)
    print(content)