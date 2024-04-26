import glob, requests
def parse_resume():
    resumes = []
    url = 'https://api.apilayer.com/resume_parser/upload'
    headers = {
        'Content-Type': 'application/octet-stream',
        'apikey': 'ZPDcHTNOomS7CiFl88LP67SCP1GVuztf'
    }

    folder_path = 'resumes/*.pdf'
    files = glob.glob(folder_path)
    print(files)
    for i, file_path in enumerate(files):
        print(file_path)
        with open(file_path, 'rb') as f:
            data = f.read()
        response = requests.post(url, headers=headers, data=data)
        resumes.append("Resume " + str(i) + ":  " + str([response.text]))
    print("resumes parsed:",resumes)
    return resumes

print(parse_resume())