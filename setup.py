from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="acs-laptop-debug-analyzer",
    version="2.0.0",
    author="Manoj Kumar Badapanda",
    author_email="support@a1computersolutions.in",
    description="Professional Laptop Motherboard Debug Analyzer Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR-USERNAME/ACS-Laptop-Debug-Analyzer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Debuggers",
        "Topic :: System :: Hardware",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyQt5>=5.15.4",
        "pyqtgraph>=0.12.4",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "pyserial>=3.5",
        "pyusb>=1.2.1",
    ],
    entry_points={
        "console_scripts": [
            "laptop-debug-analyzer=logic_analyzer:main",
        ],
    },
    include_package_data=True,
    keywords="laptop debug analyzer motherboard logic-analyzer diagnostic repair",
)