# FinGuard-RAG Data Directory - India-Specific Documentation

This directory contains all data files used by the FinGuard-RAG system for Indian financial compliance.

## Directory Structure

### `documents/`
Contains the financial documents and regulatory guidelines specific to Indian financial institutions.

#### `accounting_standards/`
- **Indian Accounting Standards (IND-AS)**: Standards aligned with IFRS but adapted for the Indian context
- **GAAP Requirements**: General Accepted Accounting Principles as applied in India
- Covers standards like:
  - IND-AS 1: Presentation of Financial Statements
  - IND-AS 8: Accounting Policies
  - IND-AS 36: Impairment of Assets
  - IND-AS 109: Financial Instruments

#### `regulatory_guidelines/`
- **RBI Master Circulars**: Guidelines from the Reserve Bank of India
  - Banking Regulation Circulars
  - Monetary Policy Guidelines
  - Financial Stability Directives
  
- **SEBI Regulations and Circulars**: Securities and Exchange Board guidelines
  - Listing Obligation Regulations
  - Insider Trading Prevention Rules
  - Market Conduct Guidelines

- **FIPB/DPIIT Directives**: Foreign Investment Promotion Board guidelines
  - FDI Sector-Specific Rules
  - Approval Procedures
  - Compliance Requirements

#### `banking_regulations/`
- **RBI Act, 1934**: Core legislation for RBI operations
- **Banking Regulation Act, 1949**: Regulatory framework for banks
- **Payment and Settlement Systems Act, 2007**: Rules for payment systems
- **Bharatiya Reserve Bank of India Act, 2023**: Modified RBI framework

#### `securities_regulations/`
- **Securities Contracts (Regulation) Act, 1956**: Foundation for securities regulation
- **SEBI Act, 1992**: Regulatory authority framework
- **Depositories Act, 1996**: Rules for securities depositories
- **Corporate Governance Norms**: SEBI Board Composition Requirements

#### `forex_regulations/`
- **FEMA Rules**: Foreign Exchange Management Act compliance
- **Liberalised Remittance Scheme**: Rules for resident remittances
- **Export-Import Regulations**: Import-Export compliance
- **Foreign Direct Investment Policy**: FDI sector-wise allocations

#### `internal_policies/`
- Organization-specific compliance policies
- Internal control procedures
- Risk management frameworks
- Data governance policies

### `compliance_rules/`
Contains structured compliance rules and mappings.

#### `rules.json`
Comprehensive compliance rules database with:
- **Rule ID**: Unique identifier for each rule
- **Regulator**: Responsible regulatory body (RBI, SEBI, FIPB, etc.)
- **Regulation**: Specific Act or Regulation
- **Jurisdiction**: Applicable jurisdiction (India)
- **Description**: Natural language description of the rule
- **Validation Type**: How the rule is validated (numerical, document, behavioral, etc.)
- **Severity**: Critical, High, Medium, Low
- **Automatic Enforcement**: Whether the system can automatically verify

##### Current Rules Covered:
1. **RBI Rules** (4 rules):
   - Capital Adequacy Requirements
   - KYC Compliance
   - Loan Loss Provisioning
   - Large Exposure Limits

2. **SEBI Rules** (3 rules):
   - Disclosure Requirements
   - Corporate Governance
   - Insider Trading Prevention

3. **IND-AS Rules** (2 rules):
   - First-time Adoption
   - Asset Impairment

4. **FEMA Rules** (2 rules):
   - Foreign Direct Investment
   - Remittance Limits

5. **Other Rules** (4 rules):
   - GST Compliance (CBIC)
   - AML/CFT (RBI)
   - IT Act (Ministry of Electronics and IT)
   - Digital Personal Data Protection

#### `jurisdiction_mappings.json` (Optional)
Maps jurisdictions to applicable rules.

#### `role_permissions.json` (Optional)
Defines what documents/rules each role can access.

### `embeddings/`
Pre-computed vector embeddings for documents:
- Dense vector representations of documents
- Used for semantic similarity search
- Format: Typically saved as numpy arrays or pickle files
- File naming: `{document_category}_{date}.pkl` or similar

## Document Format Guidelines

### For Regulatory Documents
- **File Format**: PDF, TXT, or Markdown
- **Metadata**: Include regulation ID, effective date, jurisdiction, version
- **Structure**: Clear headings, numbered sections, subsection references
- **Example**: `RBI_Master_Circular_Banking_Regulation_v2.0_2024.pdf`

### For Internal Policies
- **File Format**: DOCX, PDF, or Markdown
- **Metadata**: Policy ID, version, last reviewed date, next review date
- **Structure**: Purpose, Scope, Policy Statement, Implementation, References

### For Compliance Rules
- **File Format**: JSON or YAML
- **Structure**: Must include rule_id, regulator, regulation, jurisdiction, validation_type
- **Validation**: JSONL or JSON Schema validation

## Key Indian Regulators

### Reserve Bank of India (RBI)
- **Scope**: Banking, payment systems, monetary policy
- **Key Guidelines**: Master Circulars, Policy Statements
- **Website**: https://www.rbi.org.in
- **Updates**: Quarterly review cycles

### Securities and Exchange Board of India (SEBI)
- **Scope**: Securities markets, derivatives, investors protection
- **Key Guidelines**: SEBI Regulations, Circulars
- **Website**: https://www.sebi.gov.in
- **Updates**: Periodic as per market requirements

### Foreign Investment Promotion Board (FIPB)
- **Scope**: Foreign direct investment screening
- **Key Documents**: FDI Policy, Sectoral Guidelines
- **Website**: https://dpiit.gov.in
- **Updates**: Annual policy announcements

### Ministry of Corporate Affairs (MCA)
- **Scope**: Company law, accounting standards
- **Key Documents**: Companies Act, Notification for IND-AS
- **Website**: https://www.mca.gov.in

### Central Board of Indirect Taxes and Customs (CBIC)
- **Scope**: GST, indirect taxes, customs
- **Key Documents**: GST Act, Rules, Circulars
- **Website**: https://www.cbic.gov.in

## Data Versioning

All regulatory documents should be versioned with:
- **Version Number**: e.g., v1.0, v2.1
- **Effective Date**: When the document becomes effective
- **Last Updated**: Last modification date
- **Next Review**: When the document should be reviewed

## Compliance with Data Privacy

All data in this directory must comply with:
- **DPDPA 2023**: Digital Personal Data Protection Act
- **IT Act 2000**: Information Technology Act
- **RBI Guidelines**: On data privacy in banking
- **Internal Data Governance**: Organization-specific policies

## Adding New Documents

1. Place document in appropriate subdirectory under `documents/`
2. Add metadata (regulation ID, date, version, jurisdiction)
3. Update relevant compliance rules if new regulations introduced
4. Generate or update embeddings
5. Update this README with new regulatory references

## Compliance Rule Updates

The `rules.json` file should be updated:
- **Quarterly**: After RBI, SEBI policy announcements
- **As Needed**: When new regulations are introduced
- **Version Control**: Maintain changelog of rule updates

Last Updated: March 4, 2026
Next Review: June 4, 2026
