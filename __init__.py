# https://forum.ableton.com/viewtopic.php?f=1&t=200513

from cmd_mm1 import CMDMM1       # you import your main program during the initialisation of your script

def create_instance(c_instance):    # this function tells live that you create a new midi remote script
    return CMDMM1(c_instance)     # the initialisation result is the calling of the main function of your script.
