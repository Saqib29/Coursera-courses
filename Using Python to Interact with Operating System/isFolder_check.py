# os.path.isdir() to see the contents in the list directory or not!?
# we need to join os.path.join() to create the full path of the contents of that folder

import os

dir = "images"
for name in os.listdir(dir):
    #fullname = dir+"/"+name  ----   instead we can use like below
    fullname = os.path.join(dir, name) # but adding thios function we make sure that our join
                                      # function works with all operating sysrtems as windows
                                      # split filders with it's contents with "\" where Linux
                                      # & mac OS do with "/"
    if os.path.isdir(fullname):
        print("{} is a folder".format(name))
    else:
        print("{} is a file".format(name))


