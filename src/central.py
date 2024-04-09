from .write_pdf import download_pdf
def paper_download(Paper_Code, Year, Season, Paper_Number, Qp_Ms):
    # FULL year if user only inputs the last two digits of the year number
    if len(Paper_Code) != 4: return "Wrong Paper Code", 'NA'
    if len(Year) == 2: Year = '20' + Year
    seasons = ''
    seasons = 'm' if Season.lower() in ['march', 'mar', 'feb', 'february', 'spring'] \
        else 's' if Season.lower() in ['may', 'june', 'jun', 'summer'] \
        else 'w' if Season.lower() in ['oct', 'october', 'nov', 'november', 'winter'] \
        else ''
    if seasons == '':
        return 'Wrong Seasons', 'NA'
    qp_name = f'{Paper_Code}_{seasons}{Year[2:]}_qp_{Paper_Number}'
    ms_name = f'{Paper_Code}_{seasons}{Year[2:]}_ms_{Paper_Number}'
    src_qp= 'https://cie.fraft.cn/obj/Fetch/redir/'+f'{qp_name}.pdf'
    src_ms= 'https://cie.fraft.cn/obj/Fetch/redir/'+f'{ms_name}.pdf'
    
    if Qp_Ms == '':
        try: 
            download_pdf(src_qp, qp_name)
            download_pdf(src_ms, ms_name)
        except ConnectionResetError:
            return "Wrong Network! Please check your network / proxies", qp_name
    elif Qp_Ms.lower() == 'qp':
        try:
            download_pdf(src_qp, qp_name)
        except ConnectionResetError:
            return "Wrong Network! Please check your network / proxies", qp_name
    elif Qp_Ms.lower() == 'ms': 
        try:
            download_pdf(src_ms, ms_name)
        except ConnectionResetError:
            return "Wrong Network! Please check your network / proxies", qp_name
    else:
        return "Wrong QP / MS input!", qp_name
    
    return 'Success', qp_name