# Visual and Accessibility Standards

Shared design standards for Office deliverables. Use them as defaults; the user's brand and context take precedence.

## 1. Information hierarchy

- One primary message per slide/page/section.
- A reader should understand the structure from headings alone.
- Put the conclusion first in executive material; supporting detail follows.
- Use progressive disclosure: summary, then evidence, then appendix.
- Avoid decorative elements that compete with the message.

## 2. Typography

- Use a small, consistent type scale (for example, title, heading, body, caption).
- Body text should be comfortably readable at the intended distance; avoid dense walls of text.
- Use sentence case for headings unless the brand requires otherwise.
- Keep line length reasonable; avoid very wide paragraphs in documents and slides.
- Do not use all caps for long text; do not rely on bold/italic alone for meaning.
- Ensure fonts are available on the target machine or embedded where supported; plan for substitution.

## 3. Color and contrast

- Use color with a purpose: emphasis, categories, status. Do not use it as the only signal.
- Check text/background contrast; small text needs stronger contrast than large display text.
- Avoid low-contrast gray-on-gray, yellow-on-white, and thin light text over images.
- Provide sufficient contrast for charts, table headers, focus states, and links.
- Test in grayscale for documents and charts that may be printed.

## 4. Layout and spacing

- Use a consistent grid, margins, and alignment.
- Prefer generous whitespace over crowding; increase spacing before shrinking type.
- Keep related items close; separate unrelated groups.
- Avoid centered body text for long passages; left-align for readability.
- Use native tables for tabular data; do not fake tables with text boxes or tabs.
- Keep headers/footers, page numbers, and confidentiality labels consistent.

## 5. Charts and data visualization

- Choose the chart type based on the question: comparison, trend, distribution, relationship, part-to-whole.
- Start bar/column axes at zero unless there is a defensible reason; label truncation clearly.
- Label axes, units, time period, and source.
- Do not use 3D, shadows, or decorative effects that distort perception.
- Avoid pie charts with many slices; use sorted bars for comparison.
- Show uncertainty/limitations when presenting forecasts or estimates.
- Ensure color-blind-safe palettes and direct labels where possible.
- Keep chart data traceable to the workbook/source.

## 6. Documents

- Use semantic styles for headings, lists, captions, and quotes.
- Create a real table of contents and update it before delivery.
- Use section breaks only for genuine layout changes.
- Repeat table headers across pages; avoid rows splitting awkwardly.
- Keep captions with their figures; avoid orphaned headings.
- Use meaningful link text and alt text.
- Set document language and reading order for accessibility.

## 7. Presentations

- Design for the actual room/screen; 16:9 is a practical default, not a rule.
- Keep one idea per slide; use the title to state the takeaway.
- Use high-quality, relevant imagery; avoid generic stock filler.
- Keep text large enough for the back row; move detail to notes or appendix.
- Use consistent slide masters/layouts; avoid one-off manual formatting.
- Ensure animations support comprehension and have a reduced-motion alternative.
- Review the deck in slide sorter and presentation mode.

## 8. Spreadsheets

- Separate inputs, calculations, and outputs; use consistent color/format conventions.
- Keep formulas short and auditable; use named ranges for key inputs.
- Format numbers consistently; show units and currency codes.
- Freeze panes, set print areas, and protect formula cells where appropriate.
- Use conditional formatting for exceptions, not decoration.
- Avoid hidden rows/columns or white text that conceals data.
- Document assumptions and sources on a visible sheet.

## 9. Accessibility essentials

- Use real headings, lists, and tables, not visual imitations.
- Provide alt text for meaningful images; mark decorative images as decorative.
- Maintain logical reading order in slides, documents, and exported PDFs.
- Ensure keyboard access and visible focus for interactive artifacts.
- Provide captions/transcripts for audio/video.
- Avoid autoplay and unnecessary motion; support reduced motion.
- Do not use color alone to convey status or meaning.
- Use descriptive link text.
- Test with a screen reader and keyboard where possible; automated checks are not sufficient.

## 10. Common visual failure modes

- Text overflow or clipping after font substitution.
- Inconsistent margins/alignment across slides or pages.
- Charts with missing units, truncated axes, or mismatched source data.
- Dense tables that cannot be read at presentation distance.
- Low-contrast text over images or brand colors.
- Decorative icons that add noise without meaning.
- Inconsistent date/number/currency formats.
- Placeholder text or template labels left in the final artifact.
- Reading order that differs from visual order.
- PDF export that loses tags, links, or selectable text.

## 11. Review gates

Before delivery:

1. **Structure review:** hierarchy, navigation, completeness.
2. **Content review:** accuracy, consistency, sources.
3. **Visual review:** alignment, spacing, contrast, overflow.
4. **Accessibility review:** headings, alt text, reading order, keyboard.
5. **Technical review:** file opens, formulas calculate, links work, export preserves layout.
6. **Handoff review:** name, location, version, assumptions, unverified items.
