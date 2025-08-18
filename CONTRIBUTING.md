# Contributing Guide

Welcome! This guide will help you contribute to our datasets, even if you've never used GitHub before.

## 🎯 Quick Start for Non-Technical Users

### Contributing Through GitHub's Website (No Downloads Needed!)

#### 1️⃣ Create a GitHub Account
If you don't have one, sign up at [github.com](https://github.com) - it's free!

#### 2️⃣ Navigate to the Dataset
1. Go to the `datasets` folder
2. Click on the dataset folder you want to contribute to (e.g., `ai-rights-opposition`)
3. Click on `data.jsonl`

#### 3️⃣ Edit the File
1. Click the **pencil icon** (✏️) at the top right
2. GitHub will automatically create a "fork" (your own copy) if needed

#### 4️⃣ Add Your Entry
Add a new line at the very end with your data. Copy this template and fill it in:

```json
{"name": "Person or Organization Name", "social_links": [{"platform": "Twitter", "url": "https://twitter.com/their_username"}], "sources": [{"title": "Article or Source Title", "url": "https://example.com/full-url-to-source"}]}
```

⚠️ **CRITICAL**: This must all be on ONE LINE in the file!

#### 5️⃣ Check Your Entry
Before saving, make sure:
- ✅ Everything is on one line
- ✅ All quotes are double `"` not single `'`
- ✅ All brackets match: `{` with `}` and `[` with `]`
- ✅ URLs start with `https://` or `http://`

#### 6️⃣ Save and Submit
1. Scroll down to "Commit changes"
2. Write a message like: `Add [Name] to dataset`
3. Select "Create a new branch"
4. Click "Propose changes"
5. Click "Create pull request"

## 🧪 How to Validate Your JSON

### Online Validator (Easiest)
1. Copy your entire line of JSON
2. Go to [jsonlines.org/validator](https://jsonlines.org/validator)
3. Paste and click "Validate"
4. Fix any errors shown in red

### Check in GitHub
After you submit, GitHub will automatically check your entry:
- ✅ **Green check** = Valid! Ready for review
- ❌ **Red X** = Has errors - click "Details" to see what's wrong

## 📋 JSON Format Examples

### Minimal Entry (Required Fields Only)
```json
{"name": "John Smith", "social_links": [], "sources": [{"title": "Interview on AI", "url": "https://news.com/interview"}]}
```

### Entry with Social Links
```json
{"name": "Jane Doe", "social_links": [{"platform": "Twitter", "url": "https://twitter.com/janedoe"}, {"platform": "LinkedIn", "url": "https://linkedin.com/in/janedoe"}], "sources": [{"title": "Blog Post", "url": "https://blog.com/post"}]}
```

### Entry with Quote
```json
{"name": "Organization Name", "social_links": [{"platform": "Website", "url": "https://org.com"}], "sources": [{"title": "Press Release", "url": "https://org.com/press"}], "quote": "AI should remain under human control."}
```

## 🚨 Common Errors and How to Fix Them

### Error: "Invalid JSON"
**Problem**: Syntax error in your JSON
**Fix**: Check for:
- Missing quotes around text
- Single quotes instead of double quotes
- Missing commas between items
- Extra commas at the end

### Error: "Missing required field"
**Problem**: You forgot name, social_links, or sources
**Fix**: Make sure you have all three, even if social_links is empty: `"social_links": []`

### Error: "Invalid URL format"
**Problem**: URL doesn't start with http:// or https://
**Fix**: Add https:// to the beginning of the URL

### Error: "Invalid platform"
**Problem**: Platform name not in allowed list
**Fix**: Use one of: Twitter, LinkedIn, GitHub, Facebook, Instagram, YouTube, Website, Other

## 📝 Writing Good Contributions

### For the AI Rights Opposition Dataset

✅ **Good Entry:**
- Clear source showing the person's position on AI rights
- Direct quote about AI personhood/rights (if available)
- Link to primary source (their own writing/speech)

❌ **Not Suitable:**
- General AI safety concerns without mentioning rights/personhood
- Second-hand reports without primary sources
- Private communications or unverified claims

## 🤝 Getting Help

### If You're Stuck

1. **Check existing entries** in the file for examples
2. **Open an issue** with your question
3. **Include your JSON** in the issue so others can help
4. **Be specific** about what error you're seeing

### Template for Asking for Help

```text
I'm trying to add [Name] to the [dataset name] dataset.

Here's my JSON:
[paste your JSON line here]

I'm getting this error:
[paste error message or describe the problem]

Can someone help me fix this?
```

## 🔄 After Submitting

1. **Watch for comments** on your pull request
2. **Respond to feedback** from reviewers
3. **Make requested changes** by editing your file again
4. **Celebrate** when it's merged! 🎉

## 📚 Advanced: Local Development

If you want to test locally before submitting:

### Install Python and Requirements
```bash
python3 -m pip install -r requirements.txt
```

### Validate Your Changes
```bash
python scripts/validate.py datasets/ai-rights-opposition
```

### Run Full Validation
```bash
# Check all datasets
for dir in datasets/*/; do
  python scripts/validate.py "$dir"
done
```

## 🎓 Learning Resources

- [GitHub's Hello World Tutorial](https://guides.github.com/activities/hello-world/)
- [Understanding JSON Format](https://www.json.org/json-en.html)
- [How Pull Requests Work](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

## ✨ Thank You!

Every contribution helps make these datasets more complete and valuable for research. Don't be discouraged if your first attempt has issues.
