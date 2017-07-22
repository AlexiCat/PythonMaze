#!/usr/bin/env python

######################################################################################################################
# File name: project1.py
# Description: A program that implements BFS to find the shortest path through a maze (if such a path exists).
# Author: Alexis Miranda
#
# Notes: For the BFS algorithm I've counted the four comparisons (if(arr[x][y]) != "*") as the basic operations.
#        I chose this because these four operations are performed on every single run through the while loop.
######################################################################################################################

import os, sys, time
from collections import deque

class Node:
	def __init__(self, symbol = "", visited = False, parent = None):
		self.symbol = symbol
		self.visited = visited
		self.parent = parent

while(True):

	#Get list of files
	dirs = os.listdir()

	#Ask user for file name
	print("Please select a file (0 to exit):")
	i = 0
	for file in dirs:
		i = i + 1
		print("(" + str(i) + ") " + file)

	choice = int(input("\nChoice: "))

	if(choice == 0):
		exit()

	i = 1
	fname = ""
	for file in dirs:
		if(i == choice):
			fname = file
		i = i+1

	if (fname == ""):
		print("Error: Invalid choice")
		exit()

	#Open/read file
	maze = open(fname)
	arr = maze.readlines()
	maze.close()
	nArr = []

	#Put file data into a list
	for i in range(len(arr)):
		arr[i] = arr[i].rstrip()
		nArr.append([])
		for j in range(len(arr[i])):
			nArr[i].append(Node(arr[i][j], False, None))


	#Find starting position
	# numNodes = 0
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			if (arr[i][j] == "s"):
				srow = i
				scol = j
			# if(arr[i][j] != "*"):
			# 	numNodes = numNodes +1


	#Create stuff for my algorithm
	que = deque([])
	#visited = []
	curr = (srow, scol)
	#visited.append((curr[0], curr[1]))
	#numNodes = numNodes - 1
	fail = False

	#UP: print(arr[curr[0] - 1][curr[1]])
	#DOWN: print(arr[curr[0] + 1][curr[1]])
	#LEFT: print(arr[curr[0]][curr[1] - 1])
	#RIGHT: print(arr[curr[0]][curr[1] + 1])

	#Timing and basic operations
	bOps = 0
	t0 = time.time()

	#BFS Algorithm
	while(True):
		#Check up
		bOps = bOps+1
		if (arr[curr[0] - 1][curr[1]] != "*"):
			#Have I visited this node?
			if(nArr[curr[0] - 1][curr[1]].visited == False):
				#Add to visited list
				#visited.append((curr[0]-1, curr[1]))
				#Mark as visited
				nArr[curr[0] - 1][curr[1]].visited = True
				#Parent it to current working position
				nArr[curr[0] - 1][curr[1]].parent = (curr[0], curr[1])
				#Is it the end node?
				if(arr[curr[0] - 1][curr[1]] == "e"):
					#Save end position
					epos = (curr[0]-1, curr[1])
					break
				#Add to queue
				que.append((curr[0]-1, curr[1]))

		#Check down
		bOps = bOps+1
		if (arr[curr[0] + 1][curr[1]] != "*"):
			#Have I visited this node?
			if(nArr[curr[0] + 1][curr[1]].visited == False):
				#Add to visited list
				#visited.append((curr[0]+1, curr[1]))
				#Mark as visited
				nArr[curr[0] + 1][curr[1]].visited = True
				#Parent it to current working position
				nArr[curr[0] + 1][curr[1]].parent = (curr[0], curr[1])
				#Is it the end node?
				if(arr[curr[0] + 1][curr[1]] == "e"):
					#Save end position
					epos = (curr[0]+1, curr[1])
					break
				#Add to queue
				que.append((curr[0]+1, curr[1]))

		#Check left
		bOps = bOps+1
		if (arr[curr[0]][curr[1] - 1] != "*"):
			#Have I visited this node?
			if(nArr[curr[0]][curr[1] - 1].visited == False):
				#Add to visited list
				#visited.append((curr[0], curr[1]-1))
				#Mark as visited
				nArr[curr[0]][curr[1] - 1].visited = True
				#Parent it to current working position
				nArr[curr[0]][curr[1] - 1].parent = (curr[0], curr[1])
				#Is it the end node?
				if(arr[curr[0]][curr[1] - 1] == "e"):
					#Save end position
					epos = (curr[0], curr[1]-1)
					break
				#Add to queue
				que.append((curr[0], curr[1]-1))

		#Check right
		bOps = bOps+1
		if (arr[curr[0]][curr[1] + 1] != "*"):
			#Have I visited this node?
			if(nArr[curr[0]][curr[1] + 1].visited == False):
				#Add to visited list
				#visited.append((curr[0], curr[1]+1))
				#Mark as visited
				nArr[curr[0]][curr[1] + 1].visited = True
				#Parent it to current working position
				nArr[curr[0]][curr[1] + 1].parent = (curr[0], curr[1])
				#Is it the end node?
				if(arr[curr[0]][curr[1] + 1] == "e"):
					#Save end position
					epos = (curr[0], curr[1]+1)
					break
				#Add to queue
				que.append((curr[0], curr[1]+1))

		#If queue is empty and I haven't terminated the loop then no solution exists
		try:
			curr = que.popleft()
		except IndexError:
			print("\nThis maze has no exit")
			fail = True
			break

	t1 = time.time()

	total = t1-t0

	#Print time
	print("\nFound solution in " + str((total)) + " s\n")

	#Print out path, path length, and basic operations
	if (fail == True):
		print("rip\n")
	else:
		print("Path:")
		#Python's immutable strings...
		arr2 = []
		for i in range(len(arr)):
			arr2.append([])
			arr2[i] = list(arr[i])

		#Trace back the path that we found
		pos = epos
		length = 0
		while (True):
			pos = nArr[pos[0]][pos[1]].parent
			if (arr[pos[0]][pos[1]] == "s"):
				length = length+1
				break
			else:
				length = length + 1
				arr2[pos[0]][pos[1]] = "#"

		#Print out the maze
		for i in range(len(arr)):
			for j in range(len(arr[i])):
				print(arr2[i][j], end="")
			print()

		print("I made it :)")
		print("\nPath length: " + str(length) + " moves")
		print("Basic Operations: " + str(bOps) + "\n")