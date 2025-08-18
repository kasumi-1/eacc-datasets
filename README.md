# Dataset Repository

## Overview

This repository contains curated datasets in JSONL format. Each dataset follows a strict schema validation process to ensure data quality and consistency. All contributions are automatically validated through GitHub Actions.

## 📊 Available Datasets

### [AI Rights Opposition](datasets/ai-rights-opposition/)
A comprehensive dataset documenting individuals and organizations who have publicly expressed that AI systems should not have legal rights or personhood equivalent to humans. This includes those advocating that AI should remain as tools under human control.

*Browse more datasets in the [`datasets/`](datasets/) directory.*

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
pip install -r requirements.txt

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

### 🚀 Contributing Using GitHub's Web Interface

You can contribute to datasets directly through GitHub's website without installing any software. Here's how:

#### Step 1: Find the Dataset You Want to Contribute To

1. Navigate to the [`datasets`](datasets/) folder
2. Click on the dataset you want to update (e.g., `ai-rights-opposition`)
3. Click on the `data.jsonl` file

#### Step 2: Edit the File

1. Click the **pencil icon** (✏️) in the top-right corner of the file view
2. You'll see the file contents in an editor

#### Step 3: Add Your Entry

Add a new line at the end of the file with your data. Here's the format:

```json
{"name": "Person Name", "social_links": [{"platform": "Twitter", "url": "https://twitter.com/username"}], "sources": [{"title": "Article Title", "url": "https://example.com/article"}], "quote": "Optional quote here"}
```

**Important formatting rules:**
- Everything must be on ONE line
- Use double quotes `"` not single quotes `'`
- URLs must start with `https://` or `http://`
- Don't add a comma at the end of the line
- Make sure all brackets `{}` and `[]` are properly closed

#### Step 4: Validate Your JSON

Before submitting, validate your JSON entry:

1. Copy your entire line
2. Go to [jsonlines.org/validator](https://jsonlines.org/validator)
3. Paste your line and click "Validate JSON"
4. Fix any errors it shows

#### Step 5: Preview and Commit

1. Scroll down to "Commit changes"
2. Add a title like: `Add [Person Name] to dataset`
3. Add a description explaining why this person/org belongs in the dataset
4. Select "Create a new branch" (it will suggest a name)
5. Click "Propose changes"

#### Step 6: Create Pull Request

1. GitHub will take you to a "Pull Request" page
2. Fill out the template that appears
3. Click "Create pull request"

#### Step 7: Wait for Validation

Our automated system will check your contribution. You'll see:
- ✅ **Green checkmark**: Your entry is valid and ready for review!
- ❌ **Red X**: There's an issue - click "Details" to see what needs fixing

If validation fails, click the pencil icon again on your branch to fix the issues.

**Remember:** In the JSONL file, each entry must be on a single line!

### 🔍 Common Mistakes to Avoid

1. **Using single quotes** - Always use double quotes: `"name"` not `'name'`
2. **Line breaks** - Everything must be on ONE line in JSONL format
3. **Trailing commas** - Don't add a comma after the last item in an object or array
4. **Missing brackets** - Ensure all `{`, `}`, `[`, `]` are properly paired
5. **Invalid URLs** - URLs must start with `http://` or `https://`
6. **Wrong platform names** - Use exact platform names from the allowed list

### 💡 Tips for Non-Technical Contributors

- **Use a JSON validator** before submitting to catch errors early
- **Start small** - Try adding just one entry first
- **Check existing entries** as examples of proper formatting

## Questions or Issues?

- Open an issue for bugs or problems
- Start a discussion for questions or suggestions
- Check existing issues before creating new ones

## License

Each dataset may have its own license. Check the individual dataset README files for specific licensing information.
