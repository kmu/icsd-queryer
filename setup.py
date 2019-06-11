from setuptools import setup

setup(
    install_requires=["PyYAML","beautifulsoup4", "selenium", "PyVirtualDisplay", "pandas"],
    entry_points={
        "console_scripts": [
            "icsd = app:main"
        ]
    }
)