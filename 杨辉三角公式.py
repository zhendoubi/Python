#!/usr/bin/env python
# -*- coding: utf-8 -*-
def triangles() -> object:
 	 L = [1]
 	 while True:
 	 	 yield L
 	 	 L = [1] + [[i] + [i + 1] for i in range(n - 1) + [1]

n = 0
for t in triangles():
	print(t)
	n = n + 1
	if n == 10:
		break
		