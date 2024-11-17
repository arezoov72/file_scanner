from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .utils import connect_ssh, list_remote_files, check_local_files

def file_list(request):
    # Remote connection settings
    host = "192.168.1.179"
    username = "root"
    password = "Dev0ps"
    remote_directory = "/home/devops/Pictures"
    local_base_dir = "D:/Learning/DEVOPs"

    # Connect and scan files
    ssh = connect_ssh(host, username, password)
    remote_files = list_remote_files(ssh, remote_directory)
    files_info = check_local_files(remote_files, local_base_dir)
    ssh.close()
    

    return render(request, 'scanner/file_list.html', {'files': files_info})






