from src.central import paper_download
import os
def write_log(stats, papers, log_name):
    dir=os.path.expanduser('~/Downloads/Past_Papers/log')
    os.makedirs(dir)
    final_dir=os.path.join(dir, log_name)
    for i, j in stats, papers:
        final_dir.write(f"{i}: {j}\n")

def batch_read(path):
    # read batch
    # 0625 2012 winter 11
    batch=open(path, 'r')
    batch_name=os.path.basename(path)
    lines=batch.readlines()
    file_stat=[], file_name=[]
    for line in lines:
        infos=line.split(' ')
        if(infos[4]==''):
            result_1, filename_1=paper_download(infos[0], infos[1], infos[2], infos[3], 'qp')
            file_stat.append(result_1)
            file_name.append(filename_1)
            result_2, filename_2=paper_download(infos[0], infos[1], infos[2], infos[3], 'ms')
            file_stat.append(result_2)
            file_name.append(filename_2)
        else:
            result_1, filename_1=paper_download(infos[0], infos[1], infos[2], infos[3], infos[4])
            file_stat.append(result_1)
            file_name.append(filename_1)
            
    write_log(file_stat, file_name, batch_name+'.log')