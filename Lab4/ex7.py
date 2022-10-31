import os


def info(path):
    dictionar = {}
    dictionar["full_path"]=os.path.abspath(path)
    dictionar["file_size"]=os.path.getsize(path)
    dictionar["file_extension"]=os.path.splitext(path)[1]
    dictionar["can_read"]=os.access(path,os.R_OK)
    dictionar["can_write"]=os.access(path,os.W_OK)
    return dictionar
def main():
    path = "E:\\AN3\\Sem1\\A3D\\BODY.blend1"
    print(info(path))

main()