#!/usr/bin/env python3
import datetime
import getopt
import hashlib
import os
import sys
import shutil
import re


def Get_New_Backup_File_Name(FileName=None, BackupDir=None):
    RetVal      = None
    Loop        = True
    Ctr         = 0
    File_Exists = False
    while Loop:
        (Base_Name, Base_Ext) = os.path.splitext(os.path.basename(FileName))
        Date_Stamp            = datetime.date.today().strftime("%Y%m%d")
        if File_Exists:
            New_Backup_File_Name     = '%s_%s_%s%s' % (Base_Name, Date_Stamp, "%02d" % Ctr, Base_Ext)
            New_Backup_File_Name_Path = '%s%s%s' % (BackupDir, os.path.sep, New_Backup_File_Name)
        else:
            New_Backup_File_Name     = '%s_%s%s' % (Base_Name, Date_Stamp, Base_Ext)
            New_Backup_File_Name_Path = '%s%s%s' % (BackupDir, os.path.sep, New_Backup_File_Name)
        if os.path.exists(New_Backup_File_Name_Path):
            Ctr += 1
            File_Exists = True
        else:
            Loop = False
            RetVal = New_Backup_File_Name_Path
    return RetVal


def Get_Last_File_Backup_Name(FileName=None, BackupDir=None):
    RetVal = None
    BaseName = os.path.splitext(os.path.basename(FileName))[0]
    File_List = []
    Selected_File_List = []
    if os.path.exists(BackupDir) and os.path.isdir(BackupDir):
        File_List = os.listdir(BackupDir)
        for File in File_List:
            if File.startswith(BaseName):
                Selected_File_List.append(File)
        if Selected_File_List:
            RetVal = '%s%s%s' % (BackupDir, os.path.sep, sorted(Selected_File_List)[-1])
    return RetVal


def Get_File_Hash(FileName=None):
    RetVal = None
    if FileName:
        if os.path.exists(FileName):
            RetVal = hashlib.md5(open(FileName,'rb').read()).hexdigest()
    return RetVal


def Main_Function(FileName=None, BackupDir=None):
    print()
    Backup_Flag = False
    Base_FileName = os.path.basename(FileName)
    Current_File_Hash = Get_File_Hash(FileName)

    Last_Backup_File_Name = Get_Last_File_Backup_Name(FileName=FileName, BackupDir=BackupDir)

    if Last_Backup_File_Name:
        Last_Backup_File_Hash = Get_File_Hash(Last_Backup_File_Name)
        if Current_File_Hash != Last_Backup_File_Hash:
            Backup_Flag = True
    else:
        Backup_Flag = True

    if Backup_Flag:
        New_Backup_File_Name = Get_New_Backup_File_Name(FileName, BackupDir)
        shutil.copy(FileName, New_Backup_File_Name)
        print("File: '%s' backed up as '%s'" % (Base_FileName, New_Backup_File_Name))
    else:
        print("Backup of file '%s' is already present '%s'" % (Base_FileName, Last_Backup_File_Name))
    return


def Usage():
    print("""
Usage: %s [-h|--help] | [(-f File_Name)|(--file=File_Name)] [(-b Backup_Path)|(--backdir=Backup_Path)]

Required Arguments:
    -f, --file         Path to the file that is to be backed up
    -b, --backdir      Backup directory

For Help:
    -h, --help         Displays the Command Help Message
""" % os.path.basename(sys.argv[0]))


if __name__ == '__main__':
    argv = sys.argv
    FileName   = None
    BackupDir  = None
    if len(argv) == 1:
        Usage()
        sys.exit(1)
    else:
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hf:b:", ["help", "file=", "backdir="])
        except getopt.GetoptError as err:
            print(str(err)) # will print something like "option -a not recognized"
            Usage()
            sys.exit(2)

    for Option, Argument in opts:
        if Option in ('-f', '--file'):
            FileName  = Argument
        if Option in ('-b', '--backdir'):
            BackupDir = Argument
        if Option in ('-h', '--help'):
            Usage()
            sys.exit(2)

    if FileName and BackupDir:
        if os.path.exists(FileName):
            if os.path.exists(BackupDir):
                FileName  = os.path.abspath(FileName)
                BackupDir = os.path.abspath(BackupDir)
                Main_Function(FileName=FileName, BackupDir=BackupDir)
            else:
                print("Backup Directory: %s does not exist. Exiting!!" % (BackupDir))
        else:
            print("File: %s does not exist. Exiting!!" % (FileName))
    else:
        Usage()
