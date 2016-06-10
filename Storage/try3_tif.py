import subprocess
import timeit
import glob
import os

names = ['first.nc']
fob=open('resultnc.txt','a')
for n in names:
	for num in [1]:	
	        fob.write('Filename = ' + n + '\n')
                fob.write('Compression index = '+str(num)+'\n')
		head=['gzip','bzip2','lzma','xz','lzop','lbzip2','pigz','pigz_zlib','pbzip2']
		i=0
		new=['.gz','.bz2','.lzma','.xz','.lzo','.bz2','.gz','.zz','.bz2']
		methods=['gzip -fq'+str(num)+' '+n,'bzip2 -zfqk'+str(num)+' '+n,'lzma -zkfq'+str(num)+' '+n,'xz -zkfq'+str(num)+' '+n, 'lzop -fq'+str(num)+' '+n, 'lbzip2 -zkfq'+str(num)+' '+n, 'pigz -kfq'+str(num)+' '+n, 'pigz -zkfq'+str(num)+' '+n, 'pbzip2 -zqfk'+str(num)+' '+n]
		
		methods2=['gzip -dfq','bzip2 -dkfq','lzma -dkfq','xz -dkfq','lzop -df','lbzip2 -dkfq','pigz -dkfq','pigz -dkfq','pbzip2 -dqfk']
		
		for m in methods:
		   def compress():
		   	subprocess.call(m + ' ' + n,shell=True)
	
		   timer = timeit.Timer(stmt='compress()', setup='from __main__ import compress')
	 	   tm=str(min(timer.repeat(repeat=1,number=10)))
		   print 'Time taken for compression using %s =' % head[i] + tm
		   fob.write('Time taken for compression using %s =' % head[i] + tm + '\n')
		   newcom = n + new[i]
	           size=os.path.getsize(newcom)/1000000.0
	           print  head[i] + ' Compressed file size = ' + str(size) + ' mb'
		   fob.write( head[i] + ' Compressed file size = ' + str(size) + ' mb' + '\n')

		   def decompress():
			subprocess.call(methods2[i] + ' ' + newcom,shell=True)
		   
		   timer2 = timeit.Timer(stmt='decompress()', setup='from __main__ import decompress')
		   tm2=str(min(timer2.repeat(repeat=1,number=10)))
		   print 'Time taken for decompression using %s =' % head[i] + tm2
		   fob.write('Time taken for decompression using %s =' % head[i] + tm2 + '\n\n')
		   i+=1
fob.close()
