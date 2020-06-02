# Alternate Data Stream
Can be use to hide information in an NTFS data stream (not file content, which typically use an empty data stream). 
Ringzer0 Forensics Challenge dinosaur #92

I had to use an SIFT workstation to have ewf-tools don't crap out . fdisk -l didn't find an ntfs volume
ewftools <image_name> <dir>
 cd /mnt/ewf
    parted ewf1    
        /mnt/ewf/ewf1 has been opened read-only.
        GNU Parted 2.3
        Using /mnt/ewf/ewf1
        Welcome to GNU Parted! Type 'help' to view a list of commands.
        (parted) u                                                                
        Unit?  [compact]? B                                                       
        (parted) print                                                            
        Model:  (file)
        Disk /mnt/ewf/ewf1: 13631488B
        Sector size (logical/physical): 512B/512B
        Partition Table: loop

        Number  Start  End        Size       File system  Flags
        1      0B     13631487B  13631488B  ntfs


mount -o loop,show_sys_files,streams_interface=windows /mnt/ewf/ewf1 /mnt/ewf_mount

getfattr -n ntfs.streams.list  -R ./ewf_mount



nsforensics@siftworkstation: /mnt
$ hexdump -C ewf_mount/\$RECYCLE.BIN/S-1-5-21-2338092958-3425525054-89474938-1000/\$R2N8R8J.txt
sansforensics@siftworkstation: /mnt
$ hexdump -C ewf_mount/\$RECYCLE.BIN/S-1-5-21-2338092958-3425525054-89474938-1000/\$R2N8R8J.txt:flag.txt
00000000  66 6c 61 67 2d 36 62 39  36 65 32 31 32 62 33 66  |flag-6b96e212b3f|
00000010  38 35 39 36 38 64 62 36  35 34 66 37 38 39 32 66  |85968db654f7892f|
00000020  30 36 31 32 32                                    |06122|

