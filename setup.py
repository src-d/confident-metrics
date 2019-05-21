from importlib.machinery import SourceFileLoader
import io
import os.path

from setuptools import find_packages, setup

confident_metrics = SourceFileLoader("confident-metrics",
                                     "./confident_metrics/version.py").load_module()

with io.open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    long_description = f.read()

exclude_packages = (
    ("confident_metrics.tests", "confident_metrics.source")
    if not os.getenv("CONFIDENT_METRICS_SETUP_INCLUDE_TESTS", False)
    else ()
)


setup(
    name="confident-metrics",
    description="Python abstraction for runtime metrics collection built on top of Prometheus."
                " With confidence intervals!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=confident_metrics.__version__,
    license="Apache 2.0",
    author="source{d}",
    author_email="machine-learning@sourced.tech",
    url="https://github.com/src-d/confident-metrics",
    download_url="https://github.com/src-d/confident-metrics",
    packages=find_packages(exclude=exclude_packages),
    keywords=[
        "confident metrics",
        "prometheus",
    ],
    install_requires=[
        "prometheus_client==0.6.0",
    ],
    tests_require=["requests >=2.0,<3.0"],
    package_data={
        "": ["LICENSE.md", "README.md"],
    },
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
    ],
)
