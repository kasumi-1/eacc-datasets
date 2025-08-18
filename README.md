# EACC Dataset Repository

## Overview

This repository contains curated datasets in JSONL format. Each dataset follows a strict schema validation process to ensure data quality and consistency. All contributions are automatically validated through GitHub Actions.

## Repository Structure

```
.
├── README.md                 # This file
├── datasets/                 # All datasets live here
│   ├── example-dataset/     # Example dataset folder
│   │   ├── schema.json      # JSON Schema for validation
│   │   ├── data.jsonl       # Actual data in JSONL format
│   │   └── README.md        # Dataset-specific documentation
│   └── another-dataset/     # Another dataset
│       ├── schema.json
│       ├── data.jsonl
│       └── README.md
├── .github/
│   ├── workflows/
│   │   └── validate-datasets.yml  # GitHub Action for validation
│   └── pull_request_template.md   # PR template
└── scripts/
    └── validate.py          # Validation script
```

## Creating a New Dataset

### Step 1: Create Dataset Folder

Create a new folder under `datasets/` with a descriptive name using kebab-case:

```bash
mkdir datasets/your-dataset-name
```

### Step 2: Define Schema

Create a `schema.json` file in your dataset folder. This should be a valid JSON Schema (draft-07 or later). Example:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["name"],
  "properties": {
    "name": {
      "type": "string",
      "description": "The name of the entity"
    }
  }
}
```

### Step 3: Add Data

Create a `data.jsonl` file with your data. Each line should be a valid JSON object that conforms to your schema:

```jsonl
{"name": "Example 1", "optional_field": "value"}
{"name": "Example 2"}
```

### Step 4: Add Documentation

Create a `README.md` file in your dataset folder describing:
- What the dataset contains
- Data sources and collection methodology
- Any special considerations or limitations
- License information
- Update frequency (if applicable)

### Step 5: Submit PR

1. Fork the repository
2. Create a feature branch: `git checkout -b add-dataset-name`
3. Add your dataset files
4. Commit with a descriptive message: `git commit -m "Add dataset-name dataset"`
5. Push to your fork: `git push origin add-dataset-name`
6. Open a Pull Request using our template

## Validation Rules

All datasets must:

1. **Have a valid JSON Schema** (`schema.json`)
   - Must be valid JSON
   - Must be a valid JSON Schema (draft-07 or later)
   - Must define required fields

2. **Have valid JSONL data** (`data.jsonl`)
   - Each line must be valid JSON
   - Each record must validate against the schema
   - File must not be empty

3. **Have documentation** (`README.md`)
   - Must describe the dataset
   - Must include data sources

4. **Pass automated validation**
   - GitHub Actions will automatically validate your PR
   - All checks must pass before merge

## Local Validation

Before submitting a PR, you can validate your dataset locally:

```bash
# Install dependencies
pip install jsonschema

# Run validation
python scripts/validate.py datasets/your-dataset-name
```

## Example Dataset

See `datasets/example-dataset/` for a complete example with:
- Schema requiring `name` field
- Optional `social_links`, `sources`, and `quote` fields
- Sample data entries
- Complete documentation

## Contributing

We welcome contributions! Please:

1. Follow the structure and naming conventions
2. Ensure your data is properly licensed for inclusion
3. Validate your dataset before submitting
4. Use our PR template
5. Be responsive to review feedback

## Questions or Issues?

- Open an issue for bugs or problems
- Start a discussion for questions or suggestions
- Check existing issues before creating new ones

## License

Each dataset may have its own license. Check the individual dataset README files for specific licensing information.
