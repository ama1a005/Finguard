# FinGuard-RAG: Secure RAG Built for Financial Compliance

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status: Active Development](https://img.shields.io/badge/Status-Active%20Development-green.svg)

## Abstract

FinGuard-RAG is a financially compliant Retrieval-Augmented Generation (RAG) framework designed for Indian financial institutions. It addresses domain-specific challenges including jurisdictional inconsistencies, regulatory drift, and compliance violations.

This framework integrates **policy-aware retrieval**, **time-versioned document handling**, and **compliance-verified generation** to ensure that financial RAG systems are reliable and trustworthy for compliance-critical applications. It is specifically tailored to meet Indian regulatory requirements enforced by the RBI, SEBI, FIPB, and other financial regulators.

---

## Core Features (Current Scope)

### 🔍 Policy-Aware Retrieval
- Role-based document filtering (e.g., Compliance Analyst, Auditor, Risk Manager)
- Jurisdiction-aware retrieval constrained to Indian regulatory scope
- Metadata-based filtering to ensure only relevant regulatory documents are retrieved

### ⏱️ Time-Versioned Retrieval
- Temporal filtering that prioritizes newer circulars and guidelines over older ones
- Mitigates regulatory drift by tracking document effective dates
- Ensures responses reflect the most current regulatory interpretation

### ✅ Compliance-Verified Generation
- Post-generation validation layer that checks responses against known compliance rules
- Keyword and rule-based checks (e.g., correct regulatory body citations, prohibited advice)
- Secondary LLM call to flag potential violations before response is returned
- Conservative, governance-aligned output

### 🖥️ Streamlit Demo UI *(if time permits)*
- Simple query interface with role selector
- Displays retrieved documents alongside generated response
- Shows compliance check results

---

## System Architecture

```
FinGuard-RAG Framework
├── Document Ingestion
│   └── RBI/SEBI PDF loader + chunker
├── Embedding + Vector Store (FAISS / ChromaDB)
├── Policy-Aware Retrieval Engine
│   ├── Role-Based Metadata Filter
│   └── Temporal Document Filter
├── Generation Pipeline
│   ├── LLM Query Handler (Gemini / OpenAI)
│   └── Compliance Verification Layer
└── (Optional) Streamlit UI
```

---

## Project Structure

```
Finguard/
├── README.md
├── requirements.txt
├── setup.py
├── .env.example
├── .gitignore
├── LICENSE
│
├── src/
│   ├── __init__.py
│   ├── main.py                          # Entry point
│   │
│   ├── retrieval/
│   │   ├── __init__.py
│   │   ├── policy_aware_retriever.py    # Role + jurisdiction filtering
│   │   ├── time_versioned_retriever.py  # Temporal document filtering
│   │   └── embedder.py                  # Embedding generation
│   │
│   ├── generation/
│   │   ├── __init__.py
│   │   ├── llm_handler.py               # LLM API integration
│   │   └── compliance_verifier.py       # Post-generation compliance check
│   │
│   └── utils/
│       ├── __init__.py
│       ├── data_processor.py            # PDF loading and chunking
│       └── config_loader.py             # Config and env handling
│
├── data/
│   ├── documents/
│   │   ├── rbi_circulars/               # RBI Master Circulars
│   │   ├── sebi_guidelines/             # SEBI Regulations
│   │   └── README.md
│   │
│   ├── compliance_rules/
│   │   ├── rules.json                   # Compliance rule definitions
│   │   └── role_permissions.json        # Role-based access permissions
│   │
│   └── embeddings/
│       └── .gitkeep
│
├── config/
│   ├── default_config.yaml
│   ├── roles.yaml                       # Role definitions and permissions
│   └── compliance_rules.yaml
│
├── tests/
│   ├── __init__.py
│   ├── test_retrieval.py
│   ├── test_generation.py
│   └── test_compliance.py
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_retrieval_analysis.ipynb
│   └── 03_compliance_validation.ipynb
│
└── docs/
    ├── ARCHITECTURE.md
    ├── SETUP.md
    ├── USAGE.md
    └── COMPLIANCE.md
```

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Quick Start

```bash
# Clone the repository
git clone https://github.com/ama1a005/Finguard.git
cd Finguard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys (OpenAI / Gemini)
```

---

## Usage

### Basic Example

```python
from src.retrieval.policy_aware_retriever import PolicyAwareRetriever
from src.generation.llm_handler import LLMHandler
from src.generation.compliance_verifier import ComplianceVerifier

# Initialize with role and jurisdiction
retriever = PolicyAwareRetriever(
    role="compliance_analyst",
    jurisdiction="India"
)

llm = LLMHandler()
verifier = ComplianceVerifier()

# Query
query = "What are the capital adequacy requirements under RBI guidelines?"
documents = retriever.retrieve(query)

# Generate response
response = llm.generate(query, documents)

# Verify compliance
is_compliant, violations = verifier.verify(response)

print(f"Response: {response}")
print(f"Compliant: {is_compliant}")
print(f"Violations: {violations}")
```

---

## Configuration

### Roles (`config/roles.yaml`)

```yaml
roles:
  compliance_analyst:
    access: [rbi_circulars, sebi_guidelines]
    description: Full access to regulatory documents
  auditor:
    access: [rbi_circulars]
    description: Read-only access to banking regulations
  risk_manager:
    access: [rbi_circulars, sebi_guidelines]
    description: Access to risk-related regulatory documents
```

### Compliance Rules (`data/compliance_rules/rules.json`)

```json
{
  "rules": [
    {
      "id": "R001",
      "description": "Response must cite correct regulatory body",
      "check": "regulatory_body_present"
    },
    {
      "id": "R002",
      "description": "Response must not provide direct investment advice",
      "check": "no_direct_investment_advice"
    }
  ]
}
```

---

## Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

---

## Future Work *(Out of current scope)*

The following features are planned for future iterations but are not part of the current implementation:

- 🛡️ Role-inference leakage detection and defense
- ⚖️ Multi-jurisdiction conflict resolution
- 🔐 Encryption utilities and audit logging
- 🌐 Real-time regulatory updates from RBI and SEBI
- 🗣️ Multi-language support (Hindi, regional languages)
- ☸️ Docker / Kubernetes deployment

---

## Reference Papers

This work builds upon the following research:

- *Securing RAG: A Risk Assessment and Mitigation Framework*
- *Provably Secure Retrieval-Augmented Generation*
- *SafeRAG: Benchmarking Security in Retrieval-Augmented Generation of Large Language Models*

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## Citation

```bibtex
@software{finguard_rag_2026,
  title={FinGuard-RAG: Secure RAG Built for Financial Compliance},
  author={Your Name},
  year={2026},
  url={https://github.com/ama1a005/Finguard}
}
```

---

## Contact & Support

- **Issues:** [GitHub Issues](https://github.com/ama1a005/Finguard/issues)
- **Documentation:** See `docs/` directory

---

*Status: Active Development | Last Updated: April 2026*
