#-*- codeing = utf-8 -*-
#@Time : 2020/5/15 17:58
#@Author : navy
#@File : Bpoolback.py
#@Software: PyCharm

import oss2
auth = oss2.Auth('LTAI4G1zALWs13Ea5e81r1rr', 'ovpxKM7Kq4W0KauOgejp04tXoRVvna')
bucket = oss2.Bucket(auth, 'oss-ap-southeast-1.aliyuncs.com', 'bpool')
key = 'bpool.VMDK'
filename = 'bpool.VMDK'
oss2.resumable_download(bucket, key, filename,
                        store=oss2.ResumableDownloadStore(root='/tmp'),
                        multiget_threshold=1000*1024*1024,
                        part_size=50*1024*1024,
                        num_threads=4)

