📝 Deep-Dive Blog Architect

A high-performance Python CLI tool that transforms a single topic into a visually stunning, data-dense, and SEO-optimized long-form blog post. Designed for researchers, niche site owners, and technical writers who want **luxury-magazine aesthetics** with **Wikipedia-level accuracy**.

## ✨ Features

* **Dual-Stage Generation:** Uses separate AI prompts for high-quality SEO metadata and structured content generation.
* **Visual Hierarchy:** Automatically applies advanced Markdown formatting including:
    * `> Blockquotes` for executive summaries and TL;DRs.
    * `---` Horizontal rules for section separation.
    * 📊 Professional Markdown tables for data comparisons.
    * 🏷️ Emoji-led bullet points for enhanced readability.
* **Automatic SEO:** Generates a front-matter header (Title, Description, Tags, Date) compatible with static site generators like Jekyll, Hugo, or Astro.
* **Smart File Management:** Converts titles into filesystem-friendly "slugs" and calculates an estimated reading time.
* **Local Persistence:** Securely manages your API keys via `.env` files.

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.8+ installed and a **Groq API Key**. You can get one at [console.groq.com](https://console.groq.com/).

### 2. Installation
Clone this repository or copy the script, then install the required dependencies:

```bash
pip install groq python-dotenv
```

### 3. Running the Architect
Launch the script from your terminal:

```bash
python blog_generator.py
```

On the first run, the script will prompt you for your **Groq API Key** and save it locally to a `.env` file.

---

## 🛠️ How it Works

The script follows a rigorous editorial workflow:

1.  **Metadata Extraction:** It first asks the LLM to provide a JSON object containing a catchy title, SEO description, and relevant tags.
2.  **Visual Styling:** It instructs the model to act as a "Senior Editor at Wired/National Geographic," enforcing strict formatting rules.
3.  **Data Density:** It bypasses "fluff" introduction sentences and dives straight into historical context, technical mechanics, and future predictions.
4.  **Export:** The final product is saved as a `.md` (Markdown) file in a `/blogs` directory.

---

## 📂 Project Structure

```text
.
├── blog_generator.py   # The main engine
├── .env                # Your API keys (Generated automatically)
└── blogs/              # Output directory for your generated content
    └── history-of-porsche-911.md
```

---

## 📖 Example Output Structure

The generated files are designed to be viewed in **VS Code**, **Obsidian**, or any Markdown viewer. The structure looks like this:

> **# The Quantum Leap: Understanding Superposition**
> \> **Executive Summary:** An overview of the principles...
> 
> ---
> ## 📜 Historical Context & Origins
> 🏛️ 1920s: The Copenhagen Interpretation...
> 
> ---
> ## ⚙️ Core Mechanics
> | Feature | Classical | Quantum |
> |---------|-----------|---------|
> | State   | 0 or 1    | Superposition |

---

## ⚖️ License
This project is open-source. Use it to build great things!