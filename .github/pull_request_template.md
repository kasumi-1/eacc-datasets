## Dataset Submission Checklist

### Dataset Name
<!-- Enter the name of your dataset (should match folder name) -->
datasets/

### Type of Change
- [ ] New dataset
- [ ] Update to existing dataset
- [ ] Bug fix in existing dataset
- [ ] Documentation update

### Required Files
Please confirm all required files are included:
- [ ] `schema.json` - Valid JSON Schema file
- [ ] `data.jsonl` - Data file in JSONL format
- [ ] `README.md` - Dataset documentation

### Schema Validation
- [ ] Schema is valid JSON
- [ ] Schema follows JSON Schema draft-07 or later
- [ ] Schema includes all required field definitions
- [ ] Schema has appropriate validation rules (min/max lengths, patterns, etc.)

### Data Validation
- [ ] All records are valid JSON (one per line)
- [ ] All records conform to the schema
- [ ] No empty lines in the middle of the file
- [ ] File has at least one valid record

### Documentation
- [ ] README describes what the dataset contains
- [ ] README lists data sources
- [ ] README includes license information
- [ ] README describes any limitations or considerations
- [ ] README includes update frequency (if applicable)

### Local Validation
- [ ] I have run the validation script locally:
  ```bash
  python scripts/validate.py datasets/[your-dataset-name]
  ```
- [ ] All validation checks passed

### Data Source and Licensing
- [ ] Data is properly licensed for inclusion in this repository
- [ ] Sources are properly attributed
- [ ] No personally identifiable information (PII) without consent
- [ ] Complies with all relevant data protection regulations

### Description
<!-- Provide a brief description of your dataset and its purpose -->


### Additional Context
<!-- Add any other context, screenshots, or information about the dataset here -->


### Related Issues
<!-- Link any related issues here using #issue-number -->
Closes #

---

**Note:** The GitHub Action will automatically validate your dataset when you submit this PR. Please wait for the validation to complete and address any issues that arise.
