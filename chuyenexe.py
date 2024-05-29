from cx_Freeze import setup, Executable
import os
import site

# Get the path to site-packages in the virtual environment
site_packages_path = site.getsitepackages()[0]

# Create a list of packages to include
packages = ["transformers", "streamlit", "PIL", "numpy"]

# Define include files list
include_files = [
    (os.path.join(site_packages_path, "transformers"), "lib/transformers"),
    (os.path.join(site_packages_path, "streamlit"), "lib/streamlit"),
    (os.path.join(site_packages_path, "PIL"), "lib/PIL"),
    (os.path.join(site_packages_path, "numpy"), "lib/numpy"),
]

build_exe_options = {
    "packages": packages,
    "include_files": include_files,
}

setup(
    name="test_build",
    version="1.0",
    description="tenmota",
    options={"build_exe": build_exe_options},
    executables=[Executable("ocr_app.py")]
)
