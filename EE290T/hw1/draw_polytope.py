#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:27:12 2018

@author: kewang
"""

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

class paint_poly(object):
    def __init__(self,num_points):
        self.num_points = 100
        self.fig = plt.figure()
    def paint_p(self,r):
        self.r = r
        theta = np.linspace(0,np.pi/2,self.num_points)
        phai = np.linspace(0,np.pi/2,self.num_points)
        theta,phai = np.meshgrid(theta,phai)
        #fig = plt.figure()
        #self.ax = Axes3D(self.fig)
        x = np.square(np.sqrt(r)*np.cos(theta))
        y = np.square(np.sqrt(r)*np.sin(theta)*np.sin(phai))
        z = np.square(np.sqrt(r)*np.sin(theta)*np.cos(phai))
        print(x.shape)
        for i in range(8):
            self.ax.scatter((-2*int(i/4)+1)*x,(-2*int((i%4)/2)+1)*y,(-2*(i%2)+1)*z,c='b')
        x0 = list([])
        y0 = list([])
        z0 = list([])
        print(self.plane)
        for ii in range(np.size(theta)):
            a = int(ii/100)
            b = ii%100
            if self.plane[3]>0:
                if np.sum(np.multiply(self.plane,[x[a,b],y[a,b],z[a,b],1]))<0:
                    x0.append(x[a,b])
                    y0.append(y[a,b])
                    z0.append(z[a,b])
                if np.sum(np.multiply(self.plane,[x[a,b],y[a,b],-z[a,b],1]))<0:
                    x0.append(x[a,b])
                    y0.append(y[a,b])
                    z0.append(-z[a,b])
                if np.sum(np.multiply(self.plane,[x[a,b],-y[a,b],z[a,b],1]))<0:
                    x0.append(x[a,b])
                    y0.append(-y[a,b])
                    z0.append(z[a,b])
                if np.sum(np.multiply(self.plane,[x[a,b],-y[a,b],-z[a,b],1]))<0:
                    x0.append(x[a,b])
                    y0.append(-y[a,b])
                    z0.append(-z[a,b])
                if np.sum(np.multiply(self.plane,[-x[a,b],y[a,b],z[a,b],1]))<0:
                    x0.append(-x[a,b])
                    y0.append(y[a,b])
                    z0.append(z[a,b])
                if np.sum(np.multiply(self.plane,[-x[a,b],y[a,b],-z[a,b],1]))<0:
                    x0.append(-x[a,b])
                    y0.append(y[a,b])
                    z0.append(-z[a,b])
                if np.sum(np.multiply(self.plane,[-x[a,b],-y[a,b],z[a,b],1]))<0:
                    x0.append(-x[a,b])
                    y0.append(-y[a,b])
                    z0.append(z[a,b])
                if np.sum(np.multiply(self.plane,[-x[a,b],-y[a,b],-z[a,b],1]))<0:
                    x0.append(-x[a,b])
                    y0.append(-y[a,b])
                    z0.append(-z[a,b])
            if self.plane[3]<0:
                if np.sum(np.multiply(self.plane,[x[a,b],y[a,b],z[a,b],1]))>0:
                    x0.append(x[a,b])
                    y0.append(y[a,b])
                    z0.append(z[a,b])
                if np.sum(np.multiply(self.plane,[x[a,b],y[a,b],-z[a,b],1]))>0:
                    x0.append(x[a,b])
                    y0.append(y[a,b])
                    z0.append(-z[a,b])
                if np.sum(np.multiply(self.plane,[x[a,b],-y[a,b],z[a,b],1]))>0:
                    x0.append(x[a,b])
                    y0.append(-y[a,b])
                    z0.append(z[a,b])
                if np.sum(np.multiply(self.plane,[x[a,b],-y[a,b],-z[a,b],1]))>0:
                    x0.append(x[a,b])
                    y0.append(-y[a,b])
                    z0.append(-z[a,b])
                if np.sum(np.multiply(self.plane,[-x[a,b],y[a,b],z[a,b],1]))>0:
                    x0.append(-x[a,b])
                    y0.append(y[a,b])
                    z0.append(z[a,b])
                if np.sum(np.multiply(self.plane,[-x[a,b],y[a,b],-z[a,b],1]))>0:
                    x0.append(-x[a,b])
                    y0.append(y[a,b])
                    z0.append(-z[a,b])
                if np.sum(np.multiply(self.plane,[-x[a,b],-y[a,b],z[a,b],1]))>0:
                    x0.append(-x[a,b])
                    y0.append(-y[a,b])
                    z0.append(z[a,b])
                if np.sum(np.multiply(self.plane,[-x[a,b],-y[a,b],-z[a,b],1]))>0:
                    x0.append(-x[a,b])
                    y0.append(-y[a,b])
                    z0.append(-z[a,b])                  
            if ii%1000 == 0:
                print("l")
        #print(x0)
        self.ax.scatter(x0,y0,z0,c='g')
        self.ax.set_zlabel('Z')  
        self.ax.set_ylabel('Y')
        self.ax.set_xlabel('X')
        
        #plt.show()
        
    def paint_plane(self,a,b,c,d):
        self.plane = [a,b,c,d]
        x = theta = np.linspace(-10,10,self.num_points*2)
        y = theta = np.linspace(-10,10,self.num_points*2)
        x,y = np.meshgrid(x,y)
        z = (-d-a*x-b*y)/c
        ax = Axes3D(self.fig)
        ax.scatter(x,y,z,c = 'r')
        self.ax = ax
        
        
def main():
    for r in [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]:
        print(r)
        pt = paint_poly(100)
        pt.paint_plane(1,2,3,4)# d cannot equals to 0
        pt.paint_p(r)
    
    plt.show()
        
if __name__ == "__main__":
    main()