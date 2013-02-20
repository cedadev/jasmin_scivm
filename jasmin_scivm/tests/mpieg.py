#
# Simple scatter-gather example using mpi4py
#
# $ mpirun -np 4 python ./mpieg.py
#
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = [(i+1)**2 for i in xrange(size)]
else:
   data = None

print '# Initial State for processor %s is data=%s'%(rank, data)

data = comm.scatter(data, root=0)
print '# After scattering processor %s has data %s'%(rank, data)

print '# Now something is done on processor %s'%rank
data += 100

data = comm.gather(data, root=0)
print '# After gathering processor %s has %s'%(rank, data)

#
# Typical output follows. Note things do not appear in order, and may not
# appear in the same order on repeated runs.
#
# mpirun -np 4 python ./mpieg.py
# Initial State for processor 0 is data=[1, 4, 9, 16]
# Initial State for processor 1 is data=None
# After scattering processor 1 has data 4
# Now something is done on processor 1
# After gathering processor 1 has None
# After scattering processor 0 has data 1
# Now something is done on processor 0
# Initial State for processor 3 is data=None
# Initial State for processor 2 is data=None
# After scattering processor 2 has data 9
# Now something is done on processor 2
# After gathering processor 2 has None
# After scattering processor 3 has data 16
# Now something is done on processor 3
# After gathering processor 3 has None
# After gathering processor 0 has [101, 104, 109, 116]


