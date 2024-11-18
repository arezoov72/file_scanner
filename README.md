# file_scanner

this project scans another machine files and compare it with curent machine.if file exist shows that it exist with gray color

To build requirement in Django, you need to connect to a remote machine, scan file, and display them in the browser. Files existing locally will be displayed in grey with a "files exist" message.
1. Create Django Project and App
2.  Install Dependencies:first, Install paramiko for SSH connections and then write Utility Functions which is Add a file named utils.py in the scanner app to handle SSH connection, remote file scanning, and checking if files exist locally.
  
   3.  Create Django Views: In the scanner app, define a view to scan the remote machine and display the files.
   4.   Create a Template: Create a directory templates/scanner/ and add a template file_list.html to display the files.
   5.   Add URL Configuration: Create a urls.py file in the scanner app

don't forget to Include the scanner app URLs in your project’s urls.py

and finally python manage.py runserver

