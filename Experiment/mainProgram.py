# -*- coding: utf-8 -*-

import singleClass, time

exp = singleClass.experimentClass()

exp.getTimes()
exp.getFileName()
exp.getReps()

exp.connect()
exp.prepareForExperiment()
time.sleep(1)
exp.createFile()
exp.writeHeader()
exp.startExperiment()
exp.writeFooter()
exp.resetArduino()