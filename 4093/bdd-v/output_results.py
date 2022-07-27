import pandas as pd
import json, os
from sklearn.metrics import mean_squared_error
import math
import numpy as np
from statistics import mean


# rf_actual = pd.read_feather(path='./outputs.feather')
rf_predicted = pd.read_feather(path='./outputs.feather')

# Group prdicted speeds by video index
predicted_speed = {' ': [0, 0]}
for i in range(len(rf_predicted['output_speed'])):
    if rf_predicted['video_key'][i] not in predicted_speed:
        predicted_speed[rf_predicted['video_key'][i]] = [rf_predicted['output_speed'][i]]
    else:
        predicted_speed[rf_predicted['video_key'][i]].append(rf_predicted['output_speed'][i])
        
json_files = [pos_json for pos_json in os.listdir('./') if pos_json.endswith('.json')]
actual_speed = {' ': [0, 0]}
for i in range(len(json_files)):
    with open(str(i) + '.json', 'r') as f:
        gps = json.load(f)["gps"]

        for n in range(len(gps)):
            if i not in actual_speed:
                actual_speed[i] = [gps[n]["speed"]]
            else:
                actual_speed[i].append(gps[n]["speed"])

    # print(actual_speed[i])
    # print(predicted_speed[i])
    # print("\n\n\n")

result = []
for i in range(16):
    mse = np.square(np.subtract(actual_speed[i],predicted_speed[i][:len(actual_speed[i])])).mean()
    rmse = math.sqrt(mse)
    result.append(rmse)
    print("RMSE: ", str(i), " ", rmse)

print(mean(result))






# import pandas as pd
# import numpy as np
# from sklearn.metrics import mean_squared_error

# pd.set_option('display.max_rows', None, 'display.max_columns', None)

# readFrameOriginal = pd.read_feather(path='./outputs-o.feather')
# readFrameMy = pd.read_feather(path='./outputs.feather')

# # results[i] = np.sqrt(((readFrameMy - readFrameOriginal) ** 2).mean())
# with open('results-here.txt', 'r') as f:
	# speeds = f.readlines()

# int_speeds = [float(i) for i in speeds]
# avg = (sum(int_speeds) / len(int_speeds))

# print(np.sqrt(((readFrameOriginal["output_speed"].mean() - avg) ** 2).mean()))

# print(np.sqrt(((readFrameOriginal["output_speed"][0:4020] - int_speeds) ** 2).mean()))

# print("likelihood: ", readFrameMy["likelihood"].mean(), "\n")
# print("output_speed: ", readFrameMy["output_speed"].mean(), "\n")
#print("overlap: ", readFrameMy["overlap"].mean(), "\n")
# print("speed_x: ", readFrameMy["speed_x"].mean(), "\n")
# print("speed_y: ", readFrameMy["speed_y"].mean(), "\n")
# print("time_point: ", readFrameMy["time_point"].mean(), "\n")










# print(mean_squared_error-(readFrameMy["output_speed"], readFrameOriginal["output_speed"], squared=False))
	
#print(results)


# import pandas as pd
# import numpy as np
# from sklearn.metrics import mean_squared_error

# pd.set_option('display.max_rows', None, 'display.max_columns', None)

# readFrameOriginal = pd.read_feather(path='./outputs-o.feather')
# readFrameMy = pd.read_feather(path='./outputs.feather')


# test = [0] * 34903
# with open('results-here.txt', 'r') as f:
	 #speeds = f.readlines()

# for i in speeds:
	#test.append(i)
# print(len(test), len(readFrameMy["output_speed"]))

 #print(np.sqrt(((readFrameMy["output_speed"] - test) ** 2).mean()))
#print(mean_squared_error-(readFrameMy["output_speed"], readFrameOriginal["output_speed"], squared=False))
