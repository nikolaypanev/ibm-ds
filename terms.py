import pandas as pd

# Create the data as a list of dictionaries
data = [
    {"Letter": "A", "Term": "Atlas", "Style/Tone": "Formal/Visual", "Notes": "Often geographical, but metaphorical use works well"},
    {"Letter": "A", "Term": "Anthology", "Style/Tone": "Formal/Curated", "Notes": "Best when collecting pieces or entries"},
    {"Letter": "B", "Term": "Brief", "Style/Tone": "Professional", "Notes": "Concise, high-level overview"},
    {"Letter": "B", "Term": "Blueprint", "Style/Tone": "Practical/Casual", "Notes": "Strategy or step-by-step plan feel"},
    {"Letter": "C", "Term": "Chartbook", "Style/Tone": "Visual/Technical", "Notes": "Data-heavy or summarized tables"},
    {"Letter": "C", "Term": "Compendium", "Style/Tone": "Formal/Academic", "Notes": "Core original term"},
    {"Letter": "D", "Term": "Digest", "Style/Tone": "Casual/Concise", "Notes": "Popular in blogs/news contexts too"},
    {"Letter": "D", "Term": "Directory", "Style/Tone": "Practical/List-based", "Notes": "Good for resources or links"},
    {"Letter": "D", "Term": "Dossier", "Style/Tone": "Formal/Structured", "Notes": "Sounds official or secret-agent-y"},
    {"Letter": "E", "Term": "Encyclopaedia", "Style/Tone": "Academic/Comprehensive", "Notes": "Classic reference vibe"},
    {"Letter": "E", "Term": "Essentials", "Style/Tone": "Casual/Friendly", "Notes": "Great for minimalistic or 'starter' guides"},
    {"Letter": "F", "Term": "Factbook", "Style/Tone": "Formal/Informative", "Notes": "Data-driven summary, great for stats"},
    {"Letter": "F", "Term": "Field Guide", "Style/Tone": "Practical/Naturalist", "Notes": "Ideal for observational or real-world reference"},
    {"Letter": "G", "Term": "Guide", "Style/Tone": "Versatile/Universal", "Notes": "Go-to word for any how-to"},
    {"Letter": "G", "Term": "Glossary", "Style/Tone": "Academic/Defined", "Notes": "Best for terminology-heavy subjects"},
    {"Letter": "H", "Term": "Handbook", "Style/Tone": "Professional/Compact", "Notes": "Sounds official and handy"},
    {"Letter": "H", "Term": "How-to", "Style/Tone": "Casual/Tutorial", "Notes": "Friendly and instructive"},
    {"Letter": "I", "Term": "Index", "Style/Tone": "Technical/Formal", "Notes": "More navigational, but could be fun with a twist"},
    {"Letter": "I", "Term": "Instructional", "Style/Tone": "Practical", "Notes": "Strong for educational or training use"},
    {"Letter": "J", "Term": "Journal", "Style/Tone": "Academic/Reflective", "Notes": "More ongoing or observational tone"},
    {"Letter": "K", "Term": "Knowledge Base", "Style/Tone": "Technical/Online", "Notes": "Modern digital/IT context feel"},
    {"Letter": "L", "Term": "Lexicon", "Style/Tone": "Academic/Language-focused", "Notes": "Best for vocab-driven guides"},
    {"Letter": "L", "Term": "Listicle", "Style/Tone": "Playful/Modern", "Notes": "BuzzFeed-y, clicky — fun for informal guides"},
    {"Letter": "M", "Term": "Manual", "Style/Tone": "Practical/Formal", "Notes": "Great for official or tech-style documents"},
    {"Letter": "M", "Term": "Memoir", "Style/Tone": "Reflective/Personal", "Notes": "Looser fit, more story-like, niche usage"},
    {"Letter": "N", "Term": "Notebook", "Style/Tone": "Casual/Creative", "Notes": "Flexible, intimate, even whimsical"},
    {"Letter": "O", "Term": "Overview", "Style/Tone": "Formal/High-level", "Notes": "Neutral and effective"},
    {"Letter": "O", "Term": "Outline", "Style/Tone": "Structured/Formal", "Notes": "Good for scaffolding ideas"},
    {"Letter": "P", "Term": "Primer", "Style/Tone": "Educational/Entry-level", "Notes": "Original term, very effective"},
    {"Letter": "P", "Term": "Playbook", "Style/Tone": "Strategic/Fun", "Notes": "Energetic tone, great for team or biz contexts"},
    {"Letter": "Q", "Term": "Quickstart", "Style/Tone": "Technical/User-friendly", "Notes": "Tech-y, fast onboarding"},
    {"Letter": "Q", "Term": "Quotebook", "Style/Tone": "Creative/Curated", "Notes": "Can be poetic or idea-focused"},
    {"Letter": "R", "Term": "Reference", "Style/Tone": "Formal/Neutral", "Notes": "Classic umbrella term"},
    {"Letter": "R", "Term": "Roadmap", "Style/Tone": "Strategic/Project-based", "Notes": "Good for planning resources"},
    {"Letter": "R", "Term": "Readout", "Style/Tone": "Technical/Data-focused", "Notes": "Often used in meetings or summaries"},
    {"Letter": "S", "Term": "Summary", "Style/Tone": "Concise/Formal", "Notes": "Straightforward and efficient"},
    {"Letter": "S", "Term": "Synopsis", "Style/Tone": "Academic/Creative", "Notes": "Great for condensed narratives or plans"},
    {"Letter": "S", "Term": "Sheet", "Style/Tone": "Casual/Flexible", "Notes": "Good for cheat sheets, single pages"},
    {"Letter": "T", "Term": "Treatise", "Style/Tone": "Formal/Academic", "Notes": "For deep or philosophical coverage"},
    {"Letter": "T", "Term": "Toolkit", "Style/Tone": "Practical/Empowering", "Notes": "Modular, hands-on tone"},
    {"Letter": "T", "Term": "Table", "Style/Tone": "Technical/Visual", "Notes": "Simple, structural approach"},
    {"Letter": "U", "Term": "User Guide", "Style/Tone": "Technical/Practical", "Notes": "Common in software/hardware contexts"},
    {"Letter": "U", "Term": "Update", "Style/Tone": "Casual/Living doc", "Notes": "Good for evolving documents"},
    {"Letter": "V", "Term": "Vault", "Style/Tone": "Metaphorical/Grand", "Notes": "Works metaphorically for deep collections"},
    {"Letter": "V", "Term": "Vade mecum", "Style/Tone": "Archaic/Quirky", "Notes": "Latin for 'go with me' — a pocket guide vibe"},
    {"Letter": "W", "Term": "Workbook", "Style/Tone": "Interactive/Instructional", "Notes": "Good for exercises or activities"},
    {"Letter": "W", "Term": "Whitepaper", "Style/Tone": "Formal/Analytical", "Notes": "Research-heavy or business authority tone"},
    {"Letter": "W", "Term": "Wiki", "Style/Tone": "Collaborative/Modern", "Notes": "Best for evolving, crowd-driven content"},
    {"Letter": "X", "Term": "X-ray", "Style/Tone": "Metaphorical/Deep", "Notes": "Poetic license — could mean a deep dive"},
    {"Letter": "Y", "Term": "Yearbook", "Style/Tone": "Archival/Nostalgic", "Notes": "Works for annual recaps or timelines"},
    {"Letter": "Z", "Term": "Zine", "Style/Tone": "DIY/Cool/Artistic", "Notes": "Great for niche topics or creative spins"}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
file_path = "/mnt/data/Reference_Terms_AtoZ.csv"
df.to_csv(file_path, index=False)

file_path
