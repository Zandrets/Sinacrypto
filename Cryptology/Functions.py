import os
    
def file_reader(path, file):
    org_file=open(path+file, 'rb')
    org_file.seek(0, os.SEEK_END)
    file_size=org_file.tell() #FILE SIZE
    org_file.close
    return file_size
    
if __name__ == "__main__":
    #USAGE OF FILE SIZE CALCULATION TOOL
    print(file_reader(str(os.getcwd())+'\\' , "test_file.rar"))

    