# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

def p_value(x,p):
    return np.power((1-np.power(x,p)),1/p)

def p3_value(X,Y,p):
    z0 = 1-np.power(X,p)-np.power(Y,p)
    z0[z0<0] = 0
    z1 = np.where(z0 > 0, np.power(z0,1/p), 0)
    return z1


class Paint_F(object):
    def __init__(self,dimention):
        self.dimention = dimention
    
    
    def paint(self):
        p = self.dimention
        if p==2:
            self.norm_2d()
        else:
            self.norm_3d()
    def norm_2d(self):
        plt.figure(figsize = (8,8))
        x_05 = np.linspace(0,1,1000)
        z = p_value(x_05,0.5)
        plt.plot(x_05,p_value(x_05,0.5),color = 'b')
        plt.plot(x_05,-p_value(x_05,0.5),color = 'b')
        plt.plot(-x_05,p_value(x_05,0.5),color = 'b')
        plt.plot(-x_05,-p_value(x_05,0.5),color = 'b')
        plt.plot(x_05,p_value(x_05,1),color = 'r')
        plt.plot(x_05,-p_value(x_05,1),color = 'r')
        plt.plot(-x_05,p_value(x_05,1),color = 'r')
        plt.plot(-x_05,-p_value(x_05,1),color = 'r')        
        plt.plot(x_05,p_value(x_05,2),color = 'c')
        plt.plot(x_05,-p_value(x_05,2),color = 'c')
        plt.plot(-x_05,p_value(x_05,2),color = 'c')
        plt.plot(-x_05,-p_value(x_05,2),color = 'c')
        plt.plot(x_05,p_value(x_05,1000000),color = 'b') # to simulate infinity
        plt.plot(x_05,-p_value(x_05,1000000),color = 'b')
        plt.plot(-x_05,p_value(x_05,1000000),color = 'b')
        plt.plot(-x_05,-p_value(x_05,1000000),color = 'b')        
        plt.ylim(-2, 2)
        plt.xlim(-2, 2)
        plt.grid(True)
        plt.show()
        
    def self_plot_k(self,p):
        fig = plt.figure(figsize = (8,8)) 
#        plt.subplot(2,2,1)
        ax = Axes3D(fig)
        x_3 = np.linspace(0,1,100)
        y_3 = np.linspace(0,1,100)
        X_3, Y_3 = np.meshgrid(x_3, y_3)
        
        #Z_3 = p3_value(X_3,Y_3,1)
        z2 = p3_value(X_3,Y_3,p)
        ax.plot_surface(X_3, Y_3, z2, rstride=1, cstride=1, cmap='bone')
        ax.plot_surface(X_3, Y_3, -z2 , rstride=1, cstride=1, cmap='bone')
        ax.plot_surface(X_3, -Y_3, z2 , rstride=1, cstride=1, cmap='bone')
        ax.plot_surface(X_3, -Y_3, -z2 , rstride=1, cstride=1, cmap='bone')
        ax.plot_surface(-X_3, Y_3, z2 , rstride=1, cstride=1, cmap='bone')
        ax.plot_surface(-X_3, Y_3, -z2 , rstride=1, cstride=1, cmap='bone')
        ax.plot_surface(-X_3, -Y_3, z2 , rstride=1, cstride=1, cmap='bone')
        ax.plot_surface(-X_3, -Y_3, -z2 , rstride=1, cstride=1, cmap='bone')
        ax.title.set_text(("Norm "+str(p)))
    
    
    def norm_3d(self):
        self.self_plot_k(2)
        self.self_plot_k(1)
        self.self_plot_k(0.5)
        self.self_plot_k(1000000)
#        plt.subplot(2,2,2)
#        z1 = p3_value(X_3,Y_3,1)
#        ax.plot_surface(X_3, Y_3, z1, rstride=1, cstride=1, cmap='bone')
#        ax.plot_surface(X_3, Y_3, -z1 , rstride=1, cstride=1, cmap='bone')
#        ax.plot_surface(X_3, -Y_3, z1 , rstride=1, cstride=1, cmap='bone')
#        ax.plot_surface(X_3, -Y_3, -z1 , rstride=1, cstride=1, cmap='bone')
#        ax.plot_surface(-X_3, Y_3, z1 , rstride=1, cstride=1, cmap='bone')
#        ax.plot_surface(-X_3, Y_3, -z1 , rstride=1, cstride=1, cmap='bone')
#        ax.plot_surface(-X_3, -Y_3, z1 , rstride=1, cstride=1, cmap='bone')
#        ax.plot_surface(-X_3, -Y_3, -z1 , rstride=1, cstride=1, cmap='bone')
#        plt.plot(x,p_value(x_05_1,0.5),color = 'b')
#        plt.plot(x_05,-p_value(x_05_1,0.5),color = 'b')
#        plt.plot(-x_05,p_value(x_05_1,0.5),color = 'b')
#        plt.plot(-x_05,-p_value(x_05_1,0.5),color = 'b')
#        plt.plot(x_05,p_value(x_05_1,1),color = 'r')
#        plt.plot(x_05,-p_value(x_05_1,1),color = 'r')
#        plt.plot(-x_05,p_value(x_05_1,1),color = 'r')
#        plt.plot(-x_05,-p_value(x_05_1,1),color = 'r')        
#        plt.plot(x_05,p_value(x_05_1,2),color = 'c')
#        plt.plot(x_05,-p_value(x_05_1,2),color = 'c')
#        plt.plot(-x_05,p_value(x_05_1,2),color = 'c')
#        plt.plot(-x_05,-p_value(x_05_1,2),color = 'c')
#        plt.plot(x_05,p_value(x_05_1,10000),color = 'b') # to simulate infinity
#        plt.plot(x_05,-p_value(x_05_1,10000),color = 'b')
#        plt.plot(-x_05,p_value(x_05_1,10000),color = 'b')
#        plt.plot(-x_05,-p_value(x_05_1,10000),color = 'b')        
        plt.show()        
        
        
    #handles, labels = ax.get_legend_handles_labels(
def main():
    Paint = Paint_F(2)
    Paint.paint()


if __name__ == "__main__":
    main()
