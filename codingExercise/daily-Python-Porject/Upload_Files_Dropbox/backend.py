import requests
import dropbox
from dropbox import dropbox_client

cliente = dropbox_client.Dropbox('sl.CBctRz0PdSvTLIkCEn6nSWpEzpbHBwgkYKXfJ1VJ_XWFOjX7Wsv_qp6smFAEbwXXzATcqdpjdGMIpRDJ3xhWOSz2cl2lB_KVHrCLLaNrhKhJ6O0vnjTkR19MzKjQCrUv0A4nBipK1rcZ')
#print(cliente.account_info())

file_from = 'clear.png'
file_to = '/PythonUploadFile/analytics_lane.jpg'
dbx = dropbox.Dropbox('ACCESS_TOKEN')
dbx.files_upload(open(file_from, 'rb').read(), file_to)