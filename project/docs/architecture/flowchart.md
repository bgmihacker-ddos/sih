# FORENSIGHT SIH V2 Architecture

```mermaid
graph TD
    User([Analyst]) --> API[FastAPI Portal]
    API --> Evidence[Evidence Service]
    Evidence --> Storage[(Safe Storage)]
    API --> Engine[Robust Forensic Engine]
    Engine --> Findings[Findings DB]
    Engine --> Intel[Threat Intelligence]
    Findings --> Graph[Infrastructure Graph]
    Findings --> Report[Report Generator]
```

## Description
This diagram illustrates the data flow:
1. **Analyst** uploads raw EML via the API.
2. **Evidence Service** handles secure storage and hashing.
3. **Forensic Engine** performs standalone analysis.
4. Extracted IOCs and Findings populate the **Database** and are rendered in the **Infrastructure Graph** and **Report Generator**.
