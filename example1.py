import serf

_client = serf.Client()

def _callback (response, ) :
	_members = response.body.get('Members', )
	for member in _members:
		print "%s : %s" % (member.get('Status'), '.'.join(str(x) for x in member.get('Addr')))

_client.join(Existing=('172.20.20.10',), Replay=False).request()
_client.members().add_callback(_callback, ).request()
