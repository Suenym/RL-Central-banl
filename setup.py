from setuptools import setup, find_packages

setup(
    name="macrofinance-llm-sim",
    version="0.1.0",
    description="LLM-persona macroeconomic RL environment",
    packages=find_packages(include=["envs", "envs.*", "src", "src.*"]),
    install_requires=[
        "gym>=0.26",
        "numpy",
        "pandas",
        "pyyaml",
        "torch>=1.12",
        "pytest",
        "sphinx",
    ],
    python_requires=">=3.8",
)
