def notNone(value, alt):
	if value is None: return alt
	return value

def uuid4():
	import uuid
	return str(uuid.uuid4()).upper()

class Equipment:
	def __init__(self, udtPath, timestamp):
		self.udtPath = udtPath
		self.timestamp = (timestamp if isinstance(timestamp, long) else system.date.toMillis(timestamp)) / 1000 * 1000
		self.data = system.tag.readBlocking([udtPath])[0].value
	
	def getUDTPath(self):
		return self.udtPath
	
	def getTimestampDateTime(self):
		return system.date.fromMillis(self.timestamp)
	
	def refreshData(self):
		self.data = system.tag.readBlocking([self.udtPath])[0].value
	
	#### /Info
	
	def getEquipmentId(self):
		return self.data["Info"]["EquipmentId"]
	
	def getEquipmentName(self):
		return self.data["Info"]["Name"]
	
	def getEnterprise(self):
		return self.data["Info"]["Enterprise"]
	
	def getSite(self):
		return self.data["Info"]["Site"]
	
	def getArea(self):
		return self.data["Info"]["Area"]
	
	def getWorkCenter(self):
		return self.data["Info"]["WorkCenter"]
	
	def getWorkUnit(self):
		return self.data["Info"]["WorkUnit"]
	
	
	#### /Logic/Context
	
	def getContextBeginDateTime(self):
		return system.date.fromMillis(notNone(self.data["Logic"]["Context"]["BeginDateTime"], self.timestamp))
	
	def getContextId(self):
		return self.data["Logic"]["Context"]["ContextId"]
	
	def getLogicEnabled(self):
		return self.data["Logic"]["Context"]["Enabled"]
	
	def getLogicIdealRateCount(self):
		return self.data["Logic"]["Context"]["IdealRateCount"]
	
	def getLogicIdealRateSeconds(self):
		return self.data["Logic"]["Context"]["IdealRateSeconds"]
	
	def getLogicLotNumber(self):
		return self.data["Logic"]["Context"]["LotNumber"]
	
	def getLogicMode(self):
		return self.data["Logic"]["Context"]["Mode"]
	
	def getLogicOperator(self):
		return self.data["Logic"]["Context"]["Operator"]
	
	def getLogicProduct(self):
		return self.data["Logic"]["Context"]["Product"]
	
	def getLogicShift(self):
		return self.data["Logic"]["Context"]["Shift"]
	
	def getLogicShiftBeginDateTime(self):
		return system.date.fromMillis(self.data["Logic"]["Context"]["ShiftBeginDateTime"]) if self.data["Logic"]["Context"]["ShiftBeginDateTime"] is not None else None
	
	def getLogicShiftEndDateTime(self):
		return system.date.fromMillis(self.data["Logic"]["Context"]["ShiftEndDateTime"]) if self.data["Logic"]["Context"]["ShiftEndDateTime"] is not None else None
	
	def getLogicUnits(self):
		return self.data["Logic"]["Context"]["Units"]
	
	def getLogicWorkOrder(self):
		return self.data["Logic"]["Context"]["WorkOrder"]
	
	def getLogicWorkOrderBeginDateTime(self):
		return system.date.fromMillis(self.data["Logic"]["Context"]["WorkOrderBeginDateTime"]) if self.data["Logic"]["Context"]["WorkOrderBeginDateTime"] is not None else None
	
	#### /Logic/Downtime
	
	def getDowntimeBeginDateTime(self):
		return system.date.fromMillis(self.data["Logic"]["Downtime"]["BeginDateTime"]) if self.data["Logic"]["Downtime"]["BeginDateTime"] is not None else None
	
	def getDowntimeContextId(self):
		return self.data["Logic"]["Downtime"]["ContextId"]
	
	def getDowntimeId(self):
		return self.data["Logic"]["Downtime"]["DowntimeId"]
	
	def getDowntimeEventDateTime(self):
		return system.date.fromMillis(self.data["Logic"]["Downtime"]["EventDateTime"]) if self.data["Logic"]["Downtime"]["EventDateTime"] is not None else None
	
	
	#### /Logic/Production
	
	def getProductionBadCount(self):
		return self.data["Logic"]["Production"]["BadCount"]
	
	def getProductionBeginDateTime(self):
		return system.date.fromMillis(notNone(self.data["Logic"]["Production"]["BeginDateTime"], self.timestamp))
	
	def getProductionContextId(self):
		return self.data["Logic"]["Production"]["ContextId"]
	
	def getProductionDowntimeSeconds(self):
		return self.data["Logic"]["Production"]["DowntimeSeconds"]
	
	def getProductionGoodCount(self):
		return self.data["Logic"]["Production"]["GoodCount"]
	
	def getProductionId(self):
		return self.data["Logic"]["Production"]["ProductionId"]
	
	def getProductionRuntimeSeconds(self):
		return self.data["Logic"]["Production"]["RuntimeSeconds"]
	
	def getProductionStopCount(self):
		return self.data["Logic"]["Production"]["StopCount"]
	
	
	#### /Logic
	
	def getDowntimeSeconds(self):
		return self.data["Logic"]["DowntimeTimer"]["Logic"]["ElapsedSeconds"] + ((self.timestamp - self.data["Logic"]["DowntimeTimer"]["Logic"]["Timestamp"]) / 1000 if self.data["Logic"]["DowntimeTimer"]["Logic"]["Value"] else 0)
	
	def getRuntimeSeconds(self):
		return self.data["Logic"]["RuntimeTimer"]["Logic"]["ElapsedSeconds"] + ((self.timestamp - self.data["Logic"]["RuntimeTimer"]["Logic"]["Timestamp"]) / 1000 if self.data["Logic"]["RuntimeTimer"]["Logic"]["Value"] else 0)
	
	def getStopCount(self):
		return self.data["Logic"]["StopCounter"]["Count"]
	
	
	
	
	#### /Context
	
	def getEnabled(self):
		return self.data["Context"]["Enabled"]
	
	def getIdealRateCount(self):
		return self.data["Context"]["IdealRateCount"]
	
	def getIdealRateSeconds(self):
		return self.data["Context"]["IdealRateSeconds"]
	
	def getLotNumber(self):
		return self.data["Context"]["LotNumber"]
	
	def getMode(self):
		return self.data["Context"]["Mode"]
	
	def getOperator(self):
		return self.data["Context"]["Operator"]
	
	def getProduct(self):
		return self.data["Context"]["Product"]
	
	def getShift(self):
		return self.data["Context"]["Shift"]
	
	def getShiftBeginDateTime(self):
		return system.date.fromMillis(self.data["Context"]["ShiftBeginDateTime"]) if self.data["Context"]["ShiftBeginDateTime"] is not None else None
	
	def getShiftEndDateTime(self):
		return system.date.fromMillis(self.data["Context"]["ShiftEndDateTime"]) if self.data["Context"]["ShiftEndDateTime"] is not None else None
	
	def getUnits(self):
		return self.data["Context"]["Units"]
	
	def getWorkOrder(self):
		return self.data["Context"]["WorkOrder"]
	
	def getWorkOrderBeginDateTime(self):
		return system.date.fromMillis(self.data["Context"]["WorkOrderBeginDateTime"]) if self.data["Context"]["WorkOrderBeginDateTime"] is not None else None
	
	
	#### /Production
	
	def getGoodCount(self):
		return self.data["Production"]["GoodCount"]
	
	def getBadCount(self):
		return self.data["Production"]["BadCount"]
	
	def getRunning(self):
		return self.data["Production"]["Running"]
	
	
	#### Data Processing Functions
	
	def updateProductionDatabase(self):
		if self.getProductionId() is None: return
		params = {
			"BeginDateTime": self.getProductionBeginDateTime(),
			"ContextId": self.getProductionContextId(),
			"DowntimeSeconds": self.getDowntimeSeconds() - self.getProductionDowntimeSeconds(),
			"EndDateTime": self.getTimestampDateTime(),
			"GoodCount": self.getGoodCount() - self.getProductionGoodCount(),
			"BadCount": self.getBadCount() - self.getProductionBadCount(),
			"ProductionId": self.getProductionId(),
			"RuntimeSeconds": self.getRuntimeSeconds() - self.getProductionRuntimeSeconds(),
			"StopCount": self.getStopCount() - self.getProductionStopCount()
		}
		OEE.Database.updateProduction(params)
	
	def updateProductionLogic(self):
		tags = {
			"BeginDateTime": self.getTimestampDateTime(),
			"ContextId": self.getContextId(),
			"DowntimeSeconds": self.getDowntimeSeconds(),
			"GoodCount": self.getGoodCount(),
			"BadCount": self.getBadCount(),
			"ProductionId": uuid4(),
			"RuntimeSeconds": self.getRuntimeSeconds(),
			"StopCount": self.getStopCount()
		}
		system.tag.writeBlocking([self.getUDTPath() + "/Logic/Production/" + key for key in tags.keys()], tags.values())
		self.refreshData()
	
	def updateContextDatabase(self):
		if self.getContextId() is None: return
		params = {
			"BeginDateTime": self.getContextBeginDateTime(),
			"ContextId": self.getContextId(),
			"EndDateTime": self.getTimestampDateTime(),
			"EquipmentId": self.getEquipmentId(),
			"IdealRateCount": self.getLogicIdealRateCount(),
			"IdealRateSeconds": self.getLogicIdealRateSeconds(),
			"LotNumber": self.getLogicLotNumber(),
			"Mode": self.getLogicMode(),
			"Operator": self.getLogicOperator(),
			"Product": self.getLogicProduct(),
			"Shift": self.getLogicShift(),
			"ShiftBeginDateTime": self.getLogicShiftBeginDateTime(),
			"ShiftEndDateTime": self.getLogicShiftEndDateTime(),
			"Units": self.getLogicUnits(),
			"WorkOrder": self.getLogicWorkOrder(),
			"WorkOrderBeginDateTime": self.getLogicWorkOrderBeginDateTime()
		}
		OEE.Database.updateContext(params)
	
	def updateContextLogic(self):
		
		lessThanOneMinute = system.date.minutesBetween(notNone(self.getContextBeginDateTime(), system.date.fromMillis(0)), self.getTimestampDateTime())<1
		
		tags = {
			"BeginDateTime": self.getContextBeginDateTime() if lessThanOneMinute else self.getTimestampDateTime(),
			"ContextId": self.getContextId() if lessThanOneMinute else uuid4(),
			"Enabled": self.getEnabled(),
			"IdealRateCount": self.getIdealRateCount(),
			"IdealRateSeconds": self.getIdealRateSeconds(),
			"LotNumber": self.getLotNumber(),
			"Mode": self.getMode(),
			"Operator": self.getOperator(),
			"Product": self.getProduct(),
			"Shift": self.getShift(),
			"ShiftBeginDateTime": self.getShiftBeginDateTime(),
			"ShiftEndDateTime": self.getShiftEndDateTime(),
			"Units": self.getUnits(),
			"WorkOrder": self.getWorkOrder(),
			"WorkOrderBeginDateTime": self.getWorkOrderBeginDateTime()
		}
		system.tag.writeBlocking([self.getUDTPath() + "/Logic/Context/" + key for key in tags.keys()], tags.values())
		self.refreshData()
	
	def updateDowntimeDatabase(self):
		if self.getDowntimeId() is None or self.getDowntimeBeginDateTime() is None: return
		params = {
			"BeginDateTime": self.getDowntimeBeginDateTime(),
			"ContextId": self.getDowntimeContextId(),
			"DowntimeId": self.getDowntimeId(),
			"EndDateTime": self.getTimestampDateTime(),
			"EventDateTime": self.getDowntimeEventDateTime()
		}
		OEE.Database.updateDowntime(params)
	
	def updateDowntimeLogic(self):
		if self.getRunning():
			tags = {
				"BeginDateTime": None,
				"ContextId": self.getContextId(),
				"DowntimeId": None,
				"EventDateTime": None
			}
		else:
			tags = {
				"BeginDateTime": self.getTimestampDateTime(),
				"ContextId": self.getContextId(),
				"DowntimeId": uuid4(),
				"EventDateTime": self.getTimestampDateTime() if self.hasDowntimeStateChanged() else self.getDowntimeEventDateTime()
			}
		system.tag.writeBlocking([self.getUDTPath() + "/Logic/Downtime/" + key for key in tags.keys()], tags.values())
		self.refreshData()
	
	
	def onEquipmentInfoChangedEvent(self):
		params = {
			"EquipmentId": self.getEquipmentId(),
			"Name": self.getEquipmentName(),
			"Enterprise": self.getEnterprise(),
			"Site": self.getSite(),
			"Area": self.getArea(),
			"WorkCenter": self.getWorkCenter(),
			"WorkUnit": self.getWorkUnit(), 
			"UDTPath": self.getUDTPath()
		}
		OEE.Database.updateEquipment(params)
	
	def hasContextDataChanged(self):
		return any([self.data["Context"][key] != self.data["Logic"]["Context"][key] for key in self.data["Context"].keys()]) or self.getContextId() is None
	
	def hasProductionContextChanged(self):
		return self.getProductionContextId() != self.getContextId()
	
	def hasProductionHourLapsed(self):
		return system.date.hoursBetween(self.getProductionBeginDateTime(), self.getTimestampDateTime())>=1 or system.date.getHour24(self.getProductionBeginDateTime()) != system.date.getHour24(self.getTimestampDateTime())
	
	def hasDowntimeStateChanged(self):
		if self.getRunning() and (self.getDowntimeId() is not None or self.getDowntimeBeginDateTime() is not None): return True
		if not self.getRunning() and (self.getDowntimeId() is None or self.getDowntimeBeginDateTime() is None): return True
		return False
	
	def hasDowntimeContextChanged(self):
		return self.getDowntimeContextId() != self.getContextId()
	
	
	def onEquipmentLogicUpdateEvent(self):
		### update currently active rows in database
		if self.getLogicEnabled():
			self.updateContextDatabase()
			self.updateDowntimeDatabase()
			self.updateProductionDatabase()
		
		### If context data has changed, start new Context row
		if self.hasContextDataChanged():
			self.updateContextLogic()
			if self.getLogicEnabled():
				self.updateContextDatabase()
		
		### If any downtime data has changed, start new Downtime row
		if self.hasDowntimeStateChanged() or self.hasDowntimeContextChanged():
			self.updateDowntimeLogic()
			if self.getLogicEnabled():
				self.updateDowntimeDatabase()
		
		### If any context data has changed, start new Production row
		if self.hasProductionContextChanged() or self.hasProductionHourLapsed():
			self.updateProductionLogic()
			if self.getLogicEnabled():
				self.updateProductionDatabase()







### END OF FILE