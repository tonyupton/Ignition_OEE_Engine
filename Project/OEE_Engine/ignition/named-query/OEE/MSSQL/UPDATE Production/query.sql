UPDATE OEE_Production SET
	 BeginDateTime = :BeginDateTime
	,ContextId = :ContextId
	,DowntimeSeconds = :DowntimeSeconds
	,EndDateTime = :EndDateTime
	,GoodCount = :GoodCount
	,BadCount = :BadCount
	,RuntimeSeconds = :RuntimeSeconds
	,StopCount = :StopCount
WHERE ProductionId = :ProductionId

IF @@ROWCOUNT = 0
BEGIN

INSERT INTO OEE_Production (
	 BeginDateTime
	,ContextId
	,DowntimeSeconds
	,EndDateTime
	,GoodCount
	,BadCount
	,ProductionId
	,RuntimeSeconds
	,StopCount
)
VALUES (
	 :BeginDateTime
	,:ContextId
	,:DowntimeSeconds
	,:EndDateTime
	,:GoodCount
	,:BadCount
	,:ProductionId
	,:RuntimeSeconds
	,:StopCount
)
END