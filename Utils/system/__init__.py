import platform

UNAME_INFO = platform.uname()
print(f"System: {UNAME_INFO.system}")
print(f"Node: {UNAME_INFO.node}")
print(f"Release: {UNAME_INFO.release}")
print(f"Version: {UNAME_INFO.version}")
print(f"Machine: {UNAME_INFO.machine}")
print(f"Processor: {UNAME_INFO.processor}")

