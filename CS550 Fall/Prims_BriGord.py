import png, random, heapq, argparse

class undirected_graph(dict):
	"""A dictionary of unordered pairs."""
	def __setitem__(self, key, value):
		super(undirected_graph, self).__setitem__(tuple(sorted(key)), value)

	def __getitem__(self, key):
		return super(undirected_graph, self).__getitem__(tuple(sorted(key)))

	def __has_key__(self, key):
		return super(undirected_graph, self).__has_key__(tuple(sorted(key)))

def grid_adjacent(vertex):
	"""Return all grid vertices adjacent to the given point."""
	x, y = vertex
	adj = []

	if x > 0:
		adj.append((x-1, y))
	if x < GRID_WIDTH-1:
		adj.append((x+1, y))
	if y > 0:
		adj.append((x, y-1))
	if y < GRID_HEIGHT-1:
		adj.append((x, y+1))

	return adj

def make_grid():
	weights = undirected_graph()
	for x in xrange(GRID_WIDTH):
		for y in xrange(GRID_HEIGHT):
			vertex = (x,y)
			for neighbor in grid_adjacent(vertex):
				weights[(vertex,neighbor)] = random.random()

	return weights

def MCST():
	spanning = undirected_graph()
	weights = make_grid()

	closed = set([(0,0)])
	heap = []
	for neighbor in grid_adjacent((0,0)):
		cost = weights[(0,0),neighbor]
		heapq.heappush(heap, (cost, (0,0), neighbor))

	while heap:
		cost, v1, v2 = heapq.heappop(heap)

		# v1 is the vertex already in the spanning tree
		# it's possible that we've already added v2 to the spanning tree
		if v2 in closed:
			continue

		# add v2 to the closed set
		closed.add(v2)

		# add v2's neighbors to the heap
		for neighbor in grid_adjacent(v2):
			if neighbor not in closed:
				cost = weights[v2, neighbor]
				heapq.heappush(heap, (cost, v2, neighbor))

		# update the spanning tree
		spanning[(v1,v2)] = True

	return draw_tree(spanning)

def RDM():
	spanning = undirected_graph()

	closed = set([(0,0)])
	neighbors = [((0,0), x) for x in grid_adjacent((0,0))]

	while neighbors:
		v1, v2 = neighbors.pop(random.randrange(len(neighbors)))

		# v1 is the vertex already in the spanning tree
		# it's possible that we've already added v2 to the spanning tree
		if v2 in closed:
			continue

		# add v2 to the closed set
		closed.add(v2)

		for neighbor in grid_adjacent(v2):
			if neighbor not in closed:
				neighbors.append((v2, neighbor))

		# update the spanning tree
		spanning[(v1,v2)] = True

	return draw_tree(spanning)

def draw_tree(spanning):
	# Create a big array of 0s and 1s for pypng

	pixels = []

	# Add a row of off pixels for the top
	pixels.append([0] + [1] + ([0] * (img_width-2)))

	for y in xrange(GRID_HEIGHT):
		# Row containing nodes
		row = [0] # First column is off
		for x in xrange(GRID_WIDTH):
			row.append(1)
			if x < GRID_WIDTH-1:
				row.append( int(((x,y),(x+1,y)) in spanning) )
		row.append(0) # Last column is off
		pixels.append(row)

		if y < GRID_HEIGHT-1:
			# Row containing vertical connections between nodes
			row = [0] # First column is off
			for x in xrange(GRID_WIDTH):
				row.append( int(((x,y),(x,y+1)) in spanning) )
				row.append(0)
			row.append(0) # Last column is off
			pixels.append(row)

	# Add a row of off pixels for the bottom
	pixels.append(([0] * (img_width-2)) + [1] + [0])

	return pixels

# Handle arguments

parser = argparse.ArgumentParser(description='Generate a maze with one of two algorithms.')

group = parser.add_mutually_exclusive_group()
group.add_argument('--prims', action='store_true', help='Use Prim\'s algorithm')
group.add_argument('--random', action='store_true', help='Produce a random spanning tree')

parser.add_argument('-s', dest='size', required=True, type=int, nargs=2, action='store', metavar='size', help='The maze\'s size, width then height in cells')
parser.add_argument('-o', dest='filename', metavar='filename', nargs=1, default='maze.png')

args = parser.parse_args()

GRID_WIDTH, GRID_HEIGHT = tuple(args.size)

img_width = GRID_WIDTH * 2 + 1
img_height = GRID_HEIGHT * 2 + 1

if args.random:
	pix = RDM()
else:
	pix = MCST()

f = open(args.filename, 'wb')
w = png.Writer(img_width, img_height, greyscale=True, bitdepth=1)
w.write(f, pix)
f.close()