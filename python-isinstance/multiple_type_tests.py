print("Number" if isinstance(3.14, (int, float)) else "Not a number")
print("Number" if isinstance("3.14", (int, float)) else "Not a number")
print("Number" if isinstance(3.14, ((int,), (float,))) else "Not a number")
print("Number" if isinstance(3.14, (int, float)) else "Not a number")
print("Number" if isinstance(3.14, int | float) else "Not a number")
print("Number" if isinstance("3.14", int | float) else "Not a number")
