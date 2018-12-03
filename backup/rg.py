import re

line = r'15.11.2018;16:39:01;\Bitrix\Main\Data\CacheEngineFiles::delayedDelete(2);;0.001088;'
re_date = r'\d{2}.\d{2}.\d{4}'
re_time = r'\d{2}:\d{2}:\d{2}'
re_runtime = r'\d.\d{6}'

date = re.search(re_date, line)
print(date[0] if date else 'Not found')

time = re.search(re_time, line)
print(time[0] if time else 'Not found')

runtime = re.search(re_runtime, line)
print(runtime[0] if runtime else 'Not found')
