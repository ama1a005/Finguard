# FinGuard-RAG: Secure Financial Compliance Framework

**FinGuard-RAG** is a specialized Retrieval-Augmented Generation (RAG) system designed for multinational financial institutions. [cite_start]Unlike standard RAG deployments, it integrates a "Security-First" architecture to handle jurisdictional conflicts, regulatory drift, and sensitive data leakage [cite: 841, 843-845].

## 🚀 Key Features

* [cite_start]**Policy-Aware Retrieval (RBAC):** Constrains document access based on the user's specific role (e.g., CEO vs. Junior Analyst) and location[cite: 847].
* [cite_start]**Time-Versioned Retrieval:** Mitigates "Regulatory Drift" by prioritizing the most recent laws (e.g., favoring 2026 circulars over older versions)[cite: 848].
* [cite_start]**Compliance-Verified Generation:** A neuro-symbolic validation layer that scans AI responses for violations before they reach the user[cite: 849].
* [cite_start]**Role-Inference Leakage Defense:** Detects and blocks indirect attempts to uncover sensitive company secrets like salary bands or M&A data[cite: 850].
* [cite_start]**Jurisdiction-Conflict Resolution:** Identifies and explains contradictions between different legal regimes (e.g., Ind AS vs. IFRS)[cite: 851].

## 🏗️ System Architecture

The system operates as a multi-stage security pipeline:
1.  **Request Phase:** The user query is routed through an **RBAC & Query Router** that identifies role and jurisdiction.
2.  **Retrieval Phase:** The **Policy-Aware Retrieval** module consults the **Support Modules** (Document Store and Risk Scorer) to fetch only authorized, low-risk data.
3.  **Generation Phase:** The **LLM Generator** (Gemini 1.5 Flash) produces a draft response based on the "Safe Draft".
4.  **Validation Phase:** The **Compliance Validator** cross-checks the answer against rules in the **Guard Modules** before final release.



## 🛠️ Tech Stack

* [cite_start]**Frontend:** React (Lucide-React, Headless UI)[cite: 288, 301].
* [cite_start]**Backend:** FastAPI (Python)[cite: 673, 675].
* [cite_start]**Vector Database:** ChromaDB[cite: 264, 274].
* [cite_start]**LLM:** Gemini 1.5 Flash[cite: 76].
* [cite_start]**Embeddings:** Sentence-Transformers (`all-MiniLM-L6-v2`)[cite: 273, 811].

## 📂 Project Structure

```text
finguard-rag/
├── data/
│   ├── corpus/               
│   │   ├── sebi/             # Real SEBI PDFs
│   │   ├── rbi/              # Real RBI PDFs
│   │   ├── mca/              # Real MCA PDFs
│   │   ├── icai/             # Real Accounting Standards
│   │   └── synthetic/        # Internal Policy documents
│   └── chroma_db/            # Vector store storage
├── finguard_rag/
│   ├── ingestion/            # M1: Data processing & chunking
│   ├── agent/                # Core RAG logic & Gemini integration
│   ├── api/                  # FastAPI endpoints
│   └── defense/              # Leakage & security modules
└── frontend/                 # React application
