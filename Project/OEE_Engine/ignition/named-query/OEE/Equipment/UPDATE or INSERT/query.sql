UPDATE OEE_Equipment SET
	Name = :equipmentName,
	Enterprise = :enterprise,
	Site = :site,
	Area = :area,
	WorkCenter = :workCenter,
	WorkUnit = :workUnit,
	UDTPath = :udtPath
WHERE Id = :equipmentId

IF @@ROWCOUNT = 0
BEGIN

INSERT INTO OEE_Equipment (
	Id,
	Name,
	Enterprise,
	Site,
	Area,
	WorkCenter,
	WorkUnit,
	UDTPath
)
VALUES (
	:equipmentId,
	:equipmentName,
	:enterprise,
	:site,
	:area,
	:workCenter,
	:workUnit,
	:udtPath
)

END