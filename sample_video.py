# -*- coding: utf-8 -*-
import os
import cv2
import argparse

#Example :python sample_video.py --outdir ./002 --file ./3186.mp4

parser = argparse.ArgumentParser(description='Process some integers.')
# enter the output dir path
parser.add_argument('--outdir', type=str, required = True, help='enter the output dir path')
# enter the target file path
parser.add_argument('--file', type=str, required = True, help='enter the target file path')
# enter the sample rate (_ frame per second)
parser.add_argument('--sam', type=int, default=1 , help='enter the sample rate')


args = parser.parse_args()


def main():
    if not os.path.isdir(args.outdir):
        os.mkdir(args.outdir)
    
    cap = cv2.VideoCapture(0)
    
    if cap.open(args.file):
        fps = cap.get(cv2.CAP_PROP_FPS)
        if fps <args.sam:
            print('Sample rate to high(> video fps)')
            return 
        #    frames per capture
        fpc = int(fps/args.sam)  
    else:
        print('Video File does not exist')
        return
        
    count = 0
    id_ct = 1
    
    while(True):    
        ret, img = cap.read()    
        if ret == False:
            break
        else :
            if count>=fpc:
                print('Write file:' + os.path.join(args.outdir,str(id_ct)+'.jpg'))
                cv2.imwrite(os.path.join(args.outdir,str(id_ct)+'.jpg'),img)
                count=0
                id_ct+=1
            else:
                count+=1
                
                
            

if __name__ == '__main__':
    main()