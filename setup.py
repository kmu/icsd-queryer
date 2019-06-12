from setuptools import setup

setup(
    version='0.0.2',
    name='icsd-queryer',
    install_requires=["PyYAML","beautifulsoup4", "selenium", "PyVirtualDisplay", "pandas", "tqdm"],
    entry_points={
        "console_scripts": [
            "icsd = app:main"
        ]
    },
    maintainer="Koki Muraoka",
    maintainer_email="KMuraoka@lbl.gov"
)
