import time
  
ts = time.time()
print(ts * 1000)

from datetime import datetime

date01 = datetime.fromtimestamp(ts)
print(date01)