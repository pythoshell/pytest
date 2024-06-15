import sys
import os
library_path = r'C:\pyauto\pytest\Library'

def import_module_paths(library_path, ):
    # Add the path to the directory containing your library
    if library_path not in sys.path:
        sys.path.append(library_path)


# Direct call this files
if __name__ == "__main__":
    import_module_paths(library_path)
