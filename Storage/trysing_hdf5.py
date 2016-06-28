import subprocess
import timeit
import glob
import os

names = glob.glob("*.hdf5")
fob=open('result_hdf5.txt','a')
for n in names:
     methods=['python -m snappy -c '+n+' '+n+'.snappy','7z a -y '+n+'.7z '+n, 'zip '+n+'.zip '+n]
     methods2=['python -m snappy -d '+n+'.snappy'+' '+n,'7z e -y '+n+'.7z','unzip -o '+n+'.zip']

     i=0
     for m in methods:
	head=['snappy','7z','zip']
	new=['.snappy','.7z','.zip']
        
	def compress():
  		subprocess.call(m,shell=True)
	
   	timer3 = timeit.Timer(stmt='compress()', setup='from __main__ import compress')
   	tm3=str(min(timer3.repeat(repeat=1,number=5)))
   	print 'Time taken for compression using %s =' % head[i] + tm3
   	fob.write('Time taken for compression using %s =' % head[i] + tm3 + '\n')
   	newcom = n+new[i]
   	size=os.path.getsize(newcom)/1000000.0
   	print  head[i] + ' Compressed file size = ' + str(size) + ' mb'
   	fob.write( head[i] + ' Compressed file size = ' + str(size) + ' mb' + '\n')

   	def decompress():
		subprocess.call(methods2[i],shell=True)

  	timer4 = timeit.Timer(stmt='decompress()', setup='from __main__ import decompress')
   	tm4=str(min(timer4.repeat(repeat=1,number=5)))
  	print 'Time taken for decompression using %s =' % head[i] + tm4
   	fob.write('Time taken for decompression using %s =' % head[i] + tm4 + '\n\n')	
        i+=1
fob.close()
