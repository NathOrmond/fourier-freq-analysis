# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import csv
import sys


#------------------- Main Class
class Main:
     
    def __init__(self):
         print("Main Class init")
         
    def run(self):
        
        filename = sys.argv()[1]
        #filename = "mock.csv"
        
        
        # Number of samplepoints
        N = self.get_rows(filename)
        
        # sample spacing
        T = 50000 / N
        
        y = self.get_y_data(filename)
        
        x = np.linspace(0.0, N*T, N)
        y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
        
        yf = scipy.fftpack.fft(y)
        xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

        fig, ax = plt.subplots()
        ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
        plt.show()
        

    def get_y_data(self, filename):
        
        y = []
        
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                y.insert(len(y), row[1])
                line_count += 1
                
            print(y)
            return y
           
            
    def get_rows(self, filename):
        rows = 0
        with open(filename) as csv_file:
           csv_reader = csv.reader(csv_file, delimiter=',')
           for row in csv_reader:
               if(", ".join(row) != ""):
                   rows += 1
        print(f'rows: {rows}')
        return rows
            
        
#------------------ Script
Main().run()


