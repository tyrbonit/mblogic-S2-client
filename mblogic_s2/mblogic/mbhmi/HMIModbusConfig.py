##############################################################################
# Project: 	MBLogic
# Module: 	HMIModbusConfig.py
# Purpose: 	Validate Modbus specific HMI parameters..
# Language:	Python 2.5
# Date:		09-May-2009.
# Ver.:		19-Jul-2010.
# Copyright:	2009 - 2010 - Michael Griffin       <m.os.griffin@gmail.com>
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

from mbprotocols import MBAddrTypes

##############################################################################

class HMIConfigValidator:
	"""Provide a class to validate HMI configuration parameters which are
	specific to a particular data provider. This one validates to 
	Modbus data types.
	"""

	########################################################
	def __init__(self):
		pass


	########################################################
	def ValidDataTypes(self):
		"""Return a list of the valid data types. These must include
		['boolean', 'integer', 'float']
		"""
		return ['boolean', 'integer', 'float', 'string']


	########################################################
	def DefaultIntRange(self):
		"""Returns a tuple containing the maximum and minimum
		default integers. This provides default values
		in the event they are not specified in the configuration.
		"""
		return 32767, -32768


	########################################################
	def AddrTypeIsValid(self, addrtype):
		"""Tests the 'addrtype' parameter.
		Returns True if addrtype is a valid address type.
		"""
		return addrtype in ['coil', 'discrete',
			'holdingreg', 'inputreg',
			'holdingreg32', 'inputreg32',
			'holdingregfloat', 'inputregfloat',
			'holdingregdouble', 'inputregdouble',
			'holdingregstr8', 'holdingregstr16',
			'inputregstr8', 'inputregstr16'
			]

	########################################################
	def TagAddrClass(self, addrtype):
		"""Classifies the address type as 'scale', 'boolean', or
		'string' to determine whether they require scaling parameters. 
		"""
		if addrtype in ['coil' ,'discrete']:
			return 'boolean'
		elif addrtype in ['holdingreg', 'inputreg', 
				'holdingreg32', 'inputreg32',
				'holdingregfloat', 'inputregfloat',
				'holdingregdouble', 'inputregdouble']:
			return 'scale'
		elif addrtype in ['holdingregstr8', 'holdingregstr16', 
				'inputregstr8', 'inputregstr16']:
			return 'string'
		else:
			return 'unknown'


	########################################################
	def MemAddrIsValid(self, memaddr, addrtype):
		"""Tests the 'memaddr' parameter.
		Returns a boolean flag and the formatted memory address.
		The flag is True if the address is of the correct type and
		within range. The memory address is returned as an integer
		if it could be converted, or None if not.
		"""
		try:
			memval = int(memaddr)
		except:
			return False, None

		return ((memval >= 0) and (memval <= MBAddrTypes.MaxExtAddrTypes[addrtype])), memval


	########################################################
	def AlarmEventAddrIsValid(self, base, memaddr):
		"""Parameters: base (string) = The base address to be
			converted to integer and added to memaddr.
		memaddr (string) = The alarm or event number
			to be converted to integer and added to base.
		Alarms and events are mapped to coil addresses.
		Returns a boolean flag and the formatted alarm or
		event memory address. 
		The flag is True if the address is of the correct type and
		within range. The memory address is returned as an integer
		if it could be converted, or None if not.
		
		"""
		try:
			memval = int(memaddr) + int(base)
		except:
			return False, None

		return ((memval >= 0) and (memval <= MBAddrTypes.MaxBasicAddrTypes['coil'])), memval

	########################################################
	def AlarmEventUseBase(self):
		"""Returns True if the base address is required for alarms
		and events, False otherwise.
		"""
		return True

############################################################


