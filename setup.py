from setuptools import setup
import metadata

setup(
    name=metadata.project,
    install_requires=["PyYAML","beautifulsoup4", "selenium", "PyVirtualDisplay", "pandas"],
    entry_points={
        "console_scripts": [
            "icsd = app:main"
        ]
    },
    maintainer="Koki Muraoka",
    maintainer_email="KMuraoka@lbl.gov",
    version=metadata.version
)