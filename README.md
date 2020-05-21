# DepthOfTree-Recursive
This is a recursive approach to find the depth/height of a tree given the input is of the parent nodes. 
Example input :

5

4 -1 4 1 1


This represents a tree with 5 nodes where:
parent of node 0 is 4
parent of node 1 is -1 (so this is the root node)
parent of node 2 is 4
parent of node 3 is 1
parent of node 4 is 1

This will produce a tree of height 3. 
There are faster approaches to this but I did it this way to understand python OOP.
The depth is calculated by first finding the root node (in this case, 1 with it's parent being -1) setting it's depth to 1,
then recursively finding the depth of it's children by adding 1 to the depth of the parent.
