UPDATE OEE_Equipment SET
	Name = :Name,
	Enterprise = :Enterprise,
	Site = :Site,
	Area = :Area,
	WorkCenter = :WorkCenter,
	WorkUnit = :WorkUnit,
	UDTPath = :UDTPath
WHERE EquipmentId = :EquipmentId

IF @@ROWCOUNT = 0
BEGIN

INSERT INTO OEE_Equipment (
	EquipmentId,
	Name,
	Enterprise,
	Site,
	Area,
	WorkCenter,
	WorkUnit,
	UDTPath
)
VALUES (
	:EquipmentId,
	:Name,
	:Enterprise,
	:Site,
	:Area,
	:WorkCenter,
	:WorkUnit,
	:UDTPath
)

END