#this one is like your scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print ("arg1: %r,arg2: %r" %(arg1, arg2))

#ok, that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))


#don't leave space at the calling of function
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
    
 