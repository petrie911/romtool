from subprocess import call
import os



UncompIndsDict = {
    'OoT 1.0': [0,1,2,3,4,5,6,7,8,9,15,16,17,18,19,20,21,22,23,24,25,26,942,944,946,948,950,952,954,956,958,960,962,964,966,968,970,972,974,976,978,980,982,984,986,988,990,992,994,996,998,1000,1002,1004],
    'OoT 1.2':[0,1,2,3,4,5,6,7,8,9,15,16,17,18,19,20,21,22,23,24,25,26,942,944,946,948,950,952,954,956,958,960,962,964,966,968,970,972,974,976,978,980,982,984,986,988,990,992,994,996,998,1000,1002,1004],
    'NTSC MQ':[0,1,2,3,4,5,6,7,8,9,15,16,17,18,19,20,21,22,23,24,25,26,941,943,945,947,949,951,953,955,957,959,961,963,965,967,969,971,973,975,977,979,981,983,985,987,989,991,993,995,997,999,1001,1003],
    'OoT PAL':[0,1,2,3,4,5,6,7,8,15,16,17,18,19,20,21,22,23,24,25,26,27,943,945,947,949,951,953,955,957,959,961,963,965,967,969,971,973,975,977,979,981,983,985,987,989,991,993,995,997,999,1001,1003,1005],
    'PAL MQ':[0,1,2,3,4,5,6,7,8,15,16,17,18,19,20,21,22,23,24,25,26,27,501,607,624,648,649,737,841,856,869,942,944,946,948,950,952,954,956,958,960,962,964,966,968,970,972,974,976,978,980,982,984,986,988,990,992,994,996,998,1000,1002,1004,1005,1006,1497,1498,1499,1500,1501,1502,1503,1504,1505,1506,1507,1508,1509],
    'petrie':[0,1,2,3,4,5,6,7,8,15,16,17,18,19,20,21,22,23,24,25,26,27,501,607,624,648,649,737,841,856,869,942,944,946,948,950,952,954,956,958,960,962,964,966,968,970,972,974,976,978,980,982,984,986,988,990,992,994,996,998,1000,1002,1004,1005,1006,1497,1498,1499,1500,1501,1502,1503,1504,1505,1506,1507,1508,1509],
    'Debug': [0,1,2,3,4,5,6,7,8,9,15,16,17,18,19,20,21,22,23,24,25,26,942,944,946,948,950,952,954,956,958,960,962,964,966,968,970,972,974,976,978,980,982,984,986,988,990,992,994,996,998,1000,1002,1004,1005,1006],
    }



ROMinfoDict = {
    'OoT 1.0' : 'OOT10.txt',
    'OoT 1.2' : 'OOT12.txt',
    'NTSC MQ' : 'NTSCMQ.txt',
    'OoT PAL' : 'OOTPAL.txt',
    'PAL MQ'  : 'PALMQ.txt',
    'petrie'  : 'petrie.txt',
    'Debug'   : 'Debug.txt'
    }



ROMtypeDict = {
    0x07430+1510 : 'OoT 1.0',
    0x07960+1510 : 'OoT 1.2',
    0x07170+1509 : 'NTSC MQ',
    0x07950+1511 : 'OoT PAL',
    0x07170+1510 : 'PAL MQ',
    0x07170+1511 : 'petrie',
    0x12F70+1532 : 'Debug'
    }



BootDict = {
    'OoT 1.0' : [27,0x7F1EA,31,0x13,0x32],
    'OoT 1.2' : [27,0x7F1FA,31,0x13,0x32],
    'NTSC MQ' : [27,0x7F0FA,30,0x13,0x32],
    'OoT PAL' : [28,0x7F17A,32,0x13,0x32],
    'PAL MQ'  : [28,0x7F0AA,31,0x13,0x32],
    'petrie'  : [28,0x7F0AA,31,0x13,0x32],
    'Debug'   : [28,0x8B60A,31,0x0F,0x36]
    }



# BootDict = {
    # 'OoT 1.0' : [0x0,0x0,0x0],
    # 'OoT 1.2' : [0x0,0x0,0x0],
    # 'NTSC MQ' : [0x0,0x0,0x0],
    # 'OoT PAL' : [0x0,0x0,0x0],
    # 'PAL MQ'  : [0xB070AA,0xB8D732,0xB8D713],
    # 'Debug'   : [0xB1F60A,0xBD2B56,0xBD2B2F]
    # }



EntranceDict = {
    'ydan' : 0x000,
    'ydan_boss' : 0x40F,
    'ddan' : 0x004,
    'ddan_boss' : 0x40B,
    'bdan' : 0x028,
    'bdan_boss' : 0x301,
    'Bmori1' : 0x169,
    'moribossroom' : 0x00C,
    'HIDAN'  : 0x165,
    'FIRE_bs' : 0x305,
    'MIZUsin' : 0x010,
    'MIZUsin_bs' : 0x417,
    'HAKAdan' : 0x037,
    'HAKAdan_bs' : 0x413,
    'HAKAdanCH' : 0x98,
    'jyasinzou' : 0x082,
    'jyasinboss' : 0x08D,
    'ice_doukutu' : 0x088,
    'men' : 0x008,
    'ganontika' : 0x467,
    'ganon' : 0x41B,
    'ganon_boss' : 0x41F
}



def yaz0encBytes(decompbytes):
    #hopefully to be replaced by a python implementation

    try:
        fileuncomp = open('TempUncomp.bin','wb')
        fileuncomp.write(decompbytes) #Put the uncompressed file into a holding file
        fileuncomp.close() 
        call(['yaz0enc.exe','TempUncomp.bin']) #compress the holding file
        filecomp = open('TempUncomp.bin.yaz0','rb')
        FileBytes = filecomp.read() #read in compressed file
        filecomp.close()
    finally:
        fileuncomp.close()
        filecomp.close()

    return FileBytes



def yaz0decBytes(compbytes):
    #hopefully to be replaced with a python implementation

    try:
        filecomp = open('TempComp.bin.yaz0','wb')
        filecomp.write(compbytes) #Put the compressed file into a holding file
        filecomp.close() 
        call(['yaz0dec.exe','TempComp.bin.yaz0']) #uncompress the holding file
        fileuncomp = open('TempComp.bin.yaz0 0.rarc','rb')
        FileBytes = fileuncomp.read() #read in uncompressed file
    finally:
        fileuncomp.close()
        filecomp.close()
    
    return FileBytes



def fixCRC(ROMname):
    #hopefully to be replaced by a python implementation
    
    call(['rn64crc.exe','-u',ROMname])
    
    print('CRC fixed')
    
    return 1



def findfiletable(ROM):
    
    ROM.seek(0,0)
    
    BootArea = ROM.read(0x40000)
    
    FileTableStart = BootArea.find(b'\x00\x00\x00\x00\x00\x00\x10\x60')
    
    return FileTableStart



def findROMtype(ROMfilename):
    
    ROM = open(ROMfilename,'rb')

    FileTableStart = findfiletable(ROM)
    
    ROM.seek(0x10 * 1505 + FileTableStart, 0)
    
    ind = 0
    comptemp = ROM.read(0x10)
    while(comptemp[0:8] != b'\x00\x00\x00\x00\x00\x00\x00\x00'):
        ind += 1
        comptemp = ROM.read(0x10)
    
    ROM.close()
    
    NFiles = ind + 1505
    
    ROMtype = ROMtypeDict.get(FileTableStart+NFiles,'Unknown')
        
    return [ROMtype,FileTableStart,NFiles]
    


def checkfiletable(ROM,FileTableStart,NFiles):
    
    #File table always begins with 0x0000000000001060
    ROM.seek(FileTableStart,0)
    if(ROM.read(8) != b'\x00\x00\x00\x00\x00\x00\x10\x60'):
        print('File table not found at expected location. Check for correct ROM.')
        return -1
    
    #If final entry is null, file table is too short
    ROM.seek(FileTableStart + 0x10 * NFiles,0)
    if(ROM.read(8) == b'\x00\x00\x00\x00\x00\x00\x00\x00'):
        print('File table shorter than expected. Check for correct ROM.')
        return -2
    
    #If final entry is not followed by null, file table is too long
    ROM.seek(FileTableStart + 0x10 * (NFiles + 1),0)
    if(ROM.read(8) != b'\x00\x00\x00\x00\x00\x00\x00\x00'):
        print('File table longer than expected. Check for correct ROM.')
        return -3
        
    print('File table verified.\n')
    return 1



def makeDEdict():
    EngToDebug = {}
    DebugToEng = {}
    
    with open('SceneDict.txt','r') as DictFile:
        for line in DictFile:
            [dbg,eng] = line.split(' ')
            EngToDebug[eng.strip()] = dbg
            DebugToEng[dbg] = eng.strip()
    
    return [EngToDebug,DebugToEng]



def makescenedict(ROMtype):
    
    ROMinfofile = ROMinfoDict.get(ROMtype,'Unknown')
    if(ROMinfofile == 'Unknown'):
        print('Unsupported ROM type')
        return [-1,-1]
    
    ROMinfo = open(ROMinfofile,'r')
    ROMinfo.readline()
    ROMarr = ROMinfo.readlines()
    ROMinfo.close()
    
    scenelist = []
    scenedict = {}
    
    for FileInfo in ROMarr:
        
        [FileIndex, FileName] = FileInfo.split(' ')
        
        if(FileName.strip().split('.')[1] != 'zscene'):
            continue
        
        scenelist.append(FileName.rsplit('_',1)[0])
        scenedict[FileName.rsplit('_',1)[0]] = int(FileIndex)
    
    return [scenelist,scenedict]



def getzmapinfo(zmapfilename):
    
    zmapfile = open(zmapfilename,'rb')
    zmap = zmapfile.read()
    zmapsize = zmapfile.tell()
    zmapfile.close()
    
    headertypes = zmap[0::8]
    headertypes = headertypes[0:headertypes.find(b'\x14')]
    
    if(headertypes.count(b'\x18')):
        print('Rooms with multiple setups currently not supported.')
        return -1
    
    collhdr = headertypes.find(b'\x0A')
    collstart = int.from_bytes(zmap[(collhdr*8 + 5):(collhdr*8 + 8)],'big')
    
    objhdr = headertypes.find(b'\x0B')
    numobjs = zmap[8*objhdr + 1]
    objstart = int.from_bytes(zmap[(objhdr*8 + 5):(objhdr*8 + 8)],'big')
    
    acthdr = headertypes.find(b'\x01')
    numactors = zmap[8*acthdr + 1]
    actstart = int.from_bytes(zmap[(acthdr*8 + 5):(acthdr*8 + 8)],'big')
    
    extraspace = int((0x1000 - (zmapsize % 0x1000))/0x10)
    
    normspace = int((collstart - objstart)/0x10)

    return [numactors, numobjs, normspace, extraspace]



def fixboot(ROMfilename):
    
    [ROMtype,FileTableStart,NFiles] = findROMtype(ROMfilename)
    
    return 1
    
    with open(ROMfilename,'rb+') as ROM:
        [codeind,startent,openingind,startcut,startmode] = BootDict[ROMtype]
        
        ROM.seek(FileTableStart + 0x10 * codeind,0)
        codestart = int.from_bytes(ROM.read(4),'big')
        
        ROM.seek(FileTableStart + 0x10 * openingind)
        openstart = int.from_bytes(ROM.read(4),'big')
        
        # [startent,startcut,startmode] = BootDict.get(ROMtype,'unknown')
        # codestart = 0
        # openstart = 0
        
        ROM.seek(codestart + startent - 2,0)
        if(ROM.read(2) != b'\x24\x0D'):
            print('Cannot change boot scene.')
            return -2
        ROM.seek(codestart + startent,0)
        ROM.write(b'\x00\xCD')
        ROM.seek(openstart + startcut,0)
        ROM.write(b'\xFF\xF3')
        ROM.seek(openstart + startmode,0)
        ROM.write(b'\x01')
    
    return 1



def loadtoroom(ROMfilename,entrance,sceneind,roomnum):
    
    [ROMtype,FileTableStart,NFiles] = findROMtype(ROMfilename)
    
    startent = 0x0;
    startcut = 0x0;
    
    if(ROMtype == 'Unknown'):
        print('Unsupported ROM type.')
        return -2
    
    with open(ROMfilename,'rb+') as ROM:
        
        ROM.seek(FileTableStart + 0x10 * sceneind)
        scenestart = int.from_bytes(ROM.read(4),'big')
        sceneend = int.from_bytes(ROM.read(4),'big')
        scenesize = sceneend - scenestart
        ROM.seek(scenestart)
        scenebytes = bytearray(ROM.read(scenesize))
        
        headertypes = scenebytes[0::8]
        headertypes = headertypes[0:headertypes.find(b'\x14')]
        
        if(headertypes.count(b'\x18')):
            print('Scenes with multiple setups currently not supported.')
            return -1
        
        transhdr = headertypes.find(b'\x0E')
        numtrans = scenebytes[8*transhdr + 1]
        transstart = int.from_bytes(scenebytes[(transhdr*8 + 5):(transhdr*8 + 8)],'big')
        
        spawnhdr = headertypes.find(b'\x00')
        numspawn = scenebytes[8*spawnhdr + 1]
        spawnstart = int.from_bytes(scenebytes[(spawnhdr*8 + 5):(spawnhdr*8 + 8)],'big')
        
        enthdr = headertypes.find(b'\x06')
        nument = numspawn
        entstart = int.from_bytes(scenebytes[(enthdr*8 + 5):(enthdr*8 + 8)],'big')
        
        roomhdr = headertypes.find(b'\x04')
        numrooms = scenebytes[8*roomhdr + 1]
        
        if((roomnum >= numrooms) or (roomnum < 0)):
            print('Room index out of range.')
            return -3
        
        scenebytes[entstart + 1] = roomnum
        
        for i in range(0,numtrans):
            
            tact = transstart + i*0x10
            
            if((scenebytes[tact] != roomnum) and (scenebytes[tact + 0x2] != roomnum)):
                continue
            if(scenebytes[tact + 0x5] == 0x23):
                continue
            
            
            xpos = int.from_bytes(scenebytes[(tact + 0x6):(tact + 0x8)],'big')
            ypos = int.from_bytes(scenebytes[(tact + 0x8):(tact + 0xA)],'big')
            zpos = int.from_bytes(scenebytes[(tact + 0xA):(tact + 0xC)],'big')
            yrot = scenebytes[tact + 0xC]
            
            
            if(scenebytes[tact] == roomnum):
                
                yrot = (yrot + 0x80) % 0x100
            
            
            if((yrot > 0xD0) or (yrot < 0x30)):
                zpos = (zpos + 50) % 0x10000
            elif((yrot > 0x50) and (yrot < 0xB0)):
                zpos = (zpos - 50) % 0x10000
            
            
            if((yrot > 0x10) and (yrot < 0x70)):
                xpos = (xpos + 50) % 0x10000
            elif((yrot > 0x90) and (yrot < 0xF0)):
                xpos = (xpos - 50) % 0x10000
            
            
            scenebytes[(spawnstart + 0x2):(spawnstart + 0x4)] = xpos.to_bytes(2,'big')
            scenebytes[(spawnstart + 0x4):(spawnstart + 0x6)] = ypos.to_bytes(2,'big')
            scenebytes[(spawnstart + 0x6):(spawnstart + 0x8)] = zpos.to_bytes(2,'big')
            scenebytes[spawnstart + 0xA] = yrot
            
            break
        
        ROM.seek(scenestart,0)
        ROM.write(scenebytes)
        
        [codeind,startent,openingind,startmode,startcut] = BootDict[ROMtype]
        
        ROM.seek(FileTableStart + 0x10 * codeind,0)
        codestart = int.from_bytes(ROM.read(4),'big')
        
        ROM.seek(FileTableStart + 0x10 * openingind)
        openstart = int.from_bytes(ROM.read(4),'big')
        
        # [startent,startcut,startmode] = BootDict.get(ROMtype,'unknown')
        # codestart = 0
        # openstart = 0
        
        ROM.seek(codestart + startent - 2,0)
        if(ROM.read(2) != b'\x24\x0D'):
            print('Load to room not supported in this ROM.')
            return -2
        ROM.seek(codestart + startent,0)
        ROM.write(entrance.to_bytes(2,'big'))
        ROM.seek(openstart + startcut,0)
        ROM.write(b'\x00\x00')
        ROM.seek(openstart + startmode,0)
        ROM.write(b'\x00')
    
    return 1



def compress(ROMfilename,Outfilename):
    
    [ROMtype,FileTableStart,NFiles] = findROMtype(ROMfilename)
    
    UncompInds = UncompIndsDict.get(ROMtype,'unknown')
    
    if(UncompInds == 'unknown'):
        print('Warning: Unknown ROM type. Assuming default compression scheme.')
        UncompInds = [0,1,2,3,4,5,6,7,8,9,15,16,17,18,19,20,21,22,23,24,25,26,942,944,946,948,950,952,954,956,958,960,962,964,966,968,970,972,974,976,978,980,982,984,986,988,990,992,994,996,998,1000,1002,1004]
    
    with open(ROMfilename,'rb') as decomp, open(Outfilename,'wb') as comp:
        
        decomp.seek(FileTableStart)
        VFileBegin = int.from_bytes(decomp.read(4),'big')
        VFileEnd = int.from_bytes(decomp.read(4),'big')
        FileIndex = 0
        
        while(VFileEnd != 0): #The end offset being zero indicates the end of the file table
            
            #Read in the decompressed file and prepare to write to the end of the compressed ROM
            
            VFileSize = VFileEnd - VFileBegin
            decomp.seek(VFileBegin)
            VFileBytes = decomp.read(VFileSize)
            comp.seek(0,2)
            PFileStart = comp.tell()
            
            if(UncompInds.count(FileIndex) == 1): #If the file is uncompressed, direct copy it
                PFileBytes = VFileBytes
                PFileEnd = 0
            else:
                PFileBytes = yaz0encBytes(VFileBytes) #read in compressed file
                ExtraBytes = len(PFileBytes) % 0x10 #check if compressed file is a whole number of lines
                
                if( ExtraBytes != 0):
                    PFileBytes += bytes(16 - ExtraBytes) #if not, make it so
                
                PFileEnd = PFileStart + len(PFileBytes) #record where the end of the physical file is
            
            comp.write(PFileBytes) #write the physical file to the compressed ROM
            
            if(FileIndex > 2): #fix the file table for files beyond it
                comp.seek(FileTableStart + 0x10 * FileIndex + 0x8)
                comp.write(PFileStart.to_bytes(4,'big'))
                comp.write(PFileEnd.to_bytes(4,'big'))
            
            print('Processed file %d' % FileIndex)
            
            FileIndex += 1
            decomp.seek(FileTableStart + 0x10 * FileIndex)
            VFileBegin = int.from_bytes(decomp.read(4),'big')
            VFileEnd = int.from_bytes(decomp.read(4),'big') #initialize for next file.
        
        comp.seek(0,2)
        filesize = comp.tell()
        
        if( filesize < 0x02000000 ): #pad ROM to 32MB
            padbytes = bytes(0x02000000 - filesize)
            comp.write(padbytes)
        elif( filesize > 0x02000000):
            print("Warning: Compressed ROM larger than 32MB")
    
    fixCRC(ROMfilename)
    
    return 1



def decompress(ROMfilename,Outfilename):
    
    with open(ROMfilename,'rb') as comp, open(Outfilename,'wb') as decomp:
        
        FileTableStart = findfiletable(comp)
        
        FileIndex = 0
        
        comp.seek(FileTableStart)
        VFileBegin = int.from_bytes(comp.read(4),'big')
        VFileEnd = int.from_bytes(comp.read(4),'big')
        PFileBegin = int.from_bytes(comp.read(4),'big')
        PFileEnd = int.from_bytes(comp.read(4),'big')        
        
        while(VFileEnd != 0): #The end offset being zero indicates the end of the file table
            
            comp.seek(PFileBegin)
            
            if(PFileEnd == 0): #A physical end offset of zero means the file is uncompressed
                VFileSize = VFileEnd - VFileBegin
                VFileBytes = comp.read(VFileSize)
            else:
                PFileSize = PFileEnd - PFileBegin
                PFileBytes = comp.read(PFileSize)
                VFileBytes = yaz0decBytes(PFileBytes)
                
            decomp.seek(0,2)
            WriteLocation = decomp.tell() #check if zero padding is needed.
            
            if(VFileBegin == WriteLocation):
                decomp.write(VFileBytes)
            elif(VFileBegin > WriteLocation):
                decomp.write(bytes(VFileBegin - WriteLocation))
                decomp.write(VFileBytes)
            else:
                print("Shit went wrong, yo.")
                return -2
            
            if(FileIndex > 2): #fix the file table for files beyond it
                decomp.seek(FileTableStart + 0x10 * FileIndex + 0x8)
                decomp.write(VFileBegin.to_bytes(4,'big'))
                decomp.write(bytes(4))
            
            print('Processed file %d' % FileIndex)
            
            FileIndex += 1
            
            comp.seek(FileTableStart + 0x10 * FileIndex)
            VFileBegin = int.from_bytes(comp.read(4),'big')
            VFileEnd = int.from_bytes(comp.read(4),'big')  
            PFileBegin = int.from_bytes(comp.read(4),'big')
            PFileEnd = int.from_bytes(comp.read(4),'big') #initialize for next file.
            
        decomp.seek(0,2)
        filesize = decomp.tell()
        
        if( filesize < 0x04000000 ): #pad ROM to 64MB
            padbytes = bytes(0x04000000 - filesize)
            decomp.write(padbytes)
    
    fixCRC(ROMfilename)
    
    return 1



def extractall(ROMfilename, filedirectory,debugnames):
    
    ROMtype = findROMtype(ROMfilename)
    
    ROMinfofile = ROMinfoDict.get(ROMtype[0],'unknown')
    
    if(ROMinfofile == 'unknown'):
        print('Unsupported ROM type')
        return -1
    
    if(debugnames == 0):
        [EngToDebug,DebugToEng] = makeDEdict()
    
    with open(ROMfilename, 'rb') as ROM, open(ROMinfofile,'r') as ROMinfo:
        
        #Read in initialization data
        [FileTableStart, NFiles] = [int(x,0) for x in ROMinfo.readline().split(' ')]
        
        #Check if correct ROM
        if(checkfiletable(ROM,FileTableStart,NFiles) != 1):
            return -2
        else:
            print('Beginning extraction.')
        
        FileInfo = ROMinfo.readline()
        
        while(FileInfo != ''):
            
            #Prepare to extract file
            FileIndex = int(FileInfo.split(' ')[0])
            FileName = FileInfo.split(' ')[1].strip()
            
            ROM.seek(FileTableStart + 0x10 * FileIndex,0)
            VFileBegin = int.from_bytes(ROM.read(4),'big')
            VFileEnd = int.from_bytes(ROM.read(4),'big')
            PFileBegin = int.from_bytes(ROM.read(4),'big')
            PFileEnd = int.from_bytes(ROM.read(4),'big')
            
            ROM.seek(PFileBegin,0)
            
            #If the file is compressed, decompress it
            if(PFileEnd == 0):
                VFileSize = VFileEnd - VFileBegin
                VFileBytes = ROM.read(VFileSize)
            else:
                PFileSize = PFileEnd - PFileBegin
                PFileBytes = ROM.read(PFileSize)
                VFileBytes = yaz0decBytes(PFileBytes)
            
            if(FileName == 'dmadata.zdata'):
                FileEntry = VFileBytes[0:8]
                NewFileBytes = b''
                FileIter = 0
                while(FileEntry != b'\x00\x00\x00\x00\x00\x00\x00\x00'):
                    NewFileBytes += (FileEntry + FileEntry[0:4] + b'\x00\x00\x00\x00')
                    FileIter += 1
                    FileEntry = VFileBytes[(FileIter * 0x10):(FileIter * 0x10 + 8)]
                
                NewFileBytes += VFileBytes[(FileIter * 0x10):]
                VFileBytes = NewFileBytes
            
            if(debugnames == 0):
                if(FileName.split('.')[1] == 'zmap'):
                    debugname = FileName.rsplit('_',2)[0]
                    FileName = FileName.replace(debugname,DebugToEng[debugname])
                elif(FileName.split('.')[1] == 'zscene'):
                    debugname = FileName.rsplit('_',1)[0]
                    FileName = FileName.replace(debugname,DebugToEng[debugname])
            
            
            #Create the extracted file
            ExFile = open(filedirectory + '/' + FileName,'wb')
            ExFile.write(VFileBytes)
            ExFile.close()
            
            #Load data for next file
            FileInfo = ROMinfo.readline()
    
    return 1



def injectall(ROMfilename, filedirectory,debugnames):
    
    ROMtype = findROMtype(ROMfilename)
    
    ROMinfofile = ROMinfoDict.get(ROMtype[0],'unknown')
    
    if(ROMinfofile == 'unknown'):
        print('Unsupported ROM type')
        return -1
    
    if(debugnames == 0):
        [EngToDebug,DebugToEng] = makeDEdict()
    
    with open(ROMfilename,'rb+') as ROM, open(ROMinfofile,'r') as ROMinfo:
        
        #Read in initialization info
        [FileTableStart, NFiles] = [int(x,0) for x in ROMinfo.readline().split(' ')]
        
        #Check for correct ROM
        if(checkfiletable(ROM,FileTableStart,NFiles) != 1):
            return -2
        
        if(os.path.isfile(filedirectory + '/dmadata.zdata')):
            TableFile = open(filedirectory + '/dmadata.zdata','rb')
            TableBytes = TableFile.read()
            dmastart = int.from_bytes(TableBytes[0x20:0x24],'big')
            if(dmastart != FileTableStart):
                print('dmatable does not match host ROM file table')
                return -3
        
        print('Beginning injection.')
        
        FileInfo = ROMinfo.readline()
        SceneName = '?????'
        
        while(FileInfo != ''):
            
            GoodFix = 0
            
            #Read in file info
            FileIndex = int(FileInfo.split(' ')[0])
            [FileName,FileExt] = FileInfo.split(' ')[1].strip().split('.')
            
            if(debugnames == 0):
                if(FileExt == 'zmap'):
                    dbgname = FileName.rsplit('_',2)[0]
                    FileName = FileName.replace(dbgname,DebugToEng[dbgname])
                elif(FileExt == 'zscene'):
                    dbgname = FileName.rsplit('_',1)[0]
                    FileName = FileName.replace(dbgname,DebugToEng[dbgname])
            
            #Check if file is present. If not, skip it.
            if(not os.path.isfile(filedirectory + '/' + FileName + '.' + FileExt)):
                FileInfo = ROMinfo.readline()
                continue
            
            #Read in file and prepare for injection
            VFile = open(filedirectory + '/' + FileName + '.' + FileExt, 'rb')
            VFileBytes = VFile.read()
            VFileSize = VFile.tell()
            VFile.close()
            
            ROM.seek(FileTableStart + 0x10 * FileIndex)
            VFileBegin = int.from_bytes(ROM.read(4),'big')
            VFileEnd = int.from_bytes(ROM.read(4),'big')
            
            NewFileEnd = VFileBegin + VFileSize
            
            ROM.seek(FileTableStart + 0x10 * (FileIndex + 1))
            NextFileBegin = int.from_bytes(ROM.read(4),'big')
            
            #Check if there's enough space to inject
            if((FileIndex != NFiles) and (NewFileEnd > NextFileBegin)):
                print(FileName + ' is too large to inject. Skipping.')
                FileInfo = ROMinfo.readline()
                continue
            
            #If it's a map file, we need to fix the scene file table
            if((FileExt == 'zmap') and (FileName.startswith(SceneName))):
                RoomIndex = int(FileName.split('_')[-1])
                FileTableHeader = SceneBytes[0::8].find(b'\x04')
                FileTableOffset = int.from_bytes(SceneBytes[(8*FileTableHeader + 5) :(8*FileTableHeader + 8)],'big') + 8 * RoomIndex
                OldEntry = SceneBytes[FileTableOffset:(FileTableOffset + 8)]
                NewEntry = VFileBegin.to_bytes(4,'big') + NewFileEnd.to_bytes(4,'big')
                SceneBytes = SceneBytes.replace(OldEntry,NewEntry)
                GoodFix = 1
            elif(SceneName != '?????'):
                ROM.seek(SceneBegin,0)
                ROM.write(SceneBytes)
                NewScene = open(filedirectory + '/' + SceneName + '_scene.zscene','wb')
                NewScene.write(SceneBytes)
                NewScene.close()
                print('End of scene ' + SceneName + '.')
                SceneName = '?????'
            
            #If it's a scene file, we prepare for the subsequent map files
            if(FileExt == 'zscene'):
                SceneBegin = VFileBegin
                SceneName = FileName.replace('_scene','')
                SceneBytes = VFileBytes
            
            #For non-map files, a change in size could be a problem
            if((NewFileEnd != VFileEnd) and (GoodFix == 0)):
                print('Warning: ' + FileName + "'s size has changed.\n" + \
                    'Other data tables may need modification.')
            
            #Inform the file table of the modified file
            ROM.seek(FileTableStart + 0x10*FileIndex + 4,0)
            ROM.write(NewFileEnd.to_bytes(4,'big'))
            
            #Inject file
            ROM.seek(VFileBegin,0)
            ROM.write(VFileBytes)
            print('Injected ' + FileName + ' successfully.')
            
            #Load data for next file
            FileInfo = ROMinfo.readline()
        
        if(SceneName != '?????'):
            ROM.seek(SceneBegin,0)
            ROM.write(SceneBytes)
            NewScene = open(filedirectory + '/' + SceneName + '_scene.zscene','wb')
            NewScene.write(SceneBytes)
            NewScene.close()
            print('End of scene ' + SceneName + '.')
            SceneName = '?????'
    
    #As a final step, fix the CRC
    fixCRC(ROMfilename)
    
    return 1







