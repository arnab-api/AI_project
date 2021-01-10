import os

# print(os.listdir("AudioFeatureExtractorV2"))
# print(os.stat("AudioClassifierMicro.tflite").st_size)

# print(os.path.isfile("AudioClassifierMicro.tflite"))
# print(os.path.isfile("AudioFeatureExtractorV2"))

def byte2mb(val):
    val /= 1024
    val /= 1024

    return val

def rec(root_path):
    if(os.path.isfile(root_path)):
        sz = os.stat(root_path).st_size
        print(">>> ", root_path, ":: ", sz, " :: ", byte2mb(sz))

        if(byte2mb(sz) > 100):
            danger.append((root_path, byte2mb(sz)))

        return 

    child_arr = os.listdir(root_path)
    for child in child_arr:
        sub_path = root_path + "/" + child
        rec(sub_path)

    return

danger = []

###################################################
rec("AI Mridul")
###################################################

if(len(danger) == 0):
    print("OK to push")
else:
    print("-------- NOT OK --------")
    for d in danger:
        print(d)