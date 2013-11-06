##############################################################################
# Project: 	SeegridS2Client
# Module: 	replayData__.py
# Purpose: 	Playsback recorded data from the truck's modbus server to be able to drive the truck through this recorded path through calculated speeds.
# Language:	Python 2.5
# Date:		06-Nov-2013.
# Ver.:		06-Nov-2013.
# Copyright:	2013 - 2014 - S. Selvam Raju @SEEGRID corp.       <sraju@seegrid.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# Important:	WHEN EDITING THIS FILE, USE TABS TO INDENT - NOT SPACES!
##############################################################################

# Name of this program.
_SOFTNAME = 'ModbusReplayRouteData'

# Version of this server.
_VERSION = '06-November-2013'

_HelpStr = """
%s, %s
This module takes the truck through a route recorded previously in the truckData.dat file by calculating speeds and following steering turns at corresponding encoder values. The calculated speeds and tiller angles are written to the modbus registers and the modbus server takes necessary action to run the truck.
Just like the standard clients this client has to be started with the command line parameters (which are supposed to be the same as those in the MBClient and this program should run on the same computer that runs the standard client.

Any parameters which are not specified will use their default values. 
These include:

-p Port number of HMI web server. The default is 8082.
-h Name or address of remote server. The default is localhost.
-r Port number of remote server. The default is 502.
-u Unit ID of remote server. The default is 1. (This is Modbus specific).
-t Timeout for communications. The default is 5.0 seconds.
-e hElp. (this screen).

This program is automatically setup to get the command line parameters sent to the standard MBClient and none of the above parameters need to be passed to this program seperately.
""" % (_SOFTNAME, _VERSION)

############################################################

import time
import sys
import os
import math

import ModbusClient
import HMIServerCommon
from mbprotocols import ModbusExtData


############################################################

# Get the command line parameter options.
#CmdOpts = HMIServerCommon.GetOptionsClient(502, _HelpStr)


############################################################


# Initialise the client. First get the remote host parameters.
#hbhost, hbport, hbtimeout, hbunitid = CmdOpts.GetRemoteParams()


#Initialize an instance of the ModbusClient.DataTableAccess to initialize this client.

#HBClient = ModbusClient.DataTableAccess(hbhost, hbport, hbtimeout, hbunitid)

#HBClient1 = ModbusClient.DataTableAccess('192.168.10.237', 1502, 5.0, 1)
replayDataClient1 = ModbusClient.DataTableAccess('10.0.0.100', 1502, 5.0, 1)

ExtData4 = ModbusExtData.ExtendedDataTypes(replayDataClient1)

############################################################



#file2 = open("truckHeading.dat","w")
#file2.close()

file = open("truckData.dat","r")
file.readline()
file.readline()

data = [map(float, line.split()) for line in file]
data_end = len(data)-1

truckspeed = 700

i = 0

#Can try with file open here

while i < data_end

	i=i+1;


####ALGO

#read truck speed





while True:

	i = i+1
	valVF = ExtData3.GetInpRegFloat32(20)
	valVL = ExtData3.GetInpRegFloat32(22)
	truckHeading = recDataClient1.GetInputRegistersInt(18)
	tractionEncoder = recDataClient1.GetInputRegistersInt(12)
	tillerAngle = ExtData3.GetInpRegFloat32(44)

	print tractionEncoder

	file.write( str(i) + '\t' + str(valVF) + '\t' + str(valVL) + '\t' + str(truckHeading) + '\t' + str(tractionEncoder) + '\t' + str(tillerAngle) + '\n' )
	time.sleep(0.5)

	file.close()		

	file = open("truckData.dat","a")			

#		print "Here"
#print "Here2"
#Loop exits when program is terminated 
