#TODO: Make one  that fucntions system wide
import os
def main():
    while True:
        current_path  = os.path.abspath(os.getcwd())
        print(current_path)
        download_folder = r"C:\Users\PC\Downloads"
        user_file = (os.path.basename(input("Enter the file name: "))).strip('"')
        confirmation = input(f"Are you sure {user_file} is the correct file/folder?(Type y to confirm, n to cancel, anything else to exit. ): ")
        if confirmation =="y":
            current_path = os.path.join(current_path,user_file)
            file_destination = os.path.join(download_folder,user_file)
            os.rename(file_destination,current_path)
        elif confirmation == "n":
            continue
      
if __name__ == "__main__":
    main()