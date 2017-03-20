# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib import cm


def contourplotAIDSByAgeGroup2(x,y,z, labels,location,city):
    plt.close()
    fig = plt.figure()
    # contour the gridded data, plotting dots at the randomly spaced data points.
    #CS = plt.contour(x,y,z.T,15,linewidths=0.5,colors='k')
    CS = plt.contourf(x,y,z.T,15,cmap=plt.cm.jet)
    cbar = plt.colorbar() # draw colorbar
    plt.xlim(1981,2003)
    plt.xticks([1981,1985,1990,1995,2000, 2003],['1981','1985','1990','1995','2000','2003'])
    plt.xlabel('Year of Diagnosis')
    plt.ylim(0,12)
    plt.yticks(location,labels, rotation='horizontal')
    plt.title('AIDS Diagnoses By Age Group: All Years in ' + str(city))
    cbar.set_label('Cases Diagnosed')
    plt.tight_layout()
    plt.savefig('/home/InsightfullyYours/webapp/assets/images/C2F4a.png')


def contourplotAIDSByAgeGroupLogNorm2(x,y,z,labels,location,city):
    plt.close()
    fig = plt.figure()
    # contour the gridded data, plotting dots at the randomly spaced data points.
    #CS = plt.contour(x,y,z.T,15,linewidths=0.5,colors='k')
    CS = plt.contourf(x,y,z.T,15,cmap=plt.cm.jet, norm=LogNorm())
    cbar = plt.colorbar() # draw colorbar
    plt.xlim(1981,2003)
    plt.xticks([1981,1985,1990,1995,2000, 2003],['1981','1985','1990','1995','2000','2003'])
    plt.xlabel('Year of Diagnosis')
    plt.ylim(0,12)
    plt.yticks(location,labels, rotation='horizontal')
    plt.title('AIDS Diagnoses By Age Group: All Years in ' + str(city))
    cbar.set_label('Cases Diagnosed')
    plt.tight_layout()
    plt.savefig('/home/InsightfullyYours/webapp/assets/images/C2F4b.png')


def contourplotHIVExpByYear2(x,y,z, labels,location, city):
    plt.close()
    fig = plt.figure()
    # contour the gridded data, plotting dots at the randomly spaced data points.
    #CS = plt.contour(x,y,z.T,15,linewidths=0.5,colors='k')
    CS = plt.contourf(x,y,z.T,15,cmap=plt.cm.jet)
    cbar = plt.colorbar() # draw colorbar
    plt.xlim(1981,2003)
    plt.xticks([1981,1985,1990,1995,2000, 2003],['1981','1985','1990','1995','2000','2003'])
    plt.xlabel('Year of Diagnosis')
    #plt.ylim(-1,13)
    plt.yticks(location,labels, rotation='horizontal',fontsize=8)
    plt.title('AIDS Diagnoses By HIV Exposure: All Years in ' + str(city))
    cbar.set_label('Cases Diagnosed')
    plt.tight_layout()
    plt.savefig('/home/InsightfullyYours/webapp/assets/images/C2F6a.png')


def contourplotHIVExpByYearLogNorm2(x,y,z,labels,location,city):
    plt.close()
    fig = plt.figure()
    # contour the gridded data, plotting dots at the randomly spaced data points.
    #CS = plt.contour(x,y,z.T,15,linewidths=0.5,colors='k')
    CS = plt.contourf(x,y,z.T,15,cmap=plt.cm.jet, norm=LogNorm())
    cbar = plt.colorbar() # draw colorbar
    plt.xlim(1981,2003)
    plt.xticks([1981,1985,1990,1995,2000, 2003],['1981','1985','1990','1995','2000','2003'])
    plt.xlabel('Year of Diagnosis')
    #plt.ylim(-1,13)
    plt.yticks(location,labels, rotation='horizontal', fontsize=8)
    plt.title('AIDS Diagnoses By HIV Exposure: All Years in ' + str(city))
    cbar.set_label('Cases Diagnosed')
    plt.tight_layout()
    plt.savefig('/home/InsightfullyYours/webapp/assets/images/C2F6b.png')


def contourplotHIVExpByAge2(x,y,z, labels,location,labelsy,location2,city):
    plt.close()
    fig = plt.figure()
    # contour the gridded data, plotting dots at the randomly spaced data points.
   # CS = plt.contour(x,y,z.T,15,linewidths=0.5,colors='k')
    CS = plt.contourf(x,y,z.T,15,cmap=plt.cm.jet)
    cbar = plt.colorbar() # draw colorbar
    plt.xlabel('Age At Diagnosis')
    plt.xticks(location2,labelsy, rotation='vertical', fontsize=6)
    plt.yticks(location,labels, rotation='horizontal',fontsize=6)
    plt.title('AIDS Diagnoses By HIV Exposure Type and Age at Diagnosis in ' + str(city))
    cbar.set_label('Cases Diagnosed')
    plt.tight_layout()
    plt.savefig('/home/InsightfullyYours/webapp/assets/images/C2F7.png')

def contourplotVital2(x,y,z, labels,location,city):
    plt.close()
    fig = plt.figure()
    # contour the gridded data, plotting dots at the randomly spaced data points.
    #CS = plt.contour(x,y,z.T,15,linewidths=0.5,colors='k')
    CS = plt.contourf(x,y,z.T,15,cmap=plt.cm.jet)
    cbar = plt.colorbar() # draw colorbar
    plt.xlim(1982,2000)
    plt.xlabel('Year of Diagnosis')
    plt.xticks([1982,1985,1990,1995,2000],['1982','1985','1990','1995','2000'])
    #plt.ylim(-1,13)
    plt.yticks(location,labels, rotation='horizontal',fontsize=8)
    plt.title('Case Mortality Percentage By Exposure and Year in ' + str(city))
    cbar.set_label('Percent Mortality by 2001, All Causes')
    plt.tight_layout()
    plt.savefig('/home/InsightfullyYours/webapp/assets/images/C2F9.png')

def contourplotVitalAge2(x,y,z, labels,location,city):
    plt.close()
    fig = plt.figure()
    # contour the gridded data, plotting dots at the randomly spaced data points.
    #CS = plt.contour(x,y,z.T,15,linewidths=0.5,colors='k')
    CS = plt.contourf(x,y,z.T,15,cmap=plt.cm.jet)
    cbar = plt.colorbar() # draw colorbar
    plt.xlim(1982,2000)
    plt.xlabel('Year of Diagnosis')
    plt.xticks([1982,1985,1990,1995,2000],['1982','1985','1990','1995','2000'])
    #plt.ylim(-1,13)
    plt.yticks(location,labels, rotation='horizontal',fontsize=8)
    plt.title('Case Mortality Percentage By Age at Diagnosis and Year in ' + str(city))
    cbar.set_label('Percent Mortality by 2001, All Causes')
    plt.tight_layout()
    plt.savefig('/home/InsightfullyYours/webapp/assets/images/C2F8.png')

