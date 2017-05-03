import urllib.request
testfile = urllib.request.URLopener()

urls = [x.replace('\n','') for x in open('wanted.txt','r').readlines()]

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

print('Completed downloading ' + str(len(urls)) + ' file(s).')