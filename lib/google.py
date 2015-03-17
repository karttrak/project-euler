import structures
import Point

def get_adj(grid, cur, checked):

	adj_list = []

	# Checks down
	if cur.x < len(grid[0])-1:

		down = Point.Point(cur.x+1, cur.y)

		if down not in checked:
		
			adj_list.append(down)

	# Checks right
	if cur.y < len(grid)-1:

		right = Point.Point(cur.x, cur.y+1)

		if right not in checked:

			adj_list.append(right)

	# Checks left
	# if cur.x > 0:

	# 	left = Point.Point(cur.x-1, cur.y)

	# 	if left not in checked:

	# 		adj_list.append(left)

	# if grid[cur.x][cur.y+1] == '0':

	# 	adj_list.append(cur)

	return adj_list


def bfs(grid, start, target):

	# print(start)
	# print(target)

	q = structures.Queue()
	checked = structures.Set()
	checked.add(start)
	q.push(start)

	while q:

		cur = q.pop()

		q.push_list(get_adj(grid, cur, checked))

		for pnt in q:

			checked.add(pnt)

		print(q)

		print(cur)
		grid[cur.y][cur.x] = 'X'

		for line in grid:

			for cell in line:

				print(cell, end=' ')

			print()

	return grid


if __name__ == '__main__':

	grid = [
			['S','0','0', '0'],
			['0','0','0', '0'],
			['0','0','0', '0'],
			['0','0','0', '0'],
			['0','0', '0','F']
			]

	s = Point.Point()
	f = Point.Point(len(grid)-1, len(grid[0])-1)

	bfs(grid, s, f)