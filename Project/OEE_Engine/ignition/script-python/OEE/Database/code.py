def updateContext(params):
	path = "OEE/MSSQL/UPDATE Context"
	system.db.runSFNamedQuery(path, params)

def updateEquipment(params):
	path = "OEE/MSSQL/UPDATE Equipment"
	system.db.runSFNamedQuery(path, params)

def updateProduction(params):
	path = "OEE/MSSQL/UPDATE Production"
	system.db.runSFNamedQuery(path, params)

def updateDowntime(params):
	path = "OEE/MSSQL/UPDATE Downtime"
	system.db.runSFNamedQuery(path, params)

def createSchema():
	path = "OEE/MSSQL/CREATE Schema"
	system.db.runSFNamedQuery(path)

def isSchemaLoaded():
	path = "OEE/MSSQL/SELECT Schema"
	dataset = system.db.runNamedQuery(path)
	tableNames = list(set([dataset.getValueAt(row, "TableName") for row in range(dataset.getRowCount())]))
	tables = ["OEE_Equipment","OEE_Context","OEE_Downtime","OEE_Production"]
	return all([table in tableNames for table in tables])