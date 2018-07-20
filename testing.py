import time
import piplates.DAQCplate as DAQC
# sudo pip install pi-plates

# The user guide for the DAQCplate:
# https://pi-plates.com/daqc-users-guide/

addr = 0            # Address of the DAQCplate. Default is zero.
channel_in = 0      # The input ADCchannel we are using on the DAQCplate
time_to_wait = 1.0  # Time (in seconds) to wait until next read.

# Read data from the ADC, print to screen, and then wait time_to_wait for the
# next read.

# Note that time.sleep should put the RPi to sleep (put processes on hold?) so
# there may be other overhead causing irregular read times regardless of what
# time_to_read is set to. One way around this could be to use a timing
# interrupt (if one exists) like a timer counter in order to ensure a more
# consistent stream of data. As is the timing *could* be off by milliseconds.
while(1):
    data_in = DAQC.getADC(addr, channel_in)
    print(data_in)
    time.sleep(time_to_wait)


# There is also an auto logging system designed specifically for the DAQCplate.
# This requires downloading some more libraries and programs to launch from
# the RPi's terminal.
# There is an additional online version but needs some type of registration.
# https://pi-plates.com/examples/#DAQCplateDemonstration_Code_Written_in_TKinter
# https://pi-plates.com/pplogger-an-open-source-multi-channel-data-logger-for-the-raspberry-pi/
