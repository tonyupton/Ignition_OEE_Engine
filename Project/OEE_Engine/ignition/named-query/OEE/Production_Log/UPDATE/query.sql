UPDATE OEE_Production_Log SET 
EndDateTime = :endDateTime,
ProducedCount = :producedCount,
ConsumedCount = :consumedCount,
RejectedCount = :rejectedCount,
StopCount = :stopCount,
RuntimeSeconds = :runtimeSeconds,
DowntimeSeconds = :downtimeSeconds,
ProductionSeconds = :productionSeconds
WHERE Id = :productionLogId