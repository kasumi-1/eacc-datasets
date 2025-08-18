# Example Dataset

## Description

This is an example dataset demonstrating the required structure and format for datasets in this repository. It contains information about individuals including their names, social media links, information sources, and optional quotes.

## Schema Overview

Each record in this dataset contains:

- **name** (required): The person's or entity's full name
- **social_links** (required): Array of social media and web presence links
  - platform: The platform name (Twitter, LinkedIn, GitHub, etc.)
  - url: Full URL to the profile
  - verified: Boolean indicating if the link has been verified
- **sources** (required): Array of information sources
  - title: Description of the source
  - url: Link to the source
  - accessed_date: When the source was accessed (ISO date format)
  - type: Type of source (article, website, paper, etc.)
- **quote** (optional): A notable quote from or about the person
- **tags** (optional): Array of categorization tags
- **last_updated** (optional): ISO 8601 datetime of when the record was last updated

## Data Sources

This example dataset uses fictional data for demonstration purposes. In a real dataset, sources might include:

- Official biographies and profiles
- News articles and interviews
- Academic papers and publications
- Social media profiles
- Conference and event websites

## Collection Methodology

For this example dataset, data would typically be collected through:

1. Manual research and verification of public information
2. Cross-referencing multiple sources for accuracy
3. Regular updates to ensure information remains current
4. Verification of social media links where possible

## Update Frequency

This example dataset is static. Real datasets should specify their update schedule (e.g., monthly, quarterly, or as-needed basis).

## Data Quality Notes

- All URLs should be validated and active at the time of data entry
- Social media links should be to official accounts where possible
- Sources should be reputable and publicly accessible
- Dates should be in ISO format for consistency

## License

This example dataset is provided under the MIT License for demonstration purposes. Real datasets should specify their actual license terms.

## Usage Examples

To read and process this dataset:

```python
import json

with open('data.jsonl', 'r') as f:
    for line in f:
        record = json.loads(line)
        print(f"Name: {record['name']}")
        print(f"Social links: {len(record['social_links'])}")
        print(f"Sources: {len(record['sources'])}")
        if 'quote' in record:
            print(f"Quote: {record['quote']}")
        print("---")
```

## Validation

This dataset can be validated using the repository's validation script:

```bash
python scripts/validate.py datasets/example-dataset
```

## Contributing

To contribute to this dataset:

1. Ensure new entries follow the schema exactly
2. Verify all URLs are working
3. Include at least one reliable source
4. Add appropriate tags for categorization
5. Update the last_updated field

## Contact

For questions about this example dataset, please open an issue in the repository.

## Changelog

- 2024-01-15: Initial example dataset created
- 2024-02-01: Added additional example entries
- 2024-03-15: Updated schema to include more optional fields
