import time
import platform

print(platform.platform())

start_time = time.time()

import pandas 

end_time = time.time()
print("Script execution took %d seconds" % (end_time - start_time))
