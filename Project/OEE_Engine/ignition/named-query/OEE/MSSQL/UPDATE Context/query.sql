UPDATE OEE_Context SET
	 BeginDateTime = :BeginDateTime
	,EndDateTime = :EndDateTime
	,EquipmentId = :EquipmentId
	,IdealRateCount = :IdealRateCount
	,IdealRateSeconds = :IdealRateSeconds
	,LotNumber = :LotNumber
	,Mode = :Mode
	,Operator = :Operator
	,Product = :Product
	,Shift = :Shift
	,ShiftBeginDateTime = :ShiftBeginDateTime
	,ShiftEndDateTime = :ShiftEndDateTime
	,Units = :Units
	,WorkOrder = :WorkOrder
	,WorkOrderBeginDateTime = :WorkOrderBeginDateTime
WHERE ContextId = :ContextId

IF @@ROWCOUNT = 0
BEGIN

INSERT INTO OEE_Context (
	 BeginDateTime
	,ContextId
	,EndDateTime
	,EquipmentId
	,IdealRateCount
	,IdealRateSeconds
	,LotNumber
	,Mode
	,Operator
	,Product
	,Shift
	,ShiftBeginDateTime
	,ShiftEndDateTime
	,Units
	,WorkOrder
	,WorkOrderBeginDateTime
)
VALUES (
	 :BeginDateTime
	,:ContextId
	,:EndDateTime
	,:EquipmentId
	,:IdealRateCount
	,:IdealRateSeconds
	,:LotNumber
	,:Mode
	,:Operator
	,:Product
	,:Shift
	,:ShiftBeginDateTime
	,:ShiftEndDateTime
	,:Units
	,:WorkOrder
	,:WorkOrderBeginDateTime
)

END