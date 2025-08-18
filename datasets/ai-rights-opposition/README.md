# AI Rights Opposition Dataset

## Description

This dataset compiles individuals and organizations who have publicly expressed positions that artificial intelligence systems should not have the same legal rights, freedoms, or personhood status as humans. This includes those who advocate that AI should remain as tools under human control, without autonomous legal standing, rights to property, freedom of operation, or other rights typically granted to human persons or legal entities.

## Purpose

This dataset serves as a research resource for:
- Understanding perspectives on AI personhood and rights debates
- Tracking public positions on AI legal status
- Analyzing the discourse around AI autonomy and human primacy
- Academic research on AI rights philosophy and policy
- Documenting the landscape of human-centric AI governance

## Schema Overview

Each record in this dataset contains:

- **name** (required): The full name of the person or organization
- **social_links** (required): Array of verified social media and web presence
  - platform: Twitter, LinkedIn, GitHub, Facebook, Instagram, YouTube, Website, or Other
  - url: Direct link to the profile or page
- **sources** (required): Array of sources documenting their position
  - title: Description of the source
  - url: Link to the source material
- **quote** (optional): A relevant quote expressing their position on AI rights/personhood

## Inclusion Criteria

Entities are included in this dataset if they have publicly expressed that:

1. **AI should not have legal personhood** or rights equivalent to humans
2. **AI systems should remain tools** under human ownership and control
3. **Autonomous AI decision-making** should require human oversight/accountability
4. **AI should not have rights to**:
   - Own property or assets
   - Enter contracts independently
   - Have freedom of speech/expression
   - Claim consciousness-based rights
   - Operate without human oversight

## Exclusion Criteria

This dataset does NOT include:
- General AI safety concerns without addressing rights/personhood
- Technical discussions about AI capabilities
- Positions solely about current AI regulation/safety
- Views on data privacy or algorithmic bias
- Positions that are ambiguous on AI rights

## Important Note on Current Positions

As of 2025, the mainstream position among AI researchers, ethicists, and policymakers is that current AI systems are tools without consciousness or personhood. Most individuals in this dataset may not explicitly state "AI should not have rights" because this is generally assumed. Instead, their inclusion is based on:
- Explicit statements that AI should remain under human control
- Advocacy for human oversight requirements
- Positions that AI are tools, not entities deserving rights
- Opposition to AI autonomy or independent operation

## Data Sources

Information is gathered from:
- Public statements on AI consciousness and personhood
- Policy positions on AI governance
- Academic papers on AI ethics and rights
- Legislative testimony about AI regulation
- Books and articles about human-AI relationships
- Interviews and public speeches
- Company policies and principles

## Collection Methodology

1. **Position Identification**: Identify public statements about AI status, rights, or personhood
2. **Context Analysis**: Evaluate whether positions clearly indicate AI should not have human-like rights
3. **Verification**: Confirm positions through primary sources
4. **Documentation**: Provide reliable source URLs
5. **Updates**: Track if positions evolve over time

## Important Disclaimers

- **Emerging Debate**: The AI rights debate is nascent; most people haven't explicitly addressed it
- **Implicit Positions**: Many entries reflect implicit rather than explicit positions
- **Evolution**: Views on AI rights may change as technology advances
- **Context Required**: Full understanding requires reading source materials
- **No Endorsement**: Inclusion doesn't imply endorsement of any position

## Update Frequency

Updated as new explicit positions on AI rights and personhood emerge, particularly:
- After AI rights legal cases or proposals
- Following philosophical publications on AI personhood
- When new AI capabilities prompt rights discussions
- After significant AI consciousness claims

## Usage Guidelines

When using this dataset:
1. **Understand the context** - Many positions are implicit in broader statements
2. **Read sources** - Full context is essential for accuracy
3. **Note timeframes** - Positions may evolve with technology
4. **Avoid misrepresentation** - Don't overstate positions
5. **Consider nuance** - AI rights is a complex philosophical topic

## License

This dataset is provided under the [Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/1.0/). You are free to:
- Share: Copy and redistribute the material
- Adapt: Remix, transform, and build upon the material

Under the following terms:
- Attribution: You must give appropriate credit
- ShareAlike: If you remix or transform, you must distribute under the same license
- Notice: You must indicate if changes were made

## Contributing

To contribute:
1. Find explicit or clearly implicit positions on AI rights/personhood
2. Provide verifiable public sources
3. Include context about why position indicates opposition to AI rights
4. Follow the schema exactly
5. Submit a PR with clear documentation

## Contact

For questions or corrections:
- Open an issue in this repository
- Tag with `ai-rights-opposition` label
- Provide specific details about entries

## Changelog

- 2025-08-18: Initial dataset creation focusing on AI rights/personhood positions

## Citation

If you use this dataset in research or reporting, please cite as:
```text
AI Rights Opposition Dataset. (2025). 
eacc-datasets
Retrieved from https://github.com/semperai/eacc-datasets/tree/master/datasets/ai-rights-opposition
```
