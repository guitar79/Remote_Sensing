# Oceandata Downloader

## Instructions

- Place the list of wanted files to `wanted.txt` as
```
https://oceandata.sci.gsfc.nasa.gov/cgi/getfile/requested_files_2.tar?h=ocdist102&p=/data1/50d0f0708609985b/requested_files
https://oceandata.sci.gsfc.nasa.gov/cgi/getfile/requested_files_3.tar?h=ocdist102&p=/data1/50d0f0708609985b/requested_files
```
(Without `<` or `>`)

- Run `python3 OC_crawler_single_threaded.py`
	- Or simply `python3 OC*`

- To teminate the download, press `Ctrl+Z`.
