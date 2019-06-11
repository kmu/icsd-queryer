from setuptools import setup

setup(
    name="icsd",
    install_requires=["PyYAML","beautifulsoup4", "selenium", "PyVirtualDisplay", "pandas"],
    entry_points={
        "console_scripts": [
            "icsd = app:main"
        ]
    },
    maintainer="Koki Muraoka",
    maintainer_email="KMuraoka@lbl.gov",
)