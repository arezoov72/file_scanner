import paramiko
import os

def connect_ssh(host, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=username, password=password)
    return ssh

import paramiko
import os
import stat  # Import stat module for S_ISDIR

def list_remote_files(ssh, remote_directory):
    sftp = ssh.open_sftp()
    file_list = []

    def scan_directory(path):
        try:
            for entry in sftp.listdir_attr(path):
                full_path = os.path.join(path, entry.filename)
                # Use stat.S_ISDIR to check if the entry is a directory
                if stat.S_ISDIR(entry.st_mode):
                    scan_directory(full_path)
                else:
                    file_list.append(full_path)
        except Exception as e:
            print(f"Error scanning directory {path}: {e}")

    scan_directory(remote_directory)
    sftp.close()
    return file_list

def check_local_files(remote_files, local_base_dir):
    files_info = []
    for remote_file in remote_files:
        local_file = os.path.join(local_base_dir, os.path.basename(remote_file))
        file_exists = os.path.exists(local_file)
        files_info.append({
            'path': remote_file,
            'exists_locally': file_exists
        })
    return files_info
