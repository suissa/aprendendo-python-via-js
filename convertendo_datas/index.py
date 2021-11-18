import time
  
ts = time.time()
print(ts)

from datetime import date

date01 = date.fromtimestamp(ts)
print(date01)

# esse timedelta não fez muito sentido a sua nomenclatura
from datetime import timedelta
dt = date.today() - timedelta(5)
print(dt)