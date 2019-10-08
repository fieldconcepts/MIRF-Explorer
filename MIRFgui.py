from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np

from MIRFheaders import *

class  PlotWidget(pg.GraphicsWindow):
    def __init__(self, parent=None, **kargs):
  
        #create the graphing widget
        pg.GraphicsWindow.__init__(self, **kargs)
        
        # make pretty
        pg.setConfigOptions(antialias=True)
        
        #embed widget inside the main window
        self.setParent(parent)

    
    #Standard View plotting every trace
    def standardView(self, trace_obj, sample_interval, picks):
        
        # pull in variables from function call
        self.trace_obj = trace_obj
        self.sample_interval = sample_interval
        self.picks = picks

        # create an empty array to store the list of pyqtgraph plot objects
        self.plot_frames = []

        # style the plots
        for i in range(len(self.trace_obj)):

            plot = self.addPlot(row=i, col=0)
            self.plot_frames.append(plot)

            self.plot_frames[i].clear() # clear previous plot
            
            # Zero line
            zero_line = pg.InfiniteLine(movable=False, angle=0, pen=pg.mkColor(0.2)) #add infinte line at zero
            self.plot_frames[i].addItem(zero_line)

            #Time Picks
            if self.picks == True:
                
                vert_line = pg.InfiniteLine(movable=True, angle=90, pen=pg.mkColor(0.2)) #add infinte line at zero
                self.plot_frames[i].addItem(vert_line)
                vert_label = pg.InfLineLabel(vert_line, text="{value:0.2f}ms", position=0.9)

            # convert dataset to numpy array and create the calc x-axis value dependant on SI
            y = np.array(self.trace_obj[i].Raw_data)
            x = np.arange(0, len(y)*(self.sample_interval/1000), self.sample_interval/1000)

            #plot dataset
            self.plot_frames[i].plot(x, y, pen=pg.mkColor(0.7))
            self.plot_frames[i].enableAutoRange(pg.ViewBox.XYAxes)
            self.plot_frames[i].setMouseEnabled(x=True, y=False) #lock vertical scroll
            self.plot_frames[i].hideButtons() # hide auto scale A button
            
            #hide axis btoom and left
            self.plot_frames[i].hideAxis('bottom')
            self.plot_frames[i].hideAxis('left')

            #link all scrolling axis together
            if i > 0:
                self.plot_frames[i].setXLink(self.plot_frames[i-1])
            
            #left axis stuff decriptors
            owner = owner_translate(self.trace_obj[i].Owner)

            self.plot_frames[i].showAxis('left')
            self.plot_frames[i].getAxis('left').enableAutoSIPrefix(enable=False)
            self.plot_frames[i].getAxis('left').setLabel(text=owner, units=None)
            self.plot_frames[i].getAxis('left').setStyle(tickLength=0, showValues=False)

            #right axis stuff decriptors
            desc = description_translate(self.trace_obj[i].Descriptor)
            self.plot_frames[i].showAxis('right')
            self.plot_frames[i].getAxis('right').enableAutoSIPrefix(enable=False)
            self.plot_frames[i].getAxis('right').setLabel(text=desc, units=None)
            self.plot_frames[i].getAxis('right').setStyle(tickLength=0, showValues=False)


        # check to allow for an empty plots scenario.
        if len(self.plot_frames) != 0:
            #show axis and label on top plot
            self.plot_frames[0].showAxis('top')
            self.plot_frames[0].getAxis('top').setStyle(showValues=True)

            #show axis on bottom plot
            self.plot_frames[-1].showAxis('bottom')
            self.plot_frames[-1].getAxis('bottom').setStyle(showValues=True)


    # Overlay view plotting all surface channels followed by 3 XYZ compnents overlayed
    def overlayView(self, trace_obj, sample_interval, picks):
        
        # pull in variables from function call
        self.trace_obj = trace_obj
        self.sample_interval = sample_interval
        self.picks = picks
        
        # create an empty array to store the list of pyqtgraph plot objects
        self.plot_frames = []

        n_aux_plots = 0
        n_geo_plots = 0

        #work out how many AUX and GEO there are
        for i in range(len(self.trace_obj)):
            if self.trace_obj[i].Owner < 0:
                n_aux_plots += 1
            elif self.trace_obj[i].Owner > 0:
                n_geo_plots += 1
        
        n_geo_plots = int(n_geo_plots/3)
        
        #add single aux plots
        for i in range(n_aux_plots):
            plot = self.addPlot(row=i, col=0)
            self.plot_frames.append(plot)

            self.plot_frames[i].clear()

            y = np.array(self.trace_obj[i].Raw_data)
            x = np.arange(0, len(y)*(self.sample_interval/1000), self.sample_interval/1000)
            self.plot_frames[i].plot(x, y)

            #left axis stuff decriptors
            owner = owner_translate(self.trace_obj[i].Owner)

            self.plot_frames[i].showAxis('left')
            self.plot_frames[i].getAxis('left').enableAutoSIPrefix(enable=False)
            self.plot_frames[i].getAxis('left').setLabel(text=owner, units=None)
            self.plot_frames[i].getAxis('left').setStyle(tickLength=0, showValues=False)

            #right axis stuff decriptors
            desc = description_translate(self.trace_obj[i].Descriptor)
            self.plot_frames[i].showAxis('right')
            self.plot_frames[i].getAxis('right').enableAutoSIPrefix(enable=False)
            self.plot_frames[i].getAxis('right').setLabel(text=desc, units=None)
            self.plot_frames[i].getAxis('right').setStyle(tickLength=0, showValues=False)

        #add geo overlay plots
        for i in range(n_geo_plots):

            plot = self.addPlot(row=i + n_aux_plots, col=0)
            self.plot_frames.append(plot)
            
            self.plot_frames[i + n_aux_plots].clear()
        
            y1 = np.array(self.trace_obj[(i*3) + 0 + n_aux_plots].Raw_data)
            y2 = np.array(self.trace_obj[(i*3) + 1 + n_aux_plots].Raw_data)
            y3 = np.array(self.trace_obj[(i*3) + 2 + n_aux_plots].Raw_data)
            x = np.arange(0, len(y1)*(self.sample_interval/1000), self.sample_interval/1000)

            self.plot_frames[i + n_aux_plots].plot(x, y1, pen=(255,0,0))
            self.plot_frames[i + n_aux_plots].plot(x, y2, pen=(0,255,0))
            self.plot_frames[i + n_aux_plots].plot(x, y3, pen=(0,0,255))

            #left axis stuff decriptors
            owner = owner_translate(self.trace_obj[(i*3) + n_aux_plots].Owner)

            self.plot_frames[i + n_aux_plots].showAxis('left')
            self.plot_frames[i + n_aux_plots].getAxis('left').enableAutoSIPrefix(enable=False)
            self.plot_frames[i + n_aux_plots].getAxis('left').setLabel(text=owner, units=None)
            self.plot_frames[i + n_aux_plots].getAxis('left').setStyle(tickLength=0, showValues=False)

            #right axis stuff decriptors
            desc = "XYZ"
            self.plot_frames[i + n_aux_plots].showAxis('right')
            self.plot_frames[i + n_aux_plots].getAxis('right').enableAutoSIPrefix(enable=False)
            self.plot_frames[i + n_aux_plots].getAxis('right').setLabel(text=desc, units=None)
            self.plot_frames[i + n_aux_plots].getAxis('right').setStyle(tickLength=0, showValues=False)
        
        
        #Formatting plots
        for i in range(len(self.plot_frames)):
            
            # Zero line
            zero_line = pg.InfiniteLine(movable=False, angle=0, pen=pg.mkColor(0.2)) #add infinte line at zero
            self.plot_frames[i].addItem(zero_line)

            #Time Picks
            if self.picks == True:
                vert_line = pg.InfiniteLine(movable=True, angle=90, pen=pg.mkColor(0.2)) #add infinte line at zero
                self.plot_frames[i].addItem(vert_line)
                vert_label = pg.InfLineLabel(vert_line, text="{value:0.2f}ms", position=0.9)
            
            self.plot_frames[i].enableAutoRange(pg.ViewBox.XYAxes)
            self.plot_frames[i].setMouseEnabled(x=True, y=False) #lock vertical scroll
            self.plot_frames[i].hideButtons() # hide auto scale A button

            #hide axis btoom and left
            self.plot_frames[i].hideAxis('bottom')


 
            #link all scrolling axis together
            if i > 0:
                self.plot_frames[i].setXLink(self.plot_frames[i-1])
            
            
        
        # check to allow for an empty plots scenario.
        if len(self.plot_frames) != 0:
            #show axis and label on top plot
            self.plot_frames[0].showAxis('top')
            self.plot_frames[0].getAxis('top').setStyle(showValues=True)

            #show axis on bottom plot
            self.plot_frames[-1].showAxis('bottom')
            self.plot_frames[-1].getAxis('bottom').setStyle(showValues=True)



