# Arrows-Only
Take old JavaScript functions and convert them to arrow syntax!

## Note: There are some special cases where using the arrow-function syntax will break your code. Always double check the new code works before deleting the old one.

## Required:
Python 2

Old JavaScript/ECMAScript Code

## How to Run:
Note: Converted files can be found in the folder of the original files with a '-new.js' suffix.
### Converting all .js files in a folder:
```bash
$ python func-to-arrow.py 'path-to-folder'
```

### Converting a single .js file:
```bash
$ python func-to-arrow.py 'yourFile.js' 'newFileName.js'
```
if 'newFileName.js' is not provided, the output will default to 'yourFile-new.js' in the same directory.
