"""Shared by the PDF, EPUB and clean-export builders: puts the exercises at the end of each chapter and the solutions in one
back-matter section, and replaces the repository links (exercises/chNN-exercises.md) that only work in the source folder."""
import os, re
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
def _shift(text, by):
    out, fence = [], False
    for line in text.split("\n"):
        if line.startswith("```"): fence = not fence
        m = re.match(r"(#{1,6}) ", line)
        if m and not fence: line = "#" * min(6, len(m.group(1)) + by) + line[len(m.group(1)):]
        out.append(line)
    return "\n".join(out)
def _clean(text):
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"`solutions/ch\d+-solutions\.md`", "the Solutions section at the back of the book", text)
    return text.strip()
def link_fix(text):
    """Chapter text: the link to the exercises file becomes a pointer to the section at the chapter's end."""
    text = re.sub(r"\[`exercises/ch\d+-exercises\.md`\]\([^)]*\)", "the *Exercises* section at the end of this chapter", text)
    text = re.sub(r"`solutions/ch\d+-solutions\.md`", "the Solutions section at the back of the book", text)
    text = re.sub(r"`exercises/ch\d+-exercises\.md`", "the *Exercises* section at the end of this chapter", text)
    return text
def with_exercises(n, text):
    text = link_fix(text)
    p = os.path.join(root, "exercises", f"ch{n:02d}-exercises.md")
    if not os.path.exists(p): return text
    ex = _clean(open(p, encoding="utf-8").read())
    ex = re.sub(r"\A# [^\n]*\n", "", ex).strip()          # drop the file's own title
    ex = re.sub(r"solutions/ch\d+-solutions\.md", "the Solutions section", ex)
    return text.rstrip() + "\n\n## Exercises\n\n" + _shift(ex, 1) + "\n"
def solutions_text(chapters):
    """chapters: list of (number, title). Returns one Markdown document."""
    parts = ["# Solutions to the Exercises\n\nAttempt each exercise before you read its answer. Chapters are listed in book order."]
    for n, title in chapters:
        p = os.path.join(root, "solutions", f"ch{n:02d}-solutions.md")
        if not os.path.exists(p): continue
        body = _clean(open(p, encoding="utf-8").read())
        body = re.sub(r"\A# [^\n]*\n", "", body).strip()
        parts.append(f"## Chapter {n} — {title}\n\n" + _shift(body, 1))
    return "\n\n".join(parts) + "\n"
