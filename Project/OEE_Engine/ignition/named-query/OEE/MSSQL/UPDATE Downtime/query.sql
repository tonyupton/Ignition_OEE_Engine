UPDATE OEE_Downtime SET
	 BeginDateTime = :BeginDateTime
	,EndDateTime = :EndDateTime
	,ContextId = :ContextId
	,EventDateTime = :EventDateTime
WHERE DowntimeId = :DowntimeId

IF @@ROWCOUNT = 0
BEGIN

INSERT INTO OEE_Downtime (
	 DowntimeId
	,BeginDateTime
	,EndDateTime
	,ContextId
	,EventDateTime
)
VALUES (
	 :DowntimeId
	,:BeginDateTime
	,:EndDateTime
	,:ContextId
	,:EventDateTime
)
END