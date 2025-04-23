import os
import shutil

#proabably need to pass in path as arg here to reuse recursivly
def handle_dir_copy(path, copy_destination_path = ""):
    if not os.path.exists(copy_destination_path):
        os.mkdir(copy_destination_path)


    
    #can single line this directly into for loop but for content check this is nice
    dir_contents = os.listdir(path)
    #print(f"dir_contents : {dir_contents} of path {path}")
    
    for content in dir_contents:

        cur_path = os.path.join(path, content)
        dest_path = os.path.join(copy_destination_path, content)
        
        #print(f"cur_path : {cur_path}")

        if os.path.isdir(cur_path):
            #this part will need to be recursive for unknown tree depths
            #print(f"{content} : is dir")
            #TODO this will need to make a directory first
            #os.mkdir(dest_path)
            #this moved to top of function

            handle_dir_copy(cur_path, dest_path)
            #cur_path_contents = os.listdir(cur_path)
        elif os.path.isfile(cur_path):
            shutil.copy(cur_path, dest_path)
            #print(f"{content} : is file")
            #this will turn into a write to new location function call

        else:
            print(f"{content} : is something else, probably evil too")