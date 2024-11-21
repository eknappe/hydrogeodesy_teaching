#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:10:41 2020

@author: knappe
"""



### Harmonic function
# y(t) = y_0 +vt_i + SUM(from k=1) a_k*sin(w_k * t_i) + b_k*cos(w_k*t_i)
# G*m = d style

from __future__ import division
import numpy as np

# Ingest 1 component of the timse seris, omega, time in ordinal 
def harm_fit(tseries, omega, dtime, semi):
    #Observations
    dv = np.array(tseries)
    if (semi == False): #just the annual
        #G matrix
        #Start with an empty matrix
        Gv = np.zeros((len(dv), 4))
        #Make the columns to be filled
        c1v = np.ones((len(dv)))
        c2v = np.array(dtime)
        c3v = np.sin(c2v*omega)
        c4v = np.cos(c2v*omega)
        #Fill the G matrix
        Gv[:,0] = c1v
        Gv[:,1] = c2v
        Gv[:,2] = c3v
        Gv[:,3] = c4v
        #Solve using Least Squares
        mv = np.linalg.solve(np.dot(np.transpose(Gv), Gv),np.dot(np.transpose(Gv),dv))
        # Full harmonic :
        y_v = mv[0] + mv[1]*dtime + mv[2]*np.sin(omega*dtime) + mv[3]*np.cos(omega*dtime)
    else: #annual + semi annual
        omega2 = 2*omega
        #G matrix
        #Start with an empty matrix
        G2 = np.zeros((len(dv), 6))
        #Make the columns to be filled
        c1 = np.ones((len(dv)))
        c2 = np.array(dtime)
        c3 = np.sin(c2*omega)
        c4 = np.cos(c2*omega)
        c5 = np.sin(c2*omega2)
        c6 = np.cos(c2*omega2)
        #Fill the G matrix
        G2[:,0] = c1
        G2[:,1] = c2
        G2[:,2] = c3
        G2[:,3] = c4
        G2[:,4] = c5
        G2[:,5] = c6
        #Solve using Least Squares
        m2 = np.linalg.solve(np.dot(np.transpose(G2), G2),np.dot(np.transpose(G2),dv))
        # Full harmonic :
        y_v = m2[0] + m2[1]*dtime + m2[2]*np.sin(omega*dtime) + m2[3]*np.cos(omega*dtime) + m2[4]*np.sin(omega2*dtime) +m2[5]*np.cos(omega2*dtime)
    return y_v



