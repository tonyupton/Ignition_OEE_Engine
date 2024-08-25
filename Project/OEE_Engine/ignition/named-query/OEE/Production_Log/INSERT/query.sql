INSERT INTO OEE_Production_Log
(
Id, EquipmentId, BeginDateTime, EndDateTime, Shift, Operator, Mode,
Product, WorkOrder, LotNumber, OptimalRate,
ProducedCount, ConsumedCount, RejectedCount, StopCount,
RuntimeSeconds, DowntimeSeconds, ProductionSeconds
)
VALUES (
:productionLogId, :equipmentId, :beginDateTime, :endDateTime, :shift, :operator, :mode,
:Product, :workOrder, :lotNumber, :optimalRate,
:producedCount, :consumedCount, :rejectedCount, :stopCount,
:runtimeSeconds, :downtimeSeconds, :productionSeconds
)