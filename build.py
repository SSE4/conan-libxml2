import os
import platform
import sys

if __name__ == "__main__":
    os.system('conan export lasote/stable')
   
    def test(settings):
        argv =  " ".join(sys.argv[1:])
        command = "conan test %s %s" % (settings, argv)
        retcode = os.system(command)
        if retcode != 0:
            exit("Error while executing:\n\t %s" % command)

#       
#     # Static x86
#     test('-s arch=x86 -s build_type=Debug -o libxml2:shared=False')
#     test('-s arch=x86 -s build_type=Release -o libxml2:shared=False')
#     # Shared x86
#     test('-s arch=x86 -s build_type=Debug -o libxml2:shared=True')
#     test('-s arch=x86 -s build_type=Release -o libxml2:shared=True')
# 
#    

    # Shared x86_64
    test('-s arch=x86_64 -s build_type=Debug -o libxml2:shared=True')
    test('-s arch=x86_64 -s build_type=Release -o libxml2:shared=True')
 
    # Static x86_64
    test('-s arch=x86_64 -s build_type=Debug -o libxml2:shared=False')
    test('-s arch=x86_64 -s build_type=Release -o libxml2:shared=False')
 
   