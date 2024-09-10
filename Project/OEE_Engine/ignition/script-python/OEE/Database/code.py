# MIT License
#
# Copyright (c) 2024 Anthony Upton
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


def getDatabaseInfo():
	dataset = system.db.getConnectionInfo()
	return {column: dataset.getValueAt(0, column) for column in dataset.getColumnNames()}

def getDatabaseType():
	dataset = system.db.getConnectionInfo()
	return dataset.getValueAt(0, "DBType")

def updateContext(params):
	path = "OEE/{0}/UPDATE Context".format(getDatabaseType())
	system.db.runSFNamedQuery(path, params)

def updateEquipment(params):
	path = "OEE/{0}/UPDATE Equipment".format(getDatabaseType())
	system.db.runSFNamedQuery(path, params)

def updateProduction(params):
	path = "OEE/{0}/UPDATE Production".format(getDatabaseType())
	system.db.runSFNamedQuery(path, params)

def updateDowntime(params):
	path = "OEE/{0}/UPDATE Downtime".format(getDatabaseType())
	system.db.runSFNamedQuery(path, params)

def createSchema():
	path = "OEE/{0}/CREATE Schema".format(getDatabaseType())
	system.db.runSFNamedQuery(path)

def isSchemaLoaded():
	path = "OEE/{0}/SELECT Schema".format(getDatabaseType())
	dataset = system.db.runNamedQuery(path)
	tableNames = list(set([dataset.getValueAt(row, "TableName") for row in range(dataset.getRowCount())]))
	tables = ["OEE_Equipment", "OEE_Context", "OEE_Downtime", "OEE_Production"]
	return all([table in tableNames for table in tables])