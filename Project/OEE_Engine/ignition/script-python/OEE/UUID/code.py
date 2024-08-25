def isValidUUID(uuid_to_test, version=4):
	#    Check if `uuid_to_test` is a valid UUID.
	#
	#    Parameters:
	#    - `uuid_to_test`: str
	#    - `version`: {1, 2, 3, 4}
	#
	#    Returns:
	#    - `True` if `uuid_to_test` is a valid UUID, otherwise `False`.
	from uuid import UUID
	if uuid_to_test is None:
		return False
	try:
		uuid_obj = UUID(uuid_to_test, version=version)
	except ValueError:
		return False
	return str(uuid_obj) == uuid_to_test

def UUID4():
	import uuid
	return str(uuid.uuid4()).upper()