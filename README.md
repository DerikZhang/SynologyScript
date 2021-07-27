# SynologyScript

* Only test on DSM7.0

* Install StorageAnalyzer package
* Set up report like ![image](https://github.com/DerikZhang/SynologyScript/blob/main/createReport.png) and generate your report files
* Get two path from report: basePath and reportPath
* Upload move_duplicate_to_backup.sh and remove_duplicate_file.py files into your $basePath
* Replace string from nasReport to $reportPath 
* Run command "sh move_duplicate_to_backup.sh 
* All duplicate files will move to $basePath/backup files



