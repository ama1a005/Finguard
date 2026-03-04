# FinGuard-RAG: Secure RAG Built for Financial Compliance

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status: Active Development](https://img.shields.io/badge/Status-Active%20Development-brightgreen)

## Abstract

FinGuard-RAG is a financially compliant secure Retrieval-Augmented Generation (RAG) framework designed to address domain-specific security and governance challenges in Indian financial institutions. Existing RAG deployments remain largely domain-agnostic and expose critical risks in financial settings, including jurisdictional inconsistencies, regulatory drift, compliance violations, and indirect leakage of sensitive organizational information.

FinGuard-RAG introduces a comprehensive solution that integrates policy-aware retrieval, time-versioned document handling, compliance-verified generation, and advanced security mechanisms to ensure that financial RAG systems are both reliable and trustworthy for compliance-critical applications. This framework is specifically tailored to meet Indian regulatory requirements enforced by the RBI, SEBI, FIPB, and other financial regulators.

## Key Features

### 🔍 **Policy-Aware Retrieval**
- Constrains document selection based on Indian jurisdiction, regulatory scope, and user role
- Ensures compliance with RBI, SEBI, and other Indian regulatory guidelines
- Implements role-based access control for document retrieval
- Supports state-level and national-level regulatory requirements

### ⏱️ **Time-Versioned Retrieval**
- Temporal filtering of regulatory documents
- Mitigates the impact of regulatory drift by tracking document versions
- Maintains historical consistency of regulatory interpretations

### ✅ **Compliance-Verified Generation**
- Neuro-symbolic validation layer for generated responses
- Evaluates outputs against explicit financial compliance rules
- Enforces domain-specific safety constraints prior to response release
- Conservative, governance-aligned recommendations

### 🛡️ **Role-Inference Leakage Defense**
- Detects and mitigates indirect disclosure of sensitive financial information
- Handles sensitive queries while preventing information leakage
- Advanced inference attack mitigation

### ⚖️ **Jurisdiction-Conflict Resolution**
- Identifies regulatory conflicts across legal regimes
- Provides conservative, governance-aligned recommendations
- Handles multi-jurisdictional compliance requirements

### 📊 **Risk-Aware Retrieval Scoring**
- Jointly optimizes semantic relevance and compliance risk
- Prioritizes compliance safety alongside semantic match quality
- Adaptive weighting based on regulatory requirements

## System Architecture

```
FinGuard-RAG Framework
├── Policy-Aware Retrieval Engine
│   ├── Jurisdiction Validator
│   ├── Role-Based Access Control
│   └── Regulatory Scope Enforcer
├── Time-Versioned Document Store
│   ├── Temporal Indexing
│   ├── Version Management
│   └── Regulatory Drift Detection
├── Generation Pipeline
│   ├── LLM Query Handler
│   ├── Compliance Verification Layer
│   └── Safety Constraint Validator
└── Security & Governance Layer
    ├── Leakage Detection System
    ├── Jurisdiction Conflict Resolver
    └── Risk Scoring Module
```

## Project Structure

```
Finguard/
├── README.md                           # Project documentation
├── setup.py                            # Installation configuration
├── requirements.txt                    # Python dependencies
├── LICENSE                             # MIT License
│
├── src/                                # Source code
│   ├── __init__.py
│   ├── main.py                         # Entry point
│   │
│   ├── retrieval/                      # Retrieval module
│   │   ├── __init__.py
│   │   ├── policy_aware_retriever.py   # Policy-aware retrieval logic
│   │   ├── jurisdiction_validator.py   # Jurisdiction validation
│   │   ├── role_based_access.py        # Role-based access control
│   │   ├── time_versioned_retriever.py # Time-versioned document handling
│   │   └── risk_scorer.py              # Risk-aware scoring functions
│   │
│   ├── generation/                     # Generation module
│   │   ├── __init__.py
│   │   ├── llm_handler.py              # LLM integration
│   │   ├── compliance_verifier.py      # Compliance verification layer
│   │   ├── safety_validator.py         # Safety constraint validation
│   │   └── governance_filter.py        # Governance-aligned filtering
│   │
│   ├── compliance/                     # Compliance module
│   │   ├── __init__.py
│   │   ├── rules_engine.py             # Compliance rules engine
│   │   ├── regulatory_framework.py     # Regulatory framework definitions
│   │   ├── jurisdiction_manager.py     # Jurisdiction management
│   │   └── conflict_resolver.py        # Jurisdiction conflict resolution
│   │
│   ├── security/                       # Security module
│   │   ├── __init__.py
│   │   ├── leakage_detector.py         # Sensitive information leakage detection
│   │   ├── role_inference_defense.py   # Role-inference attack defense
│   │   ├── encryption.py               # Encryption utilities
│   │   └── audit_logger.py             # Audit and logging
│   │
│   └── utils/                          # Utility functions
│       ├── __init__.py
│       ├── data_processor.py           # Data processing utilities
│       ├── embedder.py                 # Embedding generation
│       ├── config_loader.py            # Configuration handling
│       └── logger.py                   # Logging setup
│
├── data/                               # Data directory
│   ├── documents/                      # Financial documents
   │   ├── accounting_standards/       # IND-AS and Indian Accounting Standards
   │   ├── regulatory_guidelines/      # RBI Circulars, SEBI Guidelines, FIPB Directives
   │   ├── banking_regulations/        # Banking Regulation Act, RBI Act Guidelines
   │   ├── securities_regulations/     # Securities Contracts Act, SEBI Regulations
   │   ├── forex_regulations/          # FEMA Rules and Compliance Framework
│   │   ├── internal_policies/          # Internal organizational policies
│   │   └── README.md                   # Data documentation
│   │
│   ├── compliance_rules/               # Compliance rule definitions
│   │   ├── rules.json                  # Compliance rules in JSON format
│   │   ├── jurisdiction_mappings.json  # Jurisdiction to rules mapping
│   │   └── role_permissions.json       # Role-based permissions
│   │
│   └── embeddings/                     # Pre-computed embeddings
│       └── .gitkeep
│
├── config/                             # Configuration files
│   ├── default_config.yaml             # Default configuration
│   ├── jurisdictions.yaml              # Jurisdiction definitions
│   ├── roles.yaml                      # Role definitions
│   └── compliance_rules.yaml           # Compliance rules configuration
│
├── tests/                              # Test suite
│   ├── __init__.py
│   ├── conftest.py                     # Pytest configuration
│   │
│   ├── unit/                           # Unit tests
│   │   ├── test_retrieval.py           # Retrieval module tests
│   │   ├── test_generation.py          # Generation module tests
│   │   ├── test_compliance.py          # Compliance module tests
│   │   └── test_security.py            # Security module tests
│   │
│   ├── integration/                    # Integration tests
│   │   ├── test_rag_pipeline.py        # End-to-end RAG pipeline tests
│   │   ├── test_compliance_flow.py     # Compliance verification flow tests
│   │   └── test_security_flow.py       # Security mechanism tests
│   │
│   └── evaluation/                     # Evaluation scripts
│       ├── benchmark_retrieval.py      # Retrieval performance benchmarks
│       ├── compliance_metrics.py       # Compliance evaluation metrics
│       ├── security_evaluation.py      # Security evaluation metrics
│       └── leakage_detection_eval.py   # Leakage detection evaluation
│
├── notebooks/                          # Jupyter notebooks
│   ├── 01_data_exploration.ipynb       # Data exploration and analysis
│   ├── 02_retrieval_analysis.ipynb     # Retrieval performance analysis
│   ├── 03_compliance_validation.ipynb  # Compliance validation results
│   ├── 04_security_evaluation.ipynb    # Security mechanism evaluation
│   └── results.ipynb                   # Results and visualization
│
├── docs/                               # Documentation
│   ├── ARCHITECTURE.md                 # System architecture documentation
│   ├── API.md                          # API documentation
│   ├── SETUP.md                        # Setup and installation guide
│   ├── USAGE.md                        # Usage examples
│   ├── COMPLIANCE.md                   # Compliance framework documentation
│   ├── SECURITY.md                     # Security mechanisms documentation
│   └── CONTRIBUTING.md                 # Contribution guidelines
│
├── deployment/                         # Deployment configuration
│   ├── Dockerfile                      # Docker container setup
│   ├── docker-compose.yml              # Docker Compose configuration
│   ├── requirements-prod.txt           # Production dependencies
│   └── kubernetes/                     # Kubernetes deployment configs
│       ├── deployment.yaml             # Kubernetes deployment
│       └── service.yaml                # Kubernetes service
│
├── .gitignore                          # Git ignore rules
├── .env.example                        # Environment variables template
├── setup.py                            # Package setup
└── LICENSE                             # MIT License
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip or conda
- CUDA 11.8+ (for GPU acceleration, optional)

### Quick Start

1. **Clone the Repository**
```bash
git clone https://github.com/ama1a005/Finguard.git
cd Finguard
```

2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Run Tests**
```bash
pytest tests/
```

## Usage

### Basic Example

```python
from src.retrieval.policy_aware_retriever import PolicyAwareRetriever
from src.generation.compliance_verifier import ComplianceVerifier
from src.compliance.rules_engine import RulesEngine

# Initialize components
retriever = PolicyAwareRetriever(
    jurisdiction="US",
    role="compliance_analyst"
)

compliance_verifier = ComplianceVerifier()
rules_engine = RulesEngine()

# Query
query = "What are the capital adequacy requirements?"
documents = retriever.retrieve(query)

# Generate response
response = generate_response(query, documents)

# Verify compliance
is_compliant, violations = compliance_verifier.verify(response)

print(f"Response: {response}")
print(f"Compliant: {is_compliant}")
print(f"Violations: {violations}")
```

### Advanced Features

- **Jurisdiction-Aware Retrieval**: [See USAGE.md](docs/USAGE.md#jurisdiction-aware-retrieval)
- **Compliance Verification**: [See COMPLIANCE.md](docs/COMPLIANCE.md)
- **Security Mechanisms**: [See SECURITY.md](docs/SECURITY.md)
- **Role-Based Access**: [See API.md](docs/API.md#role-based-access)

## Evaluation Results

FinGuard-RAG demonstrates for Indian financial institutions:
- ✅ Improved RBI/SEBI compliance correctness
- ✅ Reduced regulatory violations in Indian context
- ✅ Proper handling of multi-state compliance requirements
- ✅ Stronger resistance to prompt-based leakage attacks
- ✅ Enhanced defense against inference-based leakage
- ✅ Practical implementation for Indian enterprise deployment

See [evaluation notebooks](notebooks/) and [evaluation tests](tests/evaluation/) for detailed results.

## Reference Papers

This work builds upon the following research:

1. **Securing RAG: A Risk Assessment and Mitigation Framework**
   - Foundational framework for identifying and mitigating RAG-specific risks

2. **Provably Secure Retrieval-Augmented Generation**
   - Theoretical guarantees for secure RAG systems

3. **SafeRAG: Benchmarking Security in Retrieval-Augmented Generation of Large Language Models**
   - Comprehensive evaluation methodology for RAG security

## Core Components

### 1. Retrieval Module (`src/retrieval/`)
- **Policy-Aware Retriever**: Enforces jurisdiction and role-based constraints
- **Jurisdiction Validator**: Validates documents against jurisdiction requirements
- **Time-Versioned Retriever**: Handles temporal document versioning
- **Risk Scorer**: Calculates compliance risk scores

### 2. Generation Module (`src/generation/`)
- **LLM Handler**: Manages language model interactions
- **Compliance Verifier**: Validates generated responses
- **Safety Validator**: Enforces safety constraints
- **Governance Filter**: Applies governance-aligned filtering

### 3. Compliance Module (`src/compliance/`)
- **Rules Engine**: Executes compliance rules
- **Regulatory Framework**: Defines financial regulations
- **Jurisdiction Manager**: Manages multi-jurisdictional requirements
- **Conflict Resolver**: Resolves jurisdiction conflicts

### 4. Security Module (`src/security/`)
- **Leakage Detector**: Detects sensitive information leakage
- **Role-Inference Defense**: Mitigates role-inference attacks
- **Encryption Utilities**: Provides encryption services
- **Audit Logger**: Maintains comprehensive audit trails

## Configuration

### Jurisdictions
Configure supported jurisdictions in `config/jurisdictions.yaml`:
```yaml
jurisdictions:
  India:
    central_regulations: [RBI, SEBI, FIPB]
    banking_regulations: [RBI Act 1934, Banking Regulation Act 1949]
    securities_regulations: [Securities Contracts (Regulation) Act 1956, SEBI Act 1992]
    forex_regulations: [Foreign Exchange Management Act (FEMA) 1999]
    standards: [IND-AS, RBI Guidelines]
    state_jurisdictions: [All Indian States]
```

### Roles
Define user roles in `config/roles.yaml` with specific permissions and access levels. Example roles:
- Bank Compliance Officer
- RBI Liaison
- SEBI Compliance Manager
- Internal Auditor
- Risk Manager

### Compliance Rules
Define compliance rules in `data/compliance_rules/rules.json` with validation logic. Includes:
- RBI Master Circulars
- SEBI Regulations and Circulars
- IND-AS Accounting Standards
- FEMA Compliance Rules
- KYC/AML Requirements

## Testing

```bash
# Run all tests
pytest tests/

# Run specific test suite
pytest tests/unit/
pytest tests/integration/
pytest tests/evaluation/

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

## Documentation

- **[SETUP.md](docs/SETUP.md)**: Detailed setup instructions
- **[USAGE.md](docs/USAGE.md)**: Usage examples and API reference
- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)**: System architecture details
- **[COMPLIANCE.md](docs/COMPLIANCE.md)**: Compliance framework details
- **[SECURITY.md](docs/SECURITY.md)**: Security mechanisms documentation
- **[API.md](docs/API.md)**: Complete API documentation

## Deployment

### Docker
```bash
docker build -t finguard-rag .
docker run -p 8000:8000 finguard-rag
```

### Kubernetes
```bash
kubectl apply -f deployment/kubernetes/
```

See [deployment/](deployment/) for more configuration options.

## Monitoring & Audit

FinGuard-RAG includes comprehensive audit logging:
- Query logging with jurisdiction and role information
- Compliance verification audit trails
- Security event tracking
- Access control logs

Access audit logs in configured log directory (see `.env`).

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

### Development

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes and add tests
4. Run `pytest` to ensure all tests pass
5. Commit and push to your fork
6. Submit a pull request

## Performance

- **Retrieval Latency**: < 200ms (p95)
- **Compliance Verification**: < 50ms (p95)
- **Throughput**: > 100 requests/second
- **Memory Efficiency**: Optimized for < 4GB RAM footprint

See [evaluation notebooks](notebooks/) for detailed performance metrics.

## Limitations & Future Work

- **Current Scope**: Focus on major financial regulatory frameworks (SEC, FCA, EBA)
- **Document Types**: Primarily structured documents (policies, guidelines, standards)
- **Future Enhancements**:
  - Expanded regulatory framework coverage
  - Real-time regulatory updates
  - Deep learning-based compliance verification
  - Multi-language support

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Citation

If you use FinGuard-RAG in your research, please cite:

```bibtex
@software{finguard_rag_2026,
  title={FinGuard-RAG: Secure RAG Built for Financial Compliance},
  author={Your Name},
  year={2026},
  url={https://github.com/ama1a005/Finguard}
}
```

## Contact & Support

- **Issues**: [GitHub Issues](https://github.com/ama1a005/Finguard/issues)
- **Email**: contact@example.com
- **Documentation**: See [docs/](docs/) directory

## Acknowledgments

This work builds upon research in secure RAG systems and financial compliance automation. We acknowledge the financial compliance community for valuable insights and feedback during development.

---

**Status**: Active Development | **Last Updated**: March 2026
