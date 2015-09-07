#!/usr/bin/env python3

import multiprocessing
import os
import sys
import time

import taskrun

def func():
  pass

num = 3000
cpus = os.cpu_count()
assert cpus > 0
rm = taskrun.ResourceManager(taskrun.Resource('cpu', 1, cpus))
tm = taskrun.TaskManager(resource_manager=rm)

start = time.clock()
for idx in range(num):
  taskrun.ProcessTask(tm, 'Task_{0:04d}'.format(idx), '')
stop = time.clock()
elapsed = stop - start
print('setup time: {0}'.format(elapsed))

start = time.clock()
tm.run_tasks()
stop = time.clock()
elapsed = stop - start
print('ProcessTasks per second = {0:.3f}'
      .format(num / elapsed))

start = time.clock()
for idx in range(num):
  taskrun.FunctionTask(tm, 'Task_{0:04d}'.format(idx), func)
stop = time.clock()
elapsed = stop - start
print('setup time: {0}'.format(elapsed))

start = time.clock()
tm.run_tasks()
stop = time.clock()
elapsed = stop - start
print('FunctionTasks per second = {0:.3f}'
      .format(num / elapsed))