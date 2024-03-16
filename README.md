# File-Backup
Makes a copy of a file with Date Stamp. If the latest copy of the file in the backup folder is same as the source file, then no backup is created.

I wanted to create backup copies of KeePass db file, hence created this script.
Hope you find it useful.

```bash
Usage: file_backup.py [-h|--help] | [(-f File_Name)|(--file=File_Name)] [(-b Backup_Path)|(--backdir=Backup_Path)]

Required Arguments:
    -f, --file         Path to the file that is to be backed up
    -b, --backdir      Backup directory

For Help:
    -h, --help         Displays the Command Help Message
```

To run the script just enter the following command...
```bash
file_backup.py -f /Users/shyam/keepass.kdbx -b /Volumes/Backup/KeePass_Backup
```
