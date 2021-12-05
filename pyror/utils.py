def parse_ids(d):
	vars = ['id', 'name', 'links']
	z = { v: d[v] for v in vars }
	z['grid_id'] = d['external_ids']['GRID']['preferred']
	z['link'] = None
	if len(z['links']):
		z['link'] = z['links'][0]
	z.pop('links')
	return z
