import subprocess

print("options",
      "1. Cutvideo",
      "2.Get Duration")

value=int(input("what do you wanna do?"))



def cutter(file_name,start,duration):
   try:
    subprocess.run([
        "ffmpeg",
        "-ss",start,
        "-i",file_name,
        "-t",duration,
        "output.mp4"
    ],check=True)
    print("video cut successfully")

   except subprocess.CalledProcessError:
    print("error")

if value==1:
    file_name=input("enter file name:")
    start=input("time stamp for starting point:")
    duration=input("duration for cut:")
    cutter(file_name,start,duration)

def get_duration(file_name):
    try:
        subprocess.run([
    "ffprobe","-v","error","-show_entries","format=duration","-of","default=noprint_wrappers=1:nokey=1", file_name
    ])
    except subprocess.CalledProcessError:
       print("cant do this")

if value==2:
    
    video=input("which videos duration you want?")
    get_duration(video)