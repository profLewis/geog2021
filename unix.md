# Basic UNIX commands

Since you will be working on UNIX (Linux) computers, it is useful to know a few UNIX commands.

## Change directory `cd`

Your course notes (these notes) should be available to you in the location `/home/zcfa***/DATA/geog2021` and `/home/zcfa***/DATA/Geog2021_Coursework`, where `zcfa***` is your username.

The location `/home/zcfa***` on the file system is called your **home directory**. When you open a shell tool (terminal) this will usually be the directory you are in to start with.

You can also refer to this location as `~` ('twiddle') or `~zcfa***` (the home of user `zcfa***`).

If you are not sure where you are on the system, you can type (`machine%` is the prompt, which will usually be your computer name):

    machine% cd ~
  
to take you 'home'.

So, the command 

    machine% cd SOMEWHERE
  
changes directory to `SOMEWHERE` (assuming `SOMEWHERE` exists).

Your data directory is located in `~/DATA`, i.e. the subdirectory `DATA` from your home directory.

To change directory there, type:

    machine% cd ~/DATA
 
## Where am I? `pwd`

If you want to know which directory you are in, type:

    machine% pwd
    
This will give e.g. `/home/zcfa***/DATA` (depending on who, and where you are of course). If you are not sure where you are, use this command.

## What is in the directory? `ls`

We use the command `ls` to get a listing of the files in a particular directory. For example:

    machine% cd ~/DATA/geog2021
    machine% pwd
    machine% ls -lh
    
The `-lh` parts tell the command to give a 'long' listing (`-l`) (with file size information etc.) in human readable form (`-h`). e.g.:

    -rw-r--r--  1 plewis  staff    18K 11 Jan 14:07 Classification.ipynb
    -rw-r--r--  1 plewis  staff    39M 11 Jan 14:07 ClassificationIntro.ipynb
    -rw-r--r--  1 plewis  staff    22K 11 Jan 14:07 ImageDisplay.ipynb
    -rw-r--r--  1 plewis  staff   6.4K 11 Jan 14:07 LICENSE
    -rw-r--r--  1 plewis  staff   2.8K 11 Jan 14:07 Programming.ipynb
    -rw-r--r--  1 plewis  staff   7.1K 11 Jan 14:07 README.md
    -rw-r--r--  1 plewis  staff   532K 11 Jan 14:07 SpatialFiltering.ipynb
    -rw-r--r--  1 plewis  staff   1.8K 11 Jan 14:07 classes.xml
    drwxr-xr-x  2 plewis  staff   340B 11 Jan 14:13 coursenotes
    drwxr-xr-x  2 plewis  staff   340B 11 Jan 14:07 data
    -rw-r--r--  1 plewis  staff   940B 11 Jan 14:07 gmRondonia.html
    -rw-r--r--  1 plewis  staff   940B 11 Jan 14:07 gmRondoniaZoom.html
    drwxr-xr-x  2 plewis  staff   2.9K 11 Jan 14:07 images
    drwxr-xr-x  3 plewis  staff   102B 11 Jan 14:07 jensen
    drwxr-xr-x  3 plewis  staff   238B 11 Jan 14:07 practical1
    -rwxr-xr-x  1 plewis  staff    46B 11 Jan 14:07 pullYou
    -rwxr-xr-x  1 plewis  staff   109B 11 Jan 14:07 pushMe
    drwxr-xr-x  2 plewis  staff   374B 11 Jan 14:07 python

The first 'field' (-rw-r--r--) tells you about file permissions. It is grouped into 3 categories. -rw-r--r-- means that the owner (plewis) has read-and-write permission (rw) and that others have only read permission (r-).
The third field tells you the file owner. The fifth field tells you the file size in bytes or other appropriate form (`B`, 'K', 'M', 'G' etc.).
Thats all you really need to know right now.

## Make a new directory: `mkdir`

To make a new directory (called `practicalWork` in this example), type:

    machine% mkdir practicalWork
    
Now change directory again (relative to where you are ...) 
 
    machine% cd practicalWork
    
Check where you are:

    machine% pwd
    
## Copy files: `cp`
    
For copying a file to the current directory (i.e. where you are now), note that we often use the special symbol `.` (`.` == 'dot' == current directory)
 
    machine% cd ~/DATA/geog2021
    machine% mkdir practicalWork
    machine% cd practicalWork
    machine% cp ~plewis/2021/ETM-* .
    
Note that the `*` symbol is a wildcard, so `~plewis/2021/ETM-*`z is all files that start with `~plewis/2021/ETM-`. The `.` ('dot')  means the current directory. ~ ('tilde' or 'twiddle')  refers to the home directory of a user, so ~plewis refers to the home directory of plewis. 

You should check to see what files have been copied over, e.g.:

  machine% ls -l ~/DATA/practical1


## Some other useful commands:

You might also be interested in how much disk space there is left on the disk you are on:

    machine% df -h . 
    Filesystem     Size   Used  Avail Capacity iused      ifree %iused  Mounted on
    /dev/disk0s2  931Gi  895Gi   36Gi    97% 2327284 4292639995    0%   /
    
    
tells us that the disk known as `/dev/disk0s2` has 36 Gbytes available, for instance. Again, . ('dot') refers to the current directory/filesystem. 

To delete a file:

    machine% rm whatEverItsCalled.dat
    
to compress a file:

    machine% gzip ETM-190600 
    
Type:

    machine% ls -l

which gives (among other things)

    -rw-r--r--   1 plewis   ps       24094770 Sep 23 13:38 ETM-190600.gz

The compressed file (with a .Z or .gz extension) is 24094770 bytes (the original was 34200000, so the compression ratio is around 1.4 in this case).

or to uncompress:

    machine% gunzip ETM-190600 
 

The next time you want to run the practical, just do:

    machine% cd ~/DATA/geog2021/practicalWork
    machine% envi 
    
    
where `envi` is the software we will mostly be using for these practicals.
Summary

Today, you came across the following UNIX commands:


      cd                 change directory              e.g.:      cd ~plewis
      mkdir              make a directory              e.g.:      mkdir ~/DATA/something
      cp                 copy files (cp <from> <to>)   e.g.:      cp ~plewis/logo/ucllogo.tif ~/DATA
      ls -l              list all files in long format e.g.:      ls -l ~plewis
      df                 disk space free               e.g.:      df ~
      pwd                print working directory       e.g.:      pwd
      rm                 remove a file                 e.g.:      rm ~/DATA/ucllogo.tif
      gzip               gzipfile                      e.g.:      gzip ~/DATA/ucllogo.tif
      gunzip             gunzip a (.gz) file           e.g.:        gunzip ~/DATA/ucllogo.tif

You also learnt what ~ and . mean.

Thats enough UNIX for one day! If you want to learn more UNIX or just some more background on workstations, directories etc., have a look at the MSc remote sensing course notes. 
  
