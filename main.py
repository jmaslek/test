import time
import platform

print(platform.platform())

start_time = time.time()

import pandas 

end_time = time.time()
elapsed = end_time - start_time
print("Script execution took %.4f seconds" % round(elapsed, 4))
