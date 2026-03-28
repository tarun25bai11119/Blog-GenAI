import os
import re
import json
import math
from pathlib import Path
from dotenv import load_dotenv, set_key
from datetime import datetime

# --- 1. SETUP & ENVIRONMENT ---
current_dir = Path(__file__).parent
env_path = current_dir / ".env"
load_dotenv(dotenv_path=env_path)

def get_api_key():
    """Checks for API key, prompts user and saves to .env if missing."""
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        print("\n🔑 GROQ_API_KEY not found in environment.")
        api_key = input("Please enter your Groq API Key: ").strip()
        if not api_key:
            print("❌ Error: API Key is required to run this script.")
            exit(1)
        
        # Save to .env file for future use
        set_key(str(env_path), "GROQ_API_KEY", api_key)
        print(f"✅ API Key saved locally to: {env_path}")
    
    return api_key

GROQ_API_KEY = get_api_key()

try:
    from groq import Groq
    client = Groq(api_key=GROQ_API_KEY)
except ImportError:
    print("❌ ERROR: Missing dependencies. Run: pip install groq python-dotenv")
    exit(1)

# --- 2. UTILITY FUNCTIONS ---
def slugify(text: str) -> str:
    """Converts titles into filesystem-friendly filenames."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")[:80]

def calculate_read_time(text: str) -> str:
    """Calculates read time based on a technical reading speed."""
    wpm = 200 
    return f"{math.ceil(len(text.split()) / wpm)} min"

# --- 3. THE BLOG ENGINE ---
def generate_deep_dive_blog():
    print("\n" + "═"*60)
    topic = input("📝 Enter the Blog Topic (e.g., Quantum Computing, History of Porsche): ").strip()
    if not topic:
        print("❌ Topic cannot be empty.")
        return

    print(f"\n🚀 Researching and Structuring: {topic}...")

    # -- STEP 1: GENERATE PROFESSIONAL METADATA --
    meta_prompt = f"""
    Generate professional SEO metadata for an encyclopedic deep-dive about: "{topic}".
    Return ONLY a valid JSON object:
    {{
      "title": "Authoritative & Catchy Title (max 70 chars)",
      "description": "A high-density factual summary (max 160 chars)",
      "tags": ["primary-sector", "technology/history", "niche-term"]
    }}
    """
    
    try:
        meta_res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": meta_prompt}],
            temperature=0.7
        )
        raw_json = meta_res.choices[0].message.content.strip().replace("```json", "").replace("```", "")
        meta_data = json.loads(raw_json)
    except Exception as e:
        print(f"⚠️ Metadata error: {e}. Using fallback values.")
        meta_data = {"title": topic, "description": f"A comprehensive guide to {topic}", "tags": ["General"]}

    # -- STEP 2: GENERATE VISUALLY STUNNING CONTENT --
    blog_prompt = f"""
    You are a Senior Editor at a world-class publication like National Geographic or Wired. 
    Write a high-detail, visually organized blog post about: {topic}.

    VISUAL HIERARCHY RULES:
    1. Use '#' for the main title ONLY.
    2. Use '##' for major sections and '###' for subsections.
    3. Use '---' (Horizontal Rules) to separate every '##' section for visual clarity.
    4. Use '>' (Blockquotes) for "TL;DR" summaries and "Pro-Tips".
    5. Use Markdown Tables for any comparisons or technical specifications.
    6. Use Emoji-led bullet points (e.g., 🏛️, ⚙️, 🧪, 📈) for all lists.

    CONTENT STRUCTURE:
    - # {meta_data['title']}
    - > **Executive Summary:** A 3-sentence high-level overview of {topic}.
    - ---
    - ## 📜 Historical Context & Origins
      - Provide specific dates, key figures, and the 'Eureka' moment.
    - ---
    - ## ⚙️ Core Mechanics / How it Works
      - Deep technical dive. 
      - Include a Markdown Table: "Comparison of [Topic] Variants/Models".
    - ---
    - ## 🌍 Societal & Economic Impact
      - Use specific statistics and global trends.
    - ---
    - ## ⚖️ Challenges & Ethical Considerations
      - A balanced view of limitations or controversies.
    - ---
    - ## 🔮 The Future Landscape (2030+)
      - Expert predictions and emerging technologies.

    CRITICAL: No fluff. No "In this blog post..." or "In conclusion...". Start with the data. 
    Make it look like a Wikipedia page designed by a luxury magazine.
    """

    print("⏳ Generating sections with deep data density...")
    content_res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": blog_prompt}],
        temperature=0.4, # Keep it factual and consistent
        max_tokens=4000
    )
    
    content = content_res.choices[0].message.content.strip()
    slug = slugify(meta_data['title'])
    
    # --- 4. SAVING LOGIC ---
    blog_folder = current_dir / "blogs"
    blog_folder.mkdir(exist_ok=True)
    
    # Note: Saved as .md (Markdown) for better visual rendering
    file_path = blog_folder / f"{slug}.md"
    
    with open(file_path, "w", encoding="utf-8") as f:
        # Front-matter for SEO/Static Site Generators
        header = (
            f"---\n"
            f"title: {meta_data['title']}\n"
            f"description: {meta_data['description']}\n"
            f"tags: {', '.join(meta_data['tags'])}\n"
            f"date: {datetime.now().strftime('%Y-%m-%d')}\n"
            f"---\n\n"
        )
        f.write(header + content)

    print(f"\n" + "═"*60)
    print(f"✅ SUCCESS: High-Detail Blog Generated!")
    print(f"📂 Saved to: {file_path.absolute()}")
    print(f"⏱️ Estimated Read Time: {calculate_read_time(content)}")
    print("📝 TIP: Open this file in a Markdown Viewer (VS Code, Obsidian) to see the styling.")
    print("═"*60 + "\n")

if __name__ == "__main__":
    generate_deep_dive_blog()