import time
from vec import Vec

def measure_op(name:str,func):
    start  = time.perf_counter()
    func()
    end = time.perf_counter()
    return end-start

if  __name__ == "__main__":

    dimensions = [1_000,100_000,1_000_00000]


    print(f"{'Dimension (N)':<15} | {'Allocation (zeros)':<20} | {'Addition (v1 + v2)':<20} | {'In-Place (v1 *= 2)':<20}")
    print("-" * 80)

    for N in dimensions:
        v1=Vec(range(N))
        v2=Vec(range(N))

        t_alloc = measure_op("Allocation", lambda: Vec([0]*N))
        t_add = measure_op("Addition", lambda: v1 + v2)
        t_inplace = measure_op("In-Place", lambda: v1.__imul__(2.0))


        print(f"{N:<15} | {t_alloc:<20.6f} | {t_add:<20.6f} | {t_inplace:<20.6f}")


