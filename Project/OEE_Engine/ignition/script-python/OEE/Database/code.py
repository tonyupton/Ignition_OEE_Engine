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