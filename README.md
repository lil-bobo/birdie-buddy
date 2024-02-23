# Birdie Buddy

This project is the core subject for my TIPE exam (2023/2024)

# Description

Golf is the most spread individual game in the United States. Precision, focus and technicity are key elements which make the game hard to learn. Hence, I decided I would create a program / assistant whose aim is to help new players understand and see shots with high winning potential in order to train them to become champions. To what extent can we help new golf players improve more efficiently ?

# Approach

In order to solve this issue, I will exploit different path finding algorithms in graphs. The golf course is represented with a 2 dimensionnal grid (for now) on which the following algorithms are implemented : Breadth-First-Search and A\* (A Star). The motion of the golf ball is a singular free fall : this model helped me focus on the programming of the algorithms.

# Polygons and Meshes

In order to make the simulation more realistic, many digital tools exist to represent hilly areas. A Mesh appears to be the most adequate solution.

# Search Tracking

Currently, I am learning about the concept around meshes. I am looking forward into using the free 3D modeling software Blender which provides a list of export file formats. A file format that interests me is Wavefront Objects.

The file format Wavefront OBJ is the most efficient since it is capable of holding data about polygons and their texture. OBJ files are ASCII hence easier to understand / imagine. What's left to do is the modeling of a golf course. This part must be kept elementary since we focus on the programming part rather that the modeling part : this means a plane surface (we will accept a few curbatures) is our limit. In fact, the core part is about the physics and mathematics behind the motion of the golf ball.

# TODO

[] Model a minimal golf course (i.e. not complex) in Blender and export it to obj format.

[] Import datas from the obj file to a c (or c++) program

[] Translate Python code to c (or c++) code

[] Start thinking about a graphical interface with OpenGL (in order to see what the decisions taken by the computer look like)
