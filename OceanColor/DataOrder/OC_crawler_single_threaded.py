import urllib.request
testfile = urllib.request.URLopener()
#import httplib
read_file = open('wanted.txt','r')
raw_lists = read_file.read()
urls = []

read_splited = raw_lists.split('<')
for i in range(1,len(read_splited)):
	urls.append(read_splited[i].split('>')[0])

print(urls)

k = 0
while(k < len(urls)):
	try: # This enables us to try downloading again if temporary network error occurs.
		filename = urls[k].split('?')[0].split('/')[-1]
		print ('Downloading ' + filename)
		testfile.retrieve(urls[k], 'Downloads/' + filename)
		k += 1
	except FileNotFoundError:
		print('***   File not found. Did you forget to make "Downloads" directory?   ***')
		break
	except:
		print('Temporary downloading error.')