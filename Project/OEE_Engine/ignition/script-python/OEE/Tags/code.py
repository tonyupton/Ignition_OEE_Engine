def downloadUDTDefinitions():
	url = "https://raw.githubusercontent.com/tonyupton/Ignition_OEE_Engine/main/Tags/UDT_Definitions.json"
	return system.net.httpGet(url)

def getUDTPyObject():
	return system.util.jsonDecode(downloadUDTDefinitions())

def getUDTDefinitionBasePath(tagProvider):
	path = "[%s]_types_" % (tagProvider)
	return path

def createUDT():
	system.tag.configure(getUDTDefinitionBasePath("Test"), getUDTPyObject(), "o")