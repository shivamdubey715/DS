from mpi4py import MPI 
import numpy as np 

comm = MPI.COMM_WORLD 
rank = comm.rank 

# Get the total number of processors
num_procs = comm.Get_size()

send_buf = np.array([])  # Initialize an empty numpy array

if rank == 0: 
    N = 100  # Total number of elements
    num_chunks = num_procs  # Number of chunks (equal to number of processors)
    arr = np.arange(N)  # Generate an array of N elements
    chunk_size = N // num_chunks  # Calculate the chunk size
    send_buf = np.array_split(arr, num_chunks)  # Split the array into chunks
    
recv_buf = np.empty(1, dtype=int)  # Create an empty array to receive data

send_buf = comm.scatter(send_buf, root=0)  # Scatter the chunks to all processes
local_sum = np.sum(send_buf)  # Calculate the local sum

print("Local sum at rank {0}: {1}".format(rank, local_sum))  # Print the local sum

recv_buf = comm.reduce(local_sum, op=MPI.SUM, root=0)  # Reduce local sums to obtain global sum

if rank == 0: 
    global_sum = recv_buf  # Global sum is received by the root process
    print("Global sum: " + str(global_sum))  # Print the global sum
