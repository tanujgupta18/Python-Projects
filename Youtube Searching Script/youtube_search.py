import pywhatkit as pwk
def main():
    videoName = input("Search: ")
    pwk.playonyt(videoName) 
    
try:
    main()
except:
    print("An unexpected error occurred")
finally:
    print("Script closed")
