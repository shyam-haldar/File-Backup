# File-Backup
Makes a copy of a file with Date Stamp. If the latest copy of the file in the backup folder is same as the source file, then no backup is created.

I felt the need to create this script as I wanted to create backup copied of KeePass db file.

If you run the script without any arguments, then it will give the following usage instructions...

Usage: file_backup.py [-h|--help] | [(-f File_Name)|(--file=File_Name)] [(-b Backup_Path)|(--backdir=Backup_Path)]

Required Arguments:
    -f, --file         Path to the file that is to be backed up
    -b, --backdir      Move the Directory to the specified path after compressing

For Help:
    -h, --help         Displays the Command Help Message


To run the script just enter the following command...

file_backup.py -f /Users/shyam/keepass.kdbx -b /Volumes/Backup/KeePass_Backup

