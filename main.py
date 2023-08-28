import os
def getFile():
  j=input("Enter the file name: ")
  m=input("What do you wanna do with this file? ")
  if m=="content":
    try:
     with open(j) as f:
      j=f.read() 
      print(f"file content is '{j}'")
    except:
     print("Error file not found") 
  elif m=="delete":
    try:
     os.remove(j)
     print("File sucessfully Deleted")
    except:
     print("File does not exist")
  else:
    print("invalid command")
getFile()
