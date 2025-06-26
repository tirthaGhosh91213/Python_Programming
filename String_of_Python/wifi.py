# import subprocess

# def get_wifi_profiles():
#     meta_data=subprocess.check_output(['netsh','wlan','show','profiles'])
#     data=meta_data.decode("utf-8")
#     # print(data)
#     data=data.split("\n")
#     names=[]
#     for line in data:
#         if"All user Profile      : " in line:
#             # print(line)
#          name= line.split(":")[1]
#          names.append(name[1:-1])

#         # print(names)    
                
#     return names

# for name in get_wifi_profiles():
#      data=subprocess.check_output(['netsh','wlan','show','profiles','name','key=clear'])
#      data2=data.decode("utf-8",errors="blackslashreplace")
#      data2=data2.split("\n")
#      names=[]
#      for line in data:          
#         if 'key Content' in line:
#          print(line)      

# import subprocess

# def get_wifi_profiles():
#     meta_data=subprocess.check_output(['netsh','wlan','show','profiles'])
#     data=meta_data.decode("utf-8")
#     # print(data)
#     data=data.split("\n")
#     names=[]
#     for line in data:
#         if"All user Profile      : " in line:
#             # print(line)
#          name= line.split(":")[1]
#          names.append(name[1:-1])

#         # print(names)    
                
#     return names

# for name in get_wifi_profiles():
#      meta_data=subprocess.check_output(['netsh','wlan','show','profiles','name','key=clear'])
#      data=data.decode("utf-8",errors="blackslashreplace")
#      data=data.split("\n")
#      names=[]
#      for line in data:          
#         if 'key Content' in line:
#           print(line)

# import subprocess

# def get_wifi_profiles():
#     meta_data=subprocess.check_output(['netsh','wlan','show','profiles'])
#     data=meta_data.decode("utf-8")
#     # print(data)
#     data=data.split("\n")
#     names=[]
#     for line in data:
#         if"All user Profile      : " in line:
#             # print(line)
#          name= line.split(":")[1]
#          names.append(name[1:-1])

#         # print(names)    
                
#     return names

# for name in get_wifi_profiles():
#      meta_data=subprocess.check_output(['netsh','wlan','show','profiles','name','key=clear'])
#      data=data.decode("utf-8",errors="blackslashreplace")
#      data=data.split("\n")
#      names=[]
#      for line in data:          
#         if 'key Content' in line:
#             print(line)
import subprocess

def get_wifi_profiles():
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    data = meta_data.decode("utf-8")
    data = data.split("\n")
    names = []
    for line in data:
        if "All User Profile" in line:
            name = line.split(":")[1].strip()
            names.append(name)
    return names

def get_wifi_password(profile_name):
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', 'name=' + profile_name, 'key=clear'])
    data = meta_data.decode("utf-8", errors="backslashreplace")
    data = data.split("\n")
    password = None
    for line in data:
        if 'Key Content' in line:
            password = line.split(":")[1].strip()
    return password

wifi_profiles = get_wifi_profiles()
for profile_name in wifi_profiles:
    password = get_wifi_password(profile_name)
    print(f"Wi-Fi Profile: {profile_name}, Password: {password}")
