#!/usr/bin/env python3
import os
import gc
import ctypes
import ctypes.util

print("🔬 RTOS Configuration Test")
print("=" * 40)

# Test Memory Locking
try:
    libc = ctypes.CDLL(ctypes.util.find_library('c'))
    MCL_CURRENT = 1
    MCL_FUTURE = 2
    result = libc.mlockall(MCL_CURRENT | MCL_FUTURE)
    memory_locked = (result == 0)
    print(f"Memory Locking (mlockall): {'🟢 LOCKED' if memory_locked else '🔴 UNLOCKED'}")
except Exception as e:
    print(f"Memory Locking (mlockall): 🔴 FAILED ({e})")

# Test RT Priority
try:
    SCHED_FIFO = 1
    param = os.sched_param(99)
    os.sched_setscheduler(0, SCHED_FIFO, param)
    print("Real-Time Priority (99): 🟢 ACTIVE (SCHED_FIFO)")
except PermissionError:
    try:
        os.nice(-20)
        print("Real-Time Priority (99): 🟡 HIGH PRIORITY (nice -20)")
    except:
        print("Real-Time Priority (99): 🔴 INACTIVE (no permissions)")
except Exception as e:
    print(f"Real-Time Priority (99): 🔴 FAILED ({e})")

# Test CPU Affinity
try:
    os.sched_setaffinity(0, {3})
    current_affinity = os.sched_getaffinity(0)
    print(f"CPU Affinity: 🟢 CORE 3 ISOLATED (current: {current_affinity})")
except Exception as e:
    print(f"CPU Affinity: 🔴 FAILED ({e})")

# Test GC Control
try:
    gc.disable()
    print("Garbage Collection: 🟢 DISABLED")
except Exception as e:
    print(f"Garbage Collection: 🔴 FAILED ({e})")

print("\n✅ RTOS Configuration Test Complete")