from itertools import izip

__author__ = 'pankaj'

import numpy as np

class Graph(object):

    def __init__(self,total_vertices):
        self.edge_list=[None]*total_vertices
        self.total_vertices = total_vertices

    def add_edge(self,v,w):
        edge = self.edge_list[v]
        if edge==None:
            edge = []
            edge.append(w)
            self.edge_list[v]=edge
        else:
            edge.append(w)


    def buildGraph(self,input_words):
        a=ord('a')
        for i in xrange(0,len(input_words)-1):
            for char1,char2 in izip(input_words[i],input_words[i+1]):
                if char1 != char2:
                    self.add_edge(ord(char1)-a,ord(char2)-a)
                    break



    def topologicalSortUtil(self,index,visited,stack):
        edge_list = self.edge_list[index]
        visited[index] = True
        if edge_list is not None:
            for i in edge_list:
                if visited[i] is False:
                    self.topologicalSortUtil(i,visited,stack)
        stack.append(index)

    def topoLogicalSort(self):
        visited = [False] * self.total_vertices
        stack =[]
        i=0
        for i in xrange(0,self.total_vertices):
            if visited[i] is False:
                self.topologicalSortUtil(i,visited,stack)


        stack.reverse()
        print stack

input_words = ("baa", "abcd", "abca", "cab", "cad")
data="".join(input_words)
dict={}
for i in data:
    hash = dict.get(i,None)
    if hash == None:
        dict.update({i:0})
    else:
        hash+=1

print input_words
g =  Graph(len(dict.keys()))
g.buildGraph(input_words)
g.topoLogicalSort()
