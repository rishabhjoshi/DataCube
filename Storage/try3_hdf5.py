import subprocess
import timeit
import glob
import os

names = glob.glob("*.hdf5")
fob=open('result_hdf5.txt','a')
for n in names:
	for num in [1,5,9]:	
	        fob.write('Filename = ' + n + '\n')
                fob.write('Compression index = '+str(num)+'\n')
		head=['gzip','bzip2','lzma','xz','lzop']
		i=0
		new=['.gz','.bz2','.lzma','.xz','.lzo']
		methods=['gzip -fqk'+str(num)+' '+n,'bzip2 -zfqk'+str(num)+' '+n,'lzma -zkfq'+str(num)+' '+n,'xz -zkfq'+str(num)+' '+n,'lzop -fq'+str(num)+' '+n ]
		
		methods2=['gzip -dkfq','bzip2 -dkfq','lzma -dkfq','xz -dkfq','lzop -df']
		
		for m in methods:
		   def compress():
		   	subprocess.call(m,shell=True)
	
		   timer = timeit.Timer(stmt='compress()', setup='from __main__ import compress')
	 	   tm=str(min(timer.repeat(repeat=1,number=5)))
		   print 'Time taken for compression using %s =' % head[i] + tm
		   fob.write('Time taken for compression using %s =' % head[i] + tm + '\n')
		   newcom = n + new[i]
	           size=os.path.getsize(newcom)/1000000.0
	           print  head[i] + ' Compressed file size = ' + str(size) + ' mb'
		   fob.write( head[i] + ' Compressed file size = ' + str(size) + ' mb' + '\n')

		   def decompress():
			subprocess.call(methods2[i] + ' ' + newcom,shell=True)
		   
		   timer2 = timeit.Timer(stmt='decompress()', setup='from __main__ import decompress')
		   tm2=str(min(timer2.repeat(repeat=1,number=5)))
		   print 'Time taken for decompression using %s =' % head[i] + tm2
		   fob.write('Time taken for decompression using %s =' % head[i] + tm2 + '\n\n')
		   i+=1
fob.close()
