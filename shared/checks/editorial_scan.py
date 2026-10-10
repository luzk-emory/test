"""Editorial scan for the student-facing course materials (plan/editorial-guide.md, Section 11).

Run from the repository root:  python3 shared/checks/editorial_scan.py [--summary] [path ...]
With no paths it scans every student-facing file (Section 0). Output: one line per match,
"F" (failure: fix or flag) or "R" (review candidate: fix, justify in the PR, or flag), then counts.

Instructor-only content is removed before scanning, keeping line numbers: \\answer{...} blocks and
LaTeX comments (which include the % [RELEASE ...] markers). Case instructor files and
plan/schedule.xlsx are not scanned.
"""
import glob, re, sys
from collections import Counter

STUDENT_FACING = (['meetings/*/slides.tex', 'meetings/*/notes.tex', 'meetings/*/handout-*.tex',
                   'cases/*/student.md', 'syllabus/syllabus.tex', 'shared/notation.tex']
                  + [f'{d}/**/*.{e}' for d in ('labs', 'assignments') for e in ('tex', 'md', 'qmd', 'ipynb')])

# ---------- text extraction ----------
def blank(s):
    return re.sub(r'[^\n]', ' ', s)

def strip_answers(s):
    """Blank every \\answer{...} block (balanced braces), keeping newlines."""
    out, i = [], 0
    for m in re.finditer(r'\\answer\{', s):
        if m.start() < i:
            continue
        j, depth = m.end(), 1
        while j < len(s) and depth:
            depth += {'{': 1, '}': -1}.get(s[j], 0) if s[j - 1] != '\\' else 0
            j += 1
        out.append(s[i:m.start()]); out.append(blank(s[m.start():j])); i = j
    out.append(s[i:])
    return ''.join(out)

def text_of(path):
    s = open(path, encoding='utf-8').read()
    if path.endswith('.tex'):
        s = strip_answers(s)
        s = '\n'.join(re.sub(r'(?<!\\)%.*', '', line) for line in s.split('\n'))
    return s

def kind(path):
    if path.endswith('slides.tex'): return 'slides'
    if path.endswith('notes.tex') and path.startswith('meetings/'): return 'notes'
    if '/handout-' in path: return 'handout'
    if path.startswith('cases/'): return 'case'
    if path.startswith('syllabus/'): return 'syllabus'
    if path.startswith('labs/'): return 'lab'
    if path.startswith('assignments/'): return 'assignment'
    return 'other'

def meeting_of(path):
    m = re.search(r'meetings/m(\d+)/', path)
    return int(m.group(1)) if m else None

# ---------- patterns ----------
I = re.I
BRITISH = re.compile(
    r"\b(\w+is(e|es|ed|ing|ation|ations|er|ers)|\w+ys(e|es|ed|ing)|"
    r"(colo|behavio|favo|hono|labo|neighbo|rumo|humo|harbo|flavo|savo|endeavo|odo|armo)ur(s|ed|ing|able|ite|ites|hood)?|"
    r"(cent|met|lit|theat|fib|calib|spect|meag|somb)re(s|d)?|centring|"
    r"(model|label|travel|cancel|signal|level|fuel|tunnel|counsel|total|channel)l(ed|ing|er|ers)|programmes?|whilst|amongst|per cent|judgements?|fulfil|enrol|enrolment|"
    r"licence|defence|offence|pretence|catalogue|analogue|learnt|spelt|grey|cheques?|storeys?)\b", I)
# -ise / -yse false positives (US words that end the same way)
BRITISH_OK = set("""raise raises raised raising praise praised praising advise advised advising advises adviser
precise concise promise promised promises promising exercise exercises exercised exercising otherwise paradise
premise premises surprise surprises surprised surprising surprisingly noise noises wise rise rises rising arise arises
arising comprise comprises comprised comprising compromise compromises compromised enterprise enterprises franchise
merchandise expertise televise revise revised revising supervise supervised supervising devise devised devising
improvise disguise disguised poise cruise bruise treatise excise incise despise chastise advertise advertised
advertising advertiser advertisers apprise apprised raiser wiser riser anise franchises premised
analysis analyses paralysis catalysis""".split())
STOCK = re.compile(r"\b(delve|delves|delving|dive into|let'?s explore|it'?s worth noting|it is important to note|"
                   r"crucial|pivotal|realm|unlock|unlocks|seamless|seamlessly|harness(es|ed|ing)?|game-changer|"
                   r"key takeaways?|at its core|testament to|in today'?s)\b|data-driven world|not just .{1,40}, but", I)
STOCK_OK = re.compile(r"agent harness|test harness|harness \(", I)
HISTORY = re.compile(r"from the spreadsheet|per the (syllabus|spreadsheet|draft)|as requested|updated to include|"
                     r"has been (moved|replaced|added)|now (covers|includes|uses)|\bnew:|\(v[0-9]|\bversion [0-9]|"
                     r"\bdraft\b|\brevised\b|\\today|this (section|table|slide|document) (explains|summari[sz]es|outlines)|"
                     r"below we outline", I)
OPENER = re.compile(r"\b(the key (insight|point|idea) is|here'?s the thing|this matters because|in short|put simply|"
                    r"the bottom line)\b", I)
FRAGMENT = re.compile(r"\bNot (because|that|just)\b[^.?!]{0,80}[.?!] +(Because|It'?s|That'?s)\b")
XMEET = re.compile(r"(Result|Assumption|Section|[Ee]quation|Definition)s?[ ~]\(?[0-9]+(\.[0-9]+)?\)?[^.]{0,30}Meeting[ ~][0-9]+|"
                   r"Meeting[ ~][0-9]+[^.]{0,30}(Result|Assumption|Section|[Ee]quation|Definition)s?[ ~][0-9]+\.[0-9]+")
PLACEHOLDER = re.compile(r"\\tbd\{|\bTODO\b|\bTBD\b|\bXXX\b|\[insert|lorem ipsum", I)
LABELS = re.compile(r"\bM[0-9]{1,2}\b(?!-R)|\bSession [0-9]|\bClass [0-9]|\bLecture [0-9]+[AB]?\b|\bLab [0-9]+[A-C]\b|"
                    r"\bBlock [0-9]", 0)
CROSS = {
    'slides':     r"\b[Nn]otes\b|[Hh]andout|\bLab [0-9]|\b[Cc]ase part|\bPart M[0-9]|[Ww]orksheet|\bA[1-4]\b|[Aa]ssignment[ ~][0-9]|\bhomework\b",
    'notes':      r"\b[Ss]lides?\b|\bLab [0-9]|\b[Cc]ase part|\bPart M[0-9]|Handout[ ~]H[0-9]|\bA[1-4]\b",
    'handout':    r"\bslides?\b|\bLab [0-9]|Meeting[ ~][0-9]+,? (Result|Section|Assumption)|(Result|Assumption)s?[ ~][0-9]+\.[0-9]+ (of|in) Meeting|technical notes|\bthe notes\b",
    'case':       r"\bslides?\b|technical notes|\bthe notes\b|Handout|\bLab [0-9]|\bframe\b",
    'lab':        r"\bslides?\b|technical notes|\bthe notes\b|Handout|\bcase\b",
    'assignment': r"\bslides?\b|technical notes|\bthe notes\b|Handout|\bcase\b",
}
CITE = re.compile(r"((?:[A-Z][\w'\\\"{}-]+)(?:,? (?:and|&) [A-Z][\w'\\\"{}-]+)*(?: et al\.?\\?)?)(?:\s*~?\(|, )(\d{4})[a-z]?\b")

def norm(name):
    return re.sub(r"[\\\"'{}`^~]", '', name).split(',')[0].split(' and ')[0].split(' et al')[0].strip()

# ---------- checks ----------
def scan(path):
    k, mtg = kind(path), meeting_of(path)
    s = text_of(path); lines = s.split('\n'); hits = []
    def add(level, rule, ln, txt):
        hits.append((level, rule, f"{path}:{ln}", txt.strip()[:140]))
    # frame titles, for slide-specific rules
    frame_at = {}; title = None
    for n, line in enumerate(lines, 1):
        m = re.search(r'\\begin\{frame\}(?:\[[^\]]*\])?\{([^}]*)\}', line)
        if m: title = m.group(1)
        frame_at[n] = title
    for n, line in enumerate(lines, 1):
        if not line.strip(): continue
        tex = path.endswith('.tex')
        # Failures
        if (tex and '---' in line) or (not tex and '\u2014' in line): add('F', 'em-dash', n, line)
        if PLACEHOLDER.search(line) and not re.search(r'\\(re)?newcommand', line):
            add('F', 'placeholder (log, never delete)', n, line)
        # Review candidates
        endash = re.findall(r'[A-Za-z]--[A-Za-z]' if tex else '[A-Za-z]\u2013[A-Za-z]', line)
        if endash: add('R', 'en-dash between words (allowed: joint names, paired terms)', n, line)
        for m in BRITISH.finditer(line):
            if m.group(0).lower() not in BRITISH_OK and not m.group(0).lower().endswith('wise'):
                add('R', f'British spelling: {m.group(0)}', n, line)
        for m in re.finditer(r"\b[\w-]+, [\w-]+(?: [\w-]+)? (?:and|or) [\w-]+", line):
            add('R', 'serial comma?', n, m.group(0)); break
        m = STOCK.search(line)
        if m and not STOCK_OK.search(line): add('R', f'stock phrase: {m.group(0)}', n, line)
        m = HISTORY.search(line)
        if m: add('R', f'production history / title residue: {m.group(0)}', n, line)
        if LABELS.search(line): add('R', 'label form', n, line)
        m = OPENER.search(line)
        if m: add('R', f'substitute device: opener "{m.group(0)}"', n, line)
        if FRAGMENT.search(line): add('R', 'substitute device: dramatic fragment', n, line)
        if XMEET.search(line): add('R', 'cross-meeting number', n, line)
        # Reference-list entries (Chicago "Name. Year.") and reading-list rows are navigation, not dependence.
        if k in CROSS and not re.match(r'\s*\\(node|draw|path|fill|coordinate|documentclass|reading)\b', line) \
                and not re.search(r'\. (19|20)[0-9]{2}[a-z]?\. ', line):
            m = re.search(CROSS[k], line, 0 if k in ('slides', 'notes') else I)
            if m: add('R', f'cross-artifact reference: {m.group(0)}', n, line)
        if mtg is not None:
            for m in re.finditer(r'Meeting[ ~]?(\d+)', line):
                later = int(m.group(1)) > mtg
                course_map = (mtg == 1 and k == 'slides' and (frame_at.get(n) or '').startswith('Where Does the Counterfactual'))
                if later and not course_map: add('R', f'forward reference: {m.group(0)}', n, line)
        if k == 'slides' and re.search(r'\\begin\{frame\}\{[^}]*\?\}', line):
            add('R', 'question title: the frame must answer it', n, line)
    # colons: at most one per paragraph of running prose
    for pm in re.finditer(r'(?:[^\n]+\n?)+', s):
        para = pm.group(0)
        t = re.sub(r'\\begin\{(tabular|tabularx|longtable|equation\*?|align\*?)\}.*?\\end\{\1\}|\$\$.*?\$\$|\\\[.*?\\\]|\$[^$]*\$',
                   ' ', para, flags=re.S)
        t = '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith(('|', '\\node', '\\draw')) and '&' not in l)
        t = re.sub(r'\\(sub)*section\*?\{[^}]*\}|\\paragraph\{[^}]*\}|\\(sub)?title(\[[^]]*\])?\{[^}]*\}|'
                   r'\\begin\{frame\}(\[[^]]*\])?\{[^}]*\}|\\notesheader\{[^}]*\}\{[^}]*\}\{[^}]*\}|^#.*$', ' ', t, flags=re.M)
        t = re.sub(r'\*\*[^*\n]{1,60}:\*\*|\\textbf\{[^}]{1,60}\}:?|\\item\s*(\[[^]]*\])?\s*[^:.\n]{1,40}:|^\s*[-*]\s*[^:.\n]{1,40}:|'
                   r'(Definition|Result|Assumption|Step|Part|Task|Note|Hint|Answer|Key)[^:\n]{0,40}:|\d+:\d+|https?:', ' ', t, flags=re.M)
        if t.count(':') > 1:
            add('R', f'substitute device: {t.count(":")} colons in one paragraph', s[:pm.start()].count('\n') + 1,
                para.strip().split('\n')[0])
    # slides: bold outside tables and box titles, per frame (defined terms + at most one key phrase)
    if k == 'slides':
        for fm in re.finditer(r'\\begin\{frame\}(?:\[[^\]]*\])?\{([^}]*)\}(.*?)\\end\{frame\}', s, re.S):
            body = re.sub(r'\\begin\{(tabular|tabularx|longtable)\}.*?\\end\{\1\}', '', fm.group(2), flags=re.S)
            body = '\n'.join(l for l in body.split('\n') if not re.match(r'\s*\\(node|draw|path)\b', l))
            body = re.sub(r'\\textbf\{(Estimand|Identification|Estimation|Inference|Design|Uncertainty)[^}]*\}', '', body)
            body = re.sub(r'\\Large *\\textbf\{[^}]*\}', '', body)
            body = re.sub(r'\\begin\{block\}\{[^}]*\}', '', body)
            nb = len(re.findall(r'\\textbf\{', body))
            if nb > 2:
                ln = s[:fm.start()].count('\n') + 1
                add('R', f'bold: {nb} outside tables (defined terms + at most one key phrase)', ln, fm.group(1))
    # citations: every in-text citation is in this document's reference list
    if k in ('slides', 'notes', 'handout', 'syllabus', 'case'):
        if k == 'slides':
            refs = ''.join(m.group(0) for m in re.finditer(r'\\begin\{frame\}(?:\[[^\]]*\])?\{References[^}]*\}.*?\\end\{frame\}', s, re.S))
        else:
            refs = ''.join(m.group(0) for m in re.finditer(r'\\begin\{readinglist\}.*?\\end\{readinglist\}|'
                                                            r'\\section\*\{(References|Bonus reading)\}.*?(?=\\section|\\appendix|\\end\{document\})', s, re.S))
        body = s.replace(refs, blank(refs)) if refs else s
        entries = re.split(r'\\reading|\\item|\n\s*\n|\\\\', refs)
        for m in CITE.finditer(body):
            name, year = norm(m.group(1)), m.group(2)
            if name in ('Meeting', 'Section', 'Result', 'Table', 'Figure', 'Lab', 'Week', 'Fall', 'Spring', 'Summer') or \
                    name in ('January February March April May June July August September October November December'.split()):
                continue
            ok = any(name in re.sub(r"[\\\"'{}`^~]", '', e) and year in e for e in entries)
            if not ok:
                add('F', f'citation not in this document\'s references: {name} ({year})', body[:m.start()].count('\n') + 1, m.group(0))
    return hits

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    files = sorted({f for p in (args or STUDENT_FACING) for f in glob.glob(p, recursive=True)})
    allhits = [h for f in files for h in scan(f)]
    if '--summary' not in sys.argv:
        for h in allhits: print(' | '.join(h))
    by_rule = Counter((h[0], re.sub(r':.*', '', h[1])) for h in allhits)
    print(f"\n{len(files)} files; {sum(1 for h in allhits if h[0]=='F')} failures, "
          f"{sum(1 for h in allhits if h[0]=='R')} review candidates")
    for (lvl, rule), c in sorted(by_rule.items()):
        print(f"  {lvl} {c:5d}  {rule}")

if __name__ == '__main__':
    main()
