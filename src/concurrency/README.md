# concurrency in Python
Concurrency means multiple computations are happening at the same time.

## Multithreading
Great for I/O bound operations where the CPU is waiting for input/output operations to be completed.

Not so great for CPU bound operations - computational heavy stuff then threads wouldn't be ideal for that type of task.