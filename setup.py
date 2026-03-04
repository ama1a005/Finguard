"""Setup configuration for FinGuard-RAG package"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="finguard-rag",
    version="1.0.0",
    author="FinGuard Team",
    author_email="team@finguard.io",
    description="Secure RAG Built for Financial Compliance - India Edition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ama1a005/Finguard",
    project_urls={
        "Bug Tracker": "https://github.com/ama1a005/Finguard/issues",
        "Documentation": "https://github.com/ama1a005/Finguard/docs",
        "Source Code": "https://github.com/ama1a005/Finguard",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Financial",
        "Topic :: Software :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "python-dotenv>=0.19.0",
        "pyyaml>=6.0",
        "requests>=2.28.0",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "sentence-transformers>=2.2.0",
        "transformers>=4.30.0",
        "torch>=2.0.0",
        "fastapi>=0.103.0",
        "uvicorn>=0.23.0",
        "sqlalchemy>=2.0.0",
        "pydantic>=1.10.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "isort>=5.12.0",
            "mypy>=1.4.0",
            "sphinx>=7.0.0",
        ],
        "llm": [
            "openai>=0.27.0",
            "langchain>=0.0.280",
            "llama-index>=0.8.0",
        ],
        "vector-store": [
            "pinecone-client>=2.2.0",
            "chromadb>=0.3.0",
            "faiss-cpu>=1.7.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "finguard=src.main:cli",
        ],
    },
    include_package_data=True,
    keywords="rag retrieval-augmented-generation financial-compliance india rbi sebi",
    project_urls={
        "Homepage": "https://github.com/ama1a005/Finguard",
    },
)
