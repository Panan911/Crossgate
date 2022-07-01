import zhconv

# 繁体转gb18030
job = "抓貓"
job = job.encode('big5').decode('gb18030')
print(job)

# 繁体转big5
job = "牛肉"
job = job.encode('gb18030').decode('big5')
print(job)

# 简体转繁体
job = "見習弓箭手"
job = zhconv.convert(job, 'zh-cn')
print(job)

#繁体转简体
# job = "遊民"
# job = job.encode('big5').decode('gb18030').encode("gbk").decode("gb18030")
# print(job)