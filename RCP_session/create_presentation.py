#!/usr/bin/env python3
"""Generate Nexus AI & PromptLint RCP Session PowerPoint."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# --- Colour palette ---
BG_DARK = RGBColor(0x0D, 0x1B, 0x2A)
BG_MID = RGBColor(0x1B, 0x2A, 0x41)
ACCENT_BLUE = RGBColor(0x00, 0x96, 0xD6)
ACCENT_GREEN = RGBColor(0x00, 0xC9, 0x7B)
ACCENT_RED = RGBColor(0xE8, 0x4D, 0x4D)
ACCENT_AMBER = RGBColor(0xFF, 0xB7, 0x4D)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xCC, 0xCC, 0xCC)
MID_GRAY = RGBColor(0x99, 0x99, 0x99)
CODE_BG = RGBColor(0x14, 0x1E, 0x30)
DB_BLUE = RGBColor(0x00, 0x18, 0xA8)


def set_slide_bg(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_textbox(slide, left, top, width, height, text, font_size=18,
                color=WHITE, bold=False, alignment=PP_ALIGN.LEFT,
                font_name="Calibri"):
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top),
                                      Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = font_name
    p.alignment = alignment
    return txBox


def add_multi_text(slide, left, top, width, height, lines,
                   font_name="Calibri"):
    """lines = list of (text, size, color, bold, alignment)"""
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top),
                                      Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, (text, size, color, bold, align) in enumerate(lines):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = text
        p.font.size = Pt(size)
        p.font.color.rgb = color
        p.font.bold = bold
        p.font.name = font_name
        p.alignment = align
        p.space_after = Pt(4)
    return txBox


def add_code_block(slide, left, top, width, height, code_text, font_size=13):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(left), Inches(top), Inches(width), Inches(height)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = CODE_BG
    shape.line.fill.background()
    shape.shadow.inherit = False

    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.2)
    tf.margin_bottom = Inches(0.2)

    for i, line in enumerate(code_text.split("\n")):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = line
        p.font.size = Pt(font_size)
        p.font.color.rgb = ACCENT_GREEN
        p.font.name = "Consolas"
        p.font.bold = False
        p.space_after = Pt(1)
        p.space_before = Pt(1)
    return shape


def add_bullet_list(slide, left, top, width, height, items,
                    font_size=16, color=LIGHT_GRAY, bullet_color=ACCENT_BLUE):
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top),
                                      Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = f"▸  {item}"
        p.font.size = Pt(font_size)
        p.font.color.rgb = color
        p.font.name = "Calibri"
        p.space_after = Pt(6)
    return txBox


def add_accent_line(slide, left, top, width, color=ACCENT_BLUE):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(left), Inches(top), Inches(width), Inches(0.04)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


def add_section_badge(slide, left, top, text, color=ACCENT_BLUE):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(left), Inches(top), Inches(2.2), Inches(0.4)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    tf = shape.text_frame
    tf.margin_left = Inches(0.1)
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(11)
    p.font.color.rgb = WHITE
    p.font.bold = True
    p.font.name = "Calibri"
    p.alignment = PP_ALIGN.CENTER
    return shape


# ============================================================
# SLIDE 1 — Title
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
set_slide_bg(slide, BG_DARK)

add_accent_line(slide, 1.5, 2.3, 10.3, ACCENT_BLUE)

add_textbox(slide, 1.5, 2.5, 10.3, 1.2,
            "Nexus AI & Studio, and PromptLint", 44, WHITE, True, PP_ALIGN.LEFT)
add_textbox(slide, 1.5, 3.5, 10.3, 0.6,
            "AI Engineering at dbCLM", 24, ACCENT_BLUE, False, PP_ALIGN.LEFT)
add_textbox(slide, 1.5, 4.15, 10.3, 0.5,
            "Java & Kotlin Native, Spring Boot Powered", 18, ACCENT_AMBER,
            False, PP_ALIGN.LEFT)

add_textbox(slide, 1.5, 4.8, 10.3, 0.4,
            "Akshay Dipta, Senior Engineer, CLM Tech", 18, LIGHT_GRAY,
            False, PP_ALIGN.LEFT)
add_textbox(slide, 1.5, 5.3, 10.3, 0.4,
            "RCP Engineering Session  |  Deutsche Bank", 14, MID_GRAY,
            False, PP_ALIGN.LEFT)


# ============================================================
# SLIDE 2 — The Problem + Vision
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 1.0, 11.7, 0.6,
            "The Problem + Vision", 32, WHITE, True)
add_accent_line(slide, 0.8, 1.55, 4, ACCENT_RED)

# Problem side
add_textbox(slide, 0.8, 1.8, 5.5, 0.4,
            "THE PROBLEM", 14, ACCENT_RED, True)
add_bullet_list(slide, 0.8, 2.2, 5.5, 3.5, [
    "Building a new AI agent took 18 to 24 hours of boilerplate",
    "Every team reimplementing auth, retry, model config from scratch",
    "No prompt quality gates, bad prompts reached production silently",
    "No observability, no audit trail of what the AI decided and why",
    "No control over LLM integration, locked into library defaults",
], 15, LIGHT_GRAY)

# Vision side
add_accent_line(slide, 7.0, 1.55, 4, ACCENT_GREEN)
add_textbox(slide, 7.0, 1.8, 5.5, 0.4,
            "THE VISION", 14, ACCENT_GREEN, True)
add_bullet_list(slide, 7.0, 2.2, 5.5, 3.5, [
    "What if a new agent took 1 hour, not 24?",
    "What if a 12-agent pipeline was expressible in 20 lines of code?",
    "What if observability, auth, and DB-driven prompts were built in by default?",
    "What if prompt quality was enforced in CI, like code linting?",
    "What if you could see your agents execute live, click any node, inspect state?",
], 15, LIGHT_GRAY)


# ============================================================
# SLIDE 3 — What's Inside Nexus AI
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 0.6, 11.7, 0.6,
            "What's Inside Nexus AI", 30, WHITE, True)
add_accent_line(slide, 0.8, 1.15, 5, ACCENT_BLUE)

# 3-column x 3-row grid
col_headers = [
    ("Core Engine", ACCENT_GREEN),
    ("Listeners & Observability", ACCENT_AMBER),
    ("Integration", ACCENT_BLUE),
]

grid = [
    [
        ("Custom Chat Models", "Full control beyond LangChain4j defaults"),
        ("AgentExecution Listener", "Logs every LLM input/output to DB"),
        ("Bank Authentication", "Custom WIF → Azure → JWT chain"),
    ],
    [
        ("Custom Serialization", "Supports framework-specific object types"),
        ("Observability Listener", "Correlation IDs for Splunk & Langfuse"),
        ("Rate Limiter", "Custom per-model rate limiting"),
    ],
    [
        ("Auto Checkpoints", "Persists graph state to DB automatically"),
        ("Token Usage Listener", "Tracks token consumption per agent"),
        ("Table Access API", "Methods to query framework tables"),
    ],
]

col_x = [0.8, 4.8, 8.8]
col_w = 3.7
cell_h = 1.1

# Column headers
for i, (header, clr) in enumerate(col_headers):
    add_textbox(slide, col_x[i], 1.5, col_w, 0.4, header, 16, clr, True,
                PP_ALIGN.CENTER)

# Grid cells
for row_idx, row in enumerate(grid):
    y = 2.1 + row_idx * (cell_h + 0.2)
    for col_idx, (title, desc) in enumerate(row):
        clr = col_headers[col_idx][1]
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(col_x[col_idx]), Inches(y),
            Inches(col_w), Inches(cell_h)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = BG_MID
        shape.line.color.rgb = clr
        shape.line.width = Pt(1.5)
        tf = shape.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.2)
        tf.margin_top = Inches(0.15)
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(15)
        p.font.color.rgb = clr
        p.font.bold = True
        p.font.name = "Calibri"
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(12)
        p2.font.color.rgb = LIGHT_GRAY
        p2.font.name = "Calibri"
        p2.space_before = Pt(6)


# ============================================================
# SLIDE 4 — Two-Tier Architecture
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 1.0, 11.7, 0.6,
            "Two-Tier Architecture", 32, WHITE, True)
add_accent_line(slide, 0.8, 1.55, 5, ACCENT_BLUE)

# Outer Nexus AI box (full width, services inside)
outer = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.8), Inches(1.9), Inches(11.7), Inches(5.2)
)
outer.fill.solid()
outer.fill.fore_color.rgb = RGBColor(0x12, 0x22, 0x38)
outer.line.color.rgb = ACCENT_BLUE
outer.line.width = Pt(2)
add_textbox(slide, 1.1, 2.0, 3, 0.4, "NEXUS AI", 16, ACCENT_BLUE, True)

# Tier 1 box
t1 = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(1.2), Inches(2.5), Inches(7.5), Inches(1.8)
)
t1.fill.solid()
t1.fill.fore_color.rgb = RGBColor(0x1A, 0x30, 0x50)
t1.line.color.rgb = RGBColor(0x40, 0x70, 0xA0)
t1.line.width = Pt(1)

add_textbox(slide, 1.5, 2.55, 5, 0.35,
            "TIER 1, Workflow Orchestration  (LangGraph4j)", 14,
            ACCENT_BLUE, True)

# Tier 1 nodes
for i, (label, clr) in enumerate([
    ("Non-AI\nNode", LIGHT_GRAY),
    ("AI Node\n(Bridge → T2)", ACCENT_GREEN),
    ("Non-AI\nNode", LIGHT_GRAY),
]):
    x = 1.6 + i * 2.3
    n = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x), Inches(3.05), Inches(1.7), Inches(0.8)
    )
    n.fill.solid()
    n.fill.fore_color.rgb = BG_MID
    n.line.color.rgb = clr
    n.line.width = Pt(1)
    tf = n.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = label
    p.font.size = Pt(11)
    p.font.color.rgb = clr
    p.font.bold = True
    p.font.name = "Calibri"
    p.alignment = PP_ALIGN.CENTER

# Arrows between T1 nodes
for i in range(2):
    x = 3.3 + i * 2.3
    add_textbox(slide, x, 3.2, 0.6, 0.5, "→", 24, MID_GRAY, True,
                PP_ALIGN.CENTER)

add_textbox(slide, 1.5, 3.95, 7.0, 0.3,
            "Checkpoints  |  Graph State  |  Conditional Edges", 11,
            MID_GRAY, False)

# Tier 2 box
t2 = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(1.2), Inches(4.5), Inches(7.5), Inches(1.3)
)
t2.fill.solid()
t2.fill.fore_color.rgb = RGBColor(0x1A, 0x30, 0x50)
t2.line.color.rgb = RGBColor(0x40, 0x70, 0xA0)
t2.line.width = Pt(1)

add_textbox(slide, 1.5, 4.55, 5, 0.35,
            "TIER 2, Agent Pipeline  (LangChain4j)", 14,
            ACCENT_GREEN, True)

add_textbox(slide, 1.5, 4.95, 7.0, 0.4,
            "AgentFactory  |  AgentSpec  |  AgenticScope  |  "
            "Tools  |  UntypedAgent", 12, LIGHT_GRAY, False)
add_textbox(slide, 1.5, 5.3, 7.0, 0.3,
            "sequence()  |  parallel()  |  loopUntil()", 12,
            ACCENT_AMBER, True)

# Bottom bar inside Nexus AI
add_textbox(slide, 1.1, 6.2, 8.0, 0.3,
            "Enterprise Auth  |  DB-Driven Prompts  |  Observability",
            12, ACCENT_BLUE, True, PP_ALIGN.CENTER)

# --- Integrated Services (right column, inside Nexus AI box) ---

# Arrow: Tier 1 → DB
add_textbox(slide, 8.65, 2.95, 0.7, 0.5, "→", 22, ACCENT_AMBER, True,
            PP_ALIGN.CENTER)

# Database box (inside, right of Tier 1)
db_box = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(9.3), Inches(2.5), Inches(2.8), Inches(1.3)
)
db_box.fill.solid()
db_box.fill.fore_color.rgb = RGBColor(0x1A, 0x30, 0x50)
db_box.line.color.rgb = ACCENT_AMBER
db_box.line.width = Pt(2)
tf = db_box.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.15)
tf.margin_top = Inches(0.08)
p = tf.paragraphs[0]
p.text = "DATABASE"
p.font.size = Pt(13)
p.font.color.rgb = ACCENT_AMBER
p.font.bold = True
p.font.name = "Calibri"
p.alignment = PP_ALIGN.CENTER
p2 = tf.add_paragraph()
p2.text = "Checkpoints (T1)\nPrompts (T2)\nExecution Records"
p2.font.size = Pt(10)
p2.font.color.rgb = LIGHT_GRAY
p2.font.name = "Calibri"
p2.alignment = PP_ALIGN.CENTER
p2.space_before = Pt(3)

# Arrow: Tier 2 → LLM
add_textbox(slide, 8.65, 4.65, 0.7, 0.5, "→", 22, ACCENT_GREEN, True,
            PP_ALIGN.CENTER)

# LLM / Gemini box (inside, right of Tier 2)
llm_box = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(9.3), Inches(4.1), Inches(2.8), Inches(1.2)
)
llm_box.fill.solid()
llm_box.fill.fore_color.rgb = RGBColor(0x1A, 0x30, 0x50)
llm_box.line.color.rgb = ACCENT_GREEN
llm_box.line.width = Pt(2)
tf = llm_box.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.15)
tf.margin_top = Inches(0.08)
p = tf.paragraphs[0]
p.text = "LLM, GEMINI"
p.font.size = Pt(13)
p.font.color.rgb = ACCENT_GREEN
p.font.bold = True
p.font.name = "Calibri"
p.alignment = PP_ALIGN.CENTER
p2 = tf.add_paragraph()
p2.text = "Model Calls (via T2)\nResponses & Streaming"
p2.font.size = Pt(10)
p2.font.color.rgb = LIGHT_GRAY
p2.font.name = "Calibri"
p2.alignment = PP_ALIGN.CENTER
p2.space_before = Pt(3)

# Azure AD box (inside, bottom right)
azure_box = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(9.3), Inches(5.6), Inches(2.8), Inches(1.1)
)
azure_box.fill.solid()
azure_box.fill.fore_color.rgb = RGBColor(0x1A, 0x30, 0x50)
azure_box.line.color.rgb = RGBColor(0x00, 0x78, 0xD4)
azure_box.line.width = Pt(2)
tf = azure_box.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.15)
tf.margin_top = Inches(0.08)
p = tf.paragraphs[0]
p.text = "AZURE AD"
p.font.size = Pt(13)
p.font.color.rgb = RGBColor(0x00, 0x78, 0xD4)
p.font.bold = True
p.font.name = "Calibri"
p.alignment = PP_ALIGN.CENTER
p2 = tf.add_paragraph()
p2.text = "WIF Authentication\nToken Management"
p2.font.size = Pt(10)
p2.font.color.rgb = LIGHT_GRAY
p2.font.name = "Calibri"
p2.alignment = PP_ALIGN.CENTER
p2.space_before = Pt(3)


# ============================================================
# SLIDE 4 — AgentSpec
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 1.0, 11.7, 0.6,
            "AgentSpec, Declarative Agent Definition", 32, WHITE, True)
add_accent_line(slide, 0.8, 1.55, 5, ACCENT_GREEN)

code = '''AgentSpec OWNERSHIP_ORG_CHART_AGENT = AgentSpec.of(
        OWNERSHIP_ORGANISATION_CHART.getValue(),
        OWNERSHIP_ORGANISATION_CHART.getDescription())
    .inputs(Map.of(
        "deduplicatedEntities", OwnershipResult.class,
        "clientEntityName",     String.class))
    .output("organisationChart", String.class)
    .cacheSystemInstruction(true)
    .inputGuardrails(inputValidatorGuardrail)
    .outputGuardrails(jsonSchemaValidator)
    .contentRetriever(ragContentRetriever)
    .tools(batchAccumulatorTool)
    .async(false)
    .cacheTools(true)
    .promptVersion(4)
    .build();'''

add_code_block(slide, 0.8, 1.9, 7.0, 4.5, code, 13)

# Annotations on the right
annotations = [
    ("inputs", "Typed bindings from graph state with class mapping"),
    ("output", "Typed output key, available to downstream agents"),
    ("cacheSystemInstruction", "Cache system prompt across calls"),
    ("inputGuardrails", "Team-provided validation before LLM call"),
    ("outputGuardrails", "Team-provided validation after LLM response"),
    ("contentRetriever", "RAG retriever, injects context from documents"),
    ("tools", "LangChain4j-compatible tool bindings"),
    ("async", "Sync or async execution mode"),
    ("promptVersion", "Versioned prompts loaded from database"),
]
y = 2.0
for label, desc in annotations:
    add_textbox(slide, 8.2, y, 4.3, 0.25, label, 12, ACCENT_GREEN, True)
    add_textbox(slide, 8.2, y + 0.25, 4.3, 0.3, desc, 11, LIGHT_GRAY)
    y += 0.55


# ============================================================
# SLIDE 5 — Spring Boot Agent Configuration
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 0.6, 11.7, 0.6,
            "Spring Boot Agent Configuration", 32, WHITE, True)
add_accent_line(slide, 0.8, 1.15, 5, ACCENT_GREEN)

# Left side — Simple sequence config
add_textbox(slide, 0.8, 1.4, 5.5, 0.35,
            "Simple Sequence", 16, ACCENT_BLUE, True)

simple_code = '''@Bean
public OwnershipOrganisationChartAgent
        ownershipOrganisationChartAgent() {

    return agentFactory.sequence(
        OwnershipOrganisationChartAgent.class,
        "organisationChart",
        specs.ownershipOrganisationChartAgent());
}'''

add_code_block(slide, 0.8, 1.8, 5.8, 5.56, simple_code, 12)

# Right side — Critic loop config
add_textbox(slide, 6.9, 1.4, 5.8, 0.35,
            "With Critic Loop", 16, ACCENT_AMBER, True)

critic_code = '''@Bean
public OwnershipOrganisationChartAgent
        ownershipOrgChartAgentWithCritic() {

    UntypedAgent initScope = AgenticServices
        .sequenceBuilder()
        .output(scope -> {
            scope.writeState("criticFeedback", "");
            scope.writeState("extractedRecords", "");
            return "";
        }).build();

    UntypedAgent extractor = agentFactory.criticLoop(
        scope -> scoreParser.parseCriticScore(
            scope.readState("criticFeedback")),
        buildWithBatchTool(
            specs.ownershipOrgChartAgent()),
        specs.ownershipExtractionCriticAgent());

    return agentFactory.sequence(
        OwnershipOrganisationChartAgent.class,
        "extractedRecords",
        initScope, extractor);
}'''

add_code_block(slide, 6.9, 1.8, 5.8, 5.56, critic_code, 12)


# ============================================================
# SLIDE 6 — Workflow Graph Definition
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 1.0, 11.7, 0.6,
            "Tier 1, Workflow Graph Definition", 32, WHITE, True)
add_accent_line(slide, 0.8, 1.55, 5, ACCENT_BLUE)

code = '''StateGraph<CsmState> workflow = new StateGraph<>(CsmState::new);

workflow.addNode("document_aggregation",            documentAggregatorNode);
workflow.addNode("document_classification_node",    documentClassificationNode);
workflow.addNode("named_entity_extraction_node",    namedEntityExtractionNode);
workflow.addNode("csm_classification",              csmClassificationNode);
workflow.addNode("csm_comparison",                  csmComparisonNode);
workflow.addNode("de_duplication_node",             deDuplicationNode);
workflow.addNode("person_name_normalization_node",  personNameNormalizationNode);
workflow.addNode("csm_persistence",                 csmPersistenceNode);
workflow.addNode("auto_answer_trigger",             autoAnswerTriggeringNode);

workflow.addEdge(START, "document_aggregation");
workflow.addEdge("document_aggregation", "document_classification_node");
workflow.addConditionalEdges("document_classification_node",
    documentAggregationEdge,
    Map.of("named_entity_extraction_node", "named_entity_extraction_node", END, END));
workflow.addEdge("named_entity_extraction_node", "person_name_normalization_node");
workflow.addEdge("person_name_normalization_node", "de_duplication_node");
workflow.addEdge("de_duplication_node", "csm_classification");
workflow.addEdge("csm_classification", "csm_comparison");
workflow.addConditionalEdges("csm_comparison", csmPersistenceTriggeringEdge,
    Map.of("csm_persistence", "csm_persistence", END, END));
workflow.addEdge("csm_persistence", "auto_answer_trigger");
workflow.addEdge("auto_answer_trigger", END);

return workflow.compile(
    CompileConfig.builder().checkpointSaver(checkpointSaver).build());'''

add_code_block(slide, 0.8, 1.8, 11.7, 5.2, code, 12)


# ============================================================
# SLIDE 7 — Entity Relationship Diagram (PlantUML image)
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 0.6, 11.7, 0.6,
            "Database Schema, Entity Relationships", 30, WHITE, True)
add_accent_line(slide, 0.8, 1.15, 5, ACCENT_AMBER)

add_textbox(slide, 0.8, 1.3, 11.7, 0.4,
            "Four tables power the framework: config, execution, observability, and state persistence.",
            13, LIGHT_GRAY)

import os
er_img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "er_diagram.png")
slide.shapes.add_picture(er_img_path, Inches(3.2), Inches(1.8), height=Inches(5.4))


# ============================================================
# SLIDE 8 — DB-Driven Configuration: Prompt Table
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 0.6, 11.7, 0.6,
            "DB-Driven Configuration, AI_CHAT_PROMPT", 30, WHITE, True)
add_accent_line(slide, 0.8, 1.15, 5, ACCENT_AMBER)

# Subtitle explanation
add_textbox(slide, 0.8, 1.3, 11.7, 0.4,
            "All agent configs defined here. Loaded and validated at application start. "
            "Missing input variables throw exceptions before first request.",
            13, LIGHT_GRAY)

# --- Column groups as boxes ---

# Group 1: Identity (top-left)
g1 = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.8), Inches(1.9), Inches(3.7), Inches(2.4)
)
g1.fill.solid()
g1.fill.fore_color.rgb = BG_MID
g1.line.color.rgb = ACCENT_BLUE
g1.line.width = Pt(1.5)
tf = g1.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.2)
tf.margin_top = Inches(0.1)
p = tf.paragraphs[0]
p.text = "IDENTITY"
p.font.size = Pt(12)
p.font.color.rgb = ACCENT_BLUE
p.font.bold = True
p.font.name = "Calibri"

id_cols = [
    ("CW_PROMPT_CODE", "VARCHAR2(50)", "Agent identifier"),
    ("PROMPT_VERSION", "NUMBER", "Version number"),
    ("CW_STEP_CODE", "VARCHAR2(50)", "Workflow step ref"),
    ("FUNCTION_CODE", "VARCHAR2(150)", "Function/workflow ref"),
    ("DEFAULT_PROMPT_VERSION", "VARCHAR2(1)", "Active version flag"),
]
for col, dtype, desc in id_cols:
    p2 = tf.add_paragraph()
    p2.text = col
    p2.font.size = Pt(10)
    p2.font.color.rgb = ACCENT_GREEN
    p2.font.bold = True
    p2.font.name = "Consolas"
    p2.space_before = Pt(3)
    p3 = tf.add_paragraph()
    p3.text = f"  {desc}"
    p3.font.size = Pt(9)
    p3.font.color.rgb = LIGHT_GRAY
    p3.font.name = "Calibri"

# Group 2: Model Config (top-right)
g2 = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(4.7), Inches(1.9), Inches(3.7), Inches(2.4)
)
g2.fill.solid()
g2.fill.fore_color.rgb = BG_MID
g2.line.color.rgb = ACCENT_GREEN
g2.line.width = Pt(1.5)
tf = g2.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.2)
tf.margin_top = Inches(0.1)
p = tf.paragraphs[0]
p.text = "MODEL CONFIGURATION"
p.font.size = Pt(12)
p.font.color.rgb = ACCENT_GREEN
p.font.bold = True
p.font.name = "Calibri"

model_cols = [
    ("CW_MODEL_NAME", "Model (e.g. gemini-1.5-pro)"),
    ("CW_TEMPERATURE", "Temperature"),
    ("CW_TOP_P / CW_TOP_K", "Sampling parameters"),
    ("CW_SEED", "Seed for reproducibility"),
    ("CW_MAX_OUTPUT_TOKENS", "Token limit"),
    ("CW_CALL_TIMEOUT_MILLIS", "Call timeout"),
    ("CW_THINKING_BUDGET", "Thinking budget"),
]
for col, desc in model_cols:
    p2 = tf.add_paragraph()
    p2.text = col
    p2.font.size = Pt(10)
    p2.font.color.rgb = ACCENT_AMBER
    p2.font.bold = True
    p2.font.name = "Consolas"
    p2.space_before = Pt(2)
    p3 = tf.add_paragraph()
    p3.text = f"  {desc}"
    p3.font.size = Pt(9)
    p3.font.color.rgb = LIGHT_GRAY
    p3.font.name = "Calibri"

# Group 3: Prompt Content (bottom-left)
g3 = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(8.6), Inches(1.9), Inches(3.9), Inches(2.4)
)
g3.fill.solid()
g3.fill.fore_color.rgb = BG_MID
g3.line.color.rgb = ACCENT_AMBER
g3.line.width = Pt(1.5)
tf = g3.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.2)
tf.margin_top = Inches(0.1)
p = tf.paragraphs[0]
p.text = "PROMPT & BEHAVIOUR"
p.font.size = Pt(12)
p.font.color.rgb = ACCENT_AMBER
p.font.bold = True
p.font.name = "Calibri"

prompt_cols = [
    ("CW_PROMPT_TEXT", "CLOB", "User prompt template"),
    ("SYSTEM_INSTRUCTION", "CLOB", "System instruction"),
    ("CW_PROMPT_LANG", "VARCHAR2(10)", "Prompt language"),
    ("CW_RESPONSE_SCHEMA", "CLOB", "Expected response schema"),
    ("CRITIC_LOOPS", "NUMBER", "Critic loop iterations"),
]
for col, dtype, desc in prompt_cols:
    p2 = tf.add_paragraph()
    p2.text = col
    p2.font.size = Pt(10)
    p2.font.color.rgb = WHITE
    p2.font.bold = True
    p2.font.name = "Consolas"
    p2.space_before = Pt(3)
    p3 = tf.add_paragraph()
    p3.text = f"  {desc}"
    p3.font.size = Pt(9)
    p3.font.color.rgb = LIGHT_GRAY
    p3.font.name = "Calibri"

# Group 4: Audit (bottom row)
g4 = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.8), Inches(4.5), Inches(11.7), Inches(1.0)
)
g4.fill.solid()
g4.fill.fore_color.rgb = BG_MID
g4.line.color.rgb = MID_GRAY
g4.line.width = Pt(1)
tf = g4.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.2)
tf.margin_top = Inches(0.1)
p = tf.paragraphs[0]
p.text = ("AUDIT    CREATED_BY  |  CREATED_DATE  |  LAST_UPDATED_BY  |  "
          "LAST_UPDATE_DATE")
p.font.size = Pt(11)
p.font.color.rgb = MID_GRAY
p.font.bold = False
p.font.name = "Consolas"
p2 = tf.add_paragraph()
p2.text = "Primary Key: (CW_PROMPT_CODE, PROMPT_VERSION)    FK → AI_CHAT_WORKFLOW, AI_CHAT_WORKFLOW_STEP"
p2.font.size = Pt(10)
p2.font.color.rgb = ACCENT_BLUE
p2.font.name = "Consolas"
p2.space_before = Pt(4)

# Bottom note
add_textbox(slide, 0.8, 5.7, 11.7, 0.5,
            "Change a prompt, model, or temperature without redeployment. "
            "Next execution picks up the new config. Full version history via PROMPT_VERSION.",
            13, ACCENT_AMBER)


# ============================================================
# SLIDE 8 — Workflow Run Table
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 0.6, 11.7, 0.6,
            "Workflow Metadata, AI_CHAT_WORKFLOW_RUN", 30, WHITE, True)
add_accent_line(slide, 0.8, 1.15, 5, ACCENT_AMBER)

add_textbox(slide, 0.8, 1.3, 11.7, 0.4,
            "Parent table for every workflow execution. "
            "CW_RUN_ID links to agent executions and checkpoints tables.",
            13, LIGHT_GRAY)

# Column table — header row
col_headers = ["COLUMN", "TYPE", "DESCRIPTION"]
col_widths = [3.8, 2.2, 5.5]
col_starts = [0.8, 4.6, 6.8]

for col, x, w in zip(col_headers, col_starts, col_widths):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(x), Inches(1.85), Inches(w), Inches(0.38)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(0x1A, 0x30, 0x50)
    shape.line.color.rgb = RGBColor(0x30, 0x50, 0x70)
    shape.line.width = Pt(0.5)
    tf = shape.text_frame
    tf.margin_left = Inches(0.1)
    p = tf.paragraphs[0]
    p.text = col
    p.font.size = Pt(11)
    p.font.color.rgb = ACCENT_BLUE
    p.font.bold = True
    p.font.name = "Consolas"

# Data rows
rows = [
    ("CW_RUN_ID", "NUMBER", "Unique run ID, links to agent executions and checkpoints"),
    ("FUNCTION_CODE", "VARCHAR2(50)", "Workflow/function identifier"),
    ("CW_RUN_STATUS", "VARCHAR2(50)", "Status: RUNNING → FINISHED / FAILED"),
    ("RUN_COMMENT", "VARCHAR2(256)", "Execution comment or description"),
    ("PROFILE_VERSION_ID", "NUMBER", "Client profile version"),
    ("KYC_ID", "NUMBER", "Client KYC identifier, which client this run is for"),
    ("IS_STBL_KYC", "CHAR(1)", "Stable KYC flag"),
    ("CREATED_BY", "VARCHAR2(128)", "Who triggered the run"),
    ("CREATE_DATE", "TIMESTAMP(6)", "When the run started"),
    ("LAST_UPDATED_BY", "VARCHAR2(128)", "Last status updater"),
    ("LAST_UPDATE_DATE", "TIMESTAMP(6)", "Last status change timestamp"),
]

y = 2.23
for col_name, dtype, desc in rows:
    # Highlight key rows
    if col_name == "CW_RUN_ID":
        name_clr = ACCENT_AMBER
    elif col_name in ("KYC_ID", "CW_RUN_STATUS"):
        name_clr = ACCENT_GREEN
    else:
        name_clr = WHITE

    for val, x, w, clr in [
        (col_name, 0.8, 3.8, name_clr),
        (dtype, 4.6, 2.2, MID_GRAY),
        (desc, 6.8, 5.5, LIGHT_GRAY),
    ]:
        shape = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(x), Inches(y), Inches(w), Inches(0.33)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = CODE_BG
        shape.line.color.rgb = RGBColor(0x25, 0x35, 0x50)
        shape.line.width = Pt(0.3)
        tf = shape.text_frame
        tf.margin_left = Inches(0.1)
        tf.margin_top = Inches(0.02)
        p = tf.paragraphs[0]
        p.text = val
        p.font.size = Pt(10)
        p.font.color.rgb = clr
        p.font.name = "Consolas" if x < 6.8 else "Calibri"
        if x == 0.8:
            p.font.bold = True
    y += 0.33

# Relationship diagram at bottom
shape = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.8), Inches(6.0), Inches(11.7), Inches(1.0)
)
shape.fill.solid()
shape.fill.fore_color.rgb = BG_MID
shape.line.color.rgb = ACCENT_BLUE
shape.line.width = Pt(1.5)
tf = shape.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.3)
tf.margin_top = Inches(0.1)
p = tf.paragraphs[0]
p.text = "AI_CHAT_WORKFLOW_RUN.CW_RUN_ID  →  NEXUS_AI_AGENT_EXECUTIONS.RUN_ID  |  CHECKPOINTS.RUN_ID"
p.font.size = Pt(12)
p.font.color.rgb = ACCENT_AMBER
p.font.bold = True
p.font.name = "Consolas"
p.alignment = PP_ALIGN.CENTER
p2 = tf.add_paragraph()
p2.text = "One workflow run → many agent executions + many checkpoints. Full traceability from client to every LLM call."
p2.font.size = Pt(12)
p2.font.color.rgb = LIGHT_GRAY
p2.font.name = "Calibri"
p2.alignment = PP_ALIGN.CENTER
p2.space_before = Pt(4)


# ============================================================
# SLIDE 9 — Agent Execution Table
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 0.6, 11.7, 0.6,
            "Automatic Observability, NEXUS_AI_AGENT_EXECUTIONS", 28, WHITE, True)
add_accent_line(slide, 0.8, 1.15, 5, ACCENT_AMBER)

add_textbox(slide, 0.8, 1.3, 11.7, 0.4,
            "Every agent execution automatically persisted by the framework. "
            "Zero developer code required.",
            13, LIGHT_GRAY)

# Group 1: Identity & Execution (top-left)
g1 = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.8), Inches(1.85), Inches(3.7), Inches(2.2)
)
g1.fill.solid()
g1.fill.fore_color.rgb = BG_MID
g1.line.color.rgb = ACCENT_BLUE
g1.line.width = Pt(1.5)
tf = g1.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.2)
tf.margin_top = Inches(0.1)
p = tf.paragraphs[0]
p.text = "IDENTITY & EXECUTION"
p.font.size = Pt(12)
p.font.color.rgb = ACCENT_BLUE
p.font.bold = True
p.font.name = "Calibri"

id_cols = [
    "EXECUTION_ID",
    "AGENT_ID  /  AGENT_NAME",
    "RUN_ID",
    "INVOCATION_ORDER",
    "STATUS",
    "PROMPT_VERSION",
]
for col in id_cols:
    p2 = tf.add_paragraph()
    p2.text = col
    p2.font.size = Pt(10)
    p2.font.color.rgb = ACCENT_GREEN
    p2.font.bold = True
    p2.font.name = "Consolas"
    p2.space_before = Pt(3)

# Group 2: Timing (top-middle)
g2 = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(4.7), Inches(1.85), Inches(3.5), Inches(2.2)
)
g2.fill.solid()
g2.fill.fore_color.rgb = BG_MID
g2.line.color.rgb = ACCENT_GREEN
g2.line.width = Pt(1.5)
tf = g2.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.2)
tf.margin_top = Inches(0.1)
p = tf.paragraphs[0]
p.text = "TIMING & DATA"
p.font.size = Pt(12)
p.font.color.rgb = ACCENT_GREEN
p.font.bold = True
p.font.name = "Calibri"

timing_cols = [
    ("STARTED_AT", "Execution start"),
    ("COMPLETED_AT", "Execution end"),
    ("DURATION_MS", "Duration in ms"),
    ("INPUT_DATA", "Full input (CLOB)"),
    ("OUTPUT_DATA", "Full output (CLOB)"),
    ("ERROR_MESSAGE", "Error details if failed"),
]
for col, desc in timing_cols:
    p2 = tf.add_paragraph()
    p2.text = col
    p2.font.size = Pt(10)
    p2.font.color.rgb = ACCENT_AMBER
    p2.font.bold = True
    p2.font.name = "Consolas"
    p2.space_before = Pt(2)
    p3 = tf.add_paragraph()
    p3.text = f"  {desc}"
    p3.font.size = Pt(9)
    p3.font.color.rgb = LIGHT_GRAY
    p3.font.name = "Calibri"

# Group 3: Token Metrics (top-right)
g3 = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(8.4), Inches(1.85), Inches(4.1), Inches(2.2)
)
g3.fill.solid()
g3.fill.fore_color.rgb = BG_MID
g3.line.color.rgb = ACCENT_AMBER
g3.line.width = Pt(1.5)
tf = g3.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.2)
tf.margin_top = Inches(0.1)
p = tf.paragraphs[0]
p.text = "TOKEN METRICS"
p.font.size = Pt(12)
p.font.color.rgb = ACCENT_AMBER
p.font.bold = True
p.font.name = "Calibri"

token_cols = [
    "INPUT_TOKENS",
    "OUTPUT_TOKENS",
    "TOTAL_TOKENS",
    "CACHED_CONTENT_TOKENS",
    "THOUGHTS_TOKENS",
    "TOOL_USE_PROMPT_TOKENS",
    "LLM_CALL_COUNT",
    "TOKEN_USAGE_DETAILS",
]
for col in token_cols:
    p2 = tf.add_paragraph()
    p2.text = col
    p2.font.size = Pt(10)
    p2.font.color.rgb = WHITE
    p2.font.bold = True
    p2.font.name = "Consolas"
    p2.space_before = Pt(2)

# Benefits row at bottom
benefits = [
    ("Zero Code", "Framework persists every\nagent run automatically",
     ACCENT_BLUE),
    ("Full I/O Capture", "Input & output data stored\nfor debugging & replay",
     ACCENT_GREEN),
    ("Cost Visibility", "Token breakdown per agent\nincl. cached & thinking tokens",
     ACCENT_AMBER),
    ("Compliance Ready", "Complete audit trail.\nWho ran what, when, how long",
     ACCENT_RED),
]
x = 0.8
for title, desc, clr in benefits:
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x), Inches(4.3), Inches(2.8), Inches(1.2)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(0x12, 0x22, 0x38)
    shape.line.color.rgb = clr
    shape.line.width = Pt(1.5)
    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.15)
    tf.margin_top = Inches(0.1)
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(14)
    p.font.color.rgb = clr
    p.font.bold = True
    p.font.name = "Calibri"
    p.alignment = PP_ALIGN.CENTER
    p2 = tf.add_paragraph()
    p2.text = desc
    p2.font.size = Pt(11)
    p2.font.color.rgb = LIGHT_GRAY
    p2.font.name = "Calibri"
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(4)
    x += 3.05


# ============================================================
# SLIDE 10 — Checkpoints Table
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 0.6, 11.7, 0.6,
            "State Persistence, NEXUS_AI_CHECKPOINT", 30, WHITE, True)
add_accent_line(slide, 0.8, 1.15, 5, ACCENT_AMBER)

add_textbox(slide, 0.8, 1.3, 11.7, 0.4,
            "Full graph state saved at every node transition. "
            "Enables replay, debugging, and resume from any point in the workflow.",
            13, LIGHT_GRAY)

# Column table — header row
col_headers = ["COLUMN", "TYPE", "DESCRIPTION"]
col_widths = [3.5, 3.5, 5.3]
col_starts = [0.8, 4.3, 7.8]

for col, x, w in zip(col_headers, col_starts, col_widths):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(x), Inches(1.9), Inches(w), Inches(0.42)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(0x1A, 0x30, 0x50)
    shape.line.color.rgb = RGBColor(0x30, 0x50, 0x70)
    shape.line.width = Pt(0.5)
    tf = shape.text_frame
    tf.margin_left = Inches(0.15)
    p = tf.paragraphs[0]
    p.text = col
    p.font.size = Pt(13)
    p.font.color.rgb = ACCENT_BLUE
    p.font.bold = True
    p.font.name = "Consolas"

# Data rows
rows = [
    ("CHECKPOINT_ID", "VARCHAR2(36)", "Unique checkpoint UUID",
     ACCENT_AMBER),
    ("RUN_ID", "VARCHAR2(255)", "Links to AI_CHAT_WORKFLOW_RUN, tracks which workflow",
     ACCENT_AMBER),
    ("NODE_ID", "VARCHAR2(255)", "Current node that just completed",
     ACCENT_GREEN),
    ("NEXT_NODE_ID", "VARCHAR2(255)", "Next node to execute, enables resume",
     ACCENT_GREEN),
    ("STATE_DATA", "CLOB", "Full graph state snapshot, all scope variables as JSON",
     WHITE),
    ("SAVED_AT", "TIMESTAMP(6) WITH TZ", "When checkpoint was saved, defaults to CURRENT_TIMESTAMP",
     LIGHT_GRAY),
]

y = 2.32
for col_name, dtype, desc, name_clr in rows:
    for val, x, w, clr in [
        (col_name, 0.8, 3.5, name_clr),
        (dtype, 4.3, 3.5, MID_GRAY),
        (desc, 7.8, 5.3, LIGHT_GRAY),
    ]:
        shape = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(x), Inches(y), Inches(w), Inches(0.42)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = CODE_BG
        shape.line.color.rgb = RGBColor(0x25, 0x35, 0x50)
        shape.line.width = Pt(0.3)
        tf = shape.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.15)
        tf.margin_top = Inches(0.04)
        p = tf.paragraphs[0]
        p.text = val
        p.font.size = Pt(12)
        p.font.color.rgb = clr
        p.font.name = "Consolas" if x < 7.8 else "Calibri"
        if x == 0.8:
            p.font.bold = True
    y += 0.42

# Benefits row
benefits = [
    ("Replay", "Re-run from any checkpoint\nwithout restarting the\nentire workflow",
     ACCENT_BLUE),
    ("Debug", "Inspect full state at every\nnode, what went in,\nwhat came out",
     ACCENT_GREEN),
    ("Resume", "NEXT_NODE_ID tracks where\nto continue after a failure\nor restart",
     ACCENT_AMBER),
    ("Audit", "Complete execution history\ntied to RUN_ID. Every\nstate transition recorded",
     ACCENT_RED),
]
x = 0.8
for title, desc, clr in benefits:
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x), Inches(5.2), Inches(2.8), Inches(1.5)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(0x12, 0x22, 0x38)
    shape.line.color.rgb = clr
    shape.line.width = Pt(1.5)
    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.15)
    tf.margin_top = Inches(0.1)
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(16)
    p.font.color.rgb = clr
    p.font.bold = True
    p.font.name = "Calibri"
    p.alignment = PP_ALIGN.CENTER
    p2 = tf.add_paragraph()
    p2.text = desc
    p2.font.size = Pt(11)
    p2.font.color.rgb = LIGHT_GRAY
    p2.font.name = "Calibri"
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(4)
    x += 3.05


# ============================================================
# SLIDE 11 — Nexus AI Studio (Info)
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

STUDIO_PURPLE = RGBColor(0x7B, 0x61, 0xFF)

add_textbox(slide, 0.8, 0.6, 11.7, 0.6,
            "Nexus AI Studio", 30, WHITE, True)
add_accent_line(slide, 0.8, 1.15, 5, STUDIO_PURPLE)

add_textbox(slide, 0.8, 1.4, 11.7, 0.4,
            "Raw execution data is powerful for auditing. "
            "But when you're building a 12-agent pipeline, you need to see it.",
            14, LIGHT_GRAY)

# Today section (left)
add_textbox(slide, 0.8, 1.95, 5.5, 0.4, "Today", 18, STUDIO_PURPLE, True)

today_items = [
    ("Graph Visualization", "Renders your workflow graph as an interactive UI"),
    ("Run Workflows from UI", "Trigger and monitor executions in the browser"),
    ("Live Execution Tracking", "Agents light up, complete, or fail in real time"),
    ("State Inspection", "Click any node for full input/output at that checkpoint"),
]
y = 2.4
for title, desc in today_items:
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(0.8), Inches(y), Inches(5.5), Inches(0.7)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = BG_MID
    shape.line.color.rgb = STUDIO_PURPLE
    shape.line.width = Pt(1.5)
    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.06)
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(13)
    p.font.color.rgb = STUDIO_PURPLE
    p.font.bold = True
    p.font.name = "Calibri"
    p2 = tf.add_paragraph()
    p2.text = desc
    p2.font.size = Pt(11)
    p2.font.color.rgb = LIGHT_GRAY
    p2.font.name = "Calibri"
    p2.space_before = Pt(2)
    y += 0.78

# Vision section (right)
add_textbox(slide, 7.0, 1.95, 5.5, 0.4, "Vision: Swagger for AI", 18,
            ACCENT_AMBER, True)

vision_items = [
    ("Auto-Discover Agents", "Scans app context, lists every registered agent"),
    ("Run Individual Agents", "Test any agent in isolation, pass input, see output"),
    ("Run Full Workflows", "End-to-end pipelines with live graph feedback"),
    ("One UI for Everything", "Like Swagger gave APIs a face, Studio gives agents a face"),
]
y = 2.4
for title, desc in vision_items:
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(7.0), Inches(y), Inches(5.5), Inches(0.7)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = BG_MID
    shape.line.color.rgb = ACCENT_AMBER
    shape.line.width = Pt(1.5)
    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.06)
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(13)
    p.font.color.rgb = ACCENT_AMBER
    p.font.bold = True
    p.font.name = "Calibri"
    p2 = tf.add_paragraph()
    p2.text = desc
    p2.font.size = Pt(11)
    p2.font.color.rgb = LIGHT_GRAY
    p2.font.name = "Calibri"
    p2.space_before = Pt(2)
    y += 0.78

# Bottom tagline
add_textbox(slide, 1.0, 5.7, 11.3, 0.5,
            "React + TypeScript SPA, packaged as a Spring Boot JAR. "
            "Add one Maven dependency, get the full UI.",
            14, MID_GRAY, False, PP_ALIGN.CENTER)


# ============================================================
# SLIDE 12 — Nexus AI Studio (Live Demo)
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 0.4, 11.7, 0.5,
            "Nexus AI Studio, Live Demo", 28, WHITE, True)
add_accent_line(slide, 0.8, 0.85, 5, STUDIO_PURPLE)

studio_img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "studio_screenshot.png")
slide.shapes.add_picture(studio_img_path, Inches(0.5), Inches(1.1),
                         width=Inches(12.3))


# ============================================================
# SLIDE 14 — Prompts Are Code
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 1.0, 11.7, 0.6,
            "Prompts Are Code", 32, WHITE, True)
add_accent_line(slide, 0.8, 1.55, 5, ACCENT_RED)

narrative = [
    "A prompt that degrades model output doesn't throw an exception. "
    "It silently returns worse results.",
    "",
    "You won't catch it in unit tests. You may not catch it in integration "
    "tests. You catch it when a business user files a ticket.",
    "",
    "We treat configuration as code, infrastructure as code. "
    "Why not prompts as code?",
    "",
    "PromptLint brings static analysis to prompt engineering: "
    "the same discipline we apply to Java, applied to the strings we send to models.",
]

y = 2.0
for line in narrative:
    if line == "":
        y += 0.15
        continue
    add_textbox(slide, 1.5, y, 10.0, 0.5, line, 16, LIGHT_GRAY)
    y += 0.55

# Quote
shape = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(2.0), Inches(4.8), Inches(9.0), Inches(0.7)
)
shape.fill.solid()
shape.fill.fore_color.rgb = BG_MID
shape.line.color.rgb = ACCENT_RED
shape.line.width = Pt(2)
tf = shape.text_frame
p = tf.paragraphs[0]
p.text = '"A bad prompt is a bug. PromptLint finds it before it ships."'
p.font.size = Pt(20)
p.font.color.rgb = WHITE
p.font.bold = True
p.font.name = "Calibri"
p.alignment = PP_ALIGN.CENTER

# Key stats
stats = [
    ("No LLM calls", "Fully deterministic, rule-based analysis"),
    ("Milliseconds", "Fast enough for pre-commit hooks and CI gates"),
    ("Deterministic", "Same prompt always produces the same score"),
]
x = 1.5
for title, desc in stats:
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x), Inches(5.8), Inches(3.2), Inches(0.9)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = BG_MID
    shape.line.fill.background()
    tf = shape.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(16)
    p.font.color.rgb = ACCENT_RED
    p.font.bold = True
    p.font.name = "Calibri"
    p.alignment = PP_ALIGN.CENTER
    p2 = tf.add_paragraph()
    p2.text = desc
    p2.font.size = Pt(11)
    p2.font.color.rgb = LIGHT_GRAY
    p2.font.name = "Calibri"
    p2.alignment = PP_ALIGN.CENTER
    x += 3.5


# ============================================================
# SLIDE 15 — 8 Quality Dimensions
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 1.0, 11.7, 0.6,
            "8 Quality Dimensions", 32, WHITE, True)
add_accent_line(slide, 0.8, 1.55, 5, ACCENT_RED)

dimensions = [
    ("CLR", "Clarity", "Sentence structure, ambiguous pronouns, vague quantifiers"),
    ("SPC", "Specificity", "Under-constrained instructions, missing format requirements"),
    ("GND", "Groundedness", "Hallucination risk, claims without context anchoring"),
    ("OUT", "Output Format", "Missing output schema, ambiguous response format"),
    ("CON", "Conciseness", "Redundancy, repetition, padding"),
    ("CST", "Consistency", "Contradictory instructions within the same prompt"),
    ("TKN", "Token Efficiency", "Unnecessary verbosity relative to instruction density"),
    ("INJ", "Injection Risk", "Prompt injection surface area, missing delimiters"),
]

y = 2.0
for code_str, name, desc in dimensions:
    # Code badge
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(1.0), Inches(y), Inches(0.8), Inches(0.45)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = ACCENT_RED
    shape.line.fill.background()
    tf = shape.text_frame
    p = tf.paragraphs[0]
    p.text = code_str
    p.font.size = Pt(12)
    p.font.color.rgb = WHITE
    p.font.bold = True
    p.font.name = "Consolas"
    p.alignment = PP_ALIGN.CENTER

    add_textbox(slide, 2.0, y + 0.02, 2.5, 0.4, name, 15, WHITE, True)
    add_textbox(slide, 4.5, y + 0.02, 7.5, 0.4, desc, 13, LIGHT_GRAY)
    y += 0.55

add_textbox(slide, 1.0, 6.6, 11.0, 0.4,
            "Each dimension scores 0 to 1. Weighted composite score. "
            "Configurable thresholds per dimension or aggregate.",
            13, MID_GRAY, False, PP_ALIGN.CENTER)


# ============================================================
# SLIDE 16 — JUnit API + CI Integration
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 1.0, 11.7, 0.6,
            "JUnit API + CI Integration", 32, WHITE, True)
add_accent_line(slide, 0.8, 1.55, 5, ACCENT_RED)

# Left — JUnit code
add_textbox(slide, 0.8, 1.8, 5.5, 0.3,
            "JUnit Assertion API", 14, ACCENT_RED, True)

junit_code = '''@Test
@DisplayName("Fetch CSM_CLASSIFIER prompt from H2
  and validate quality report meets threshold
  and has no critical issues")
void shouldFetchAndValidateCsmClassifierPromptQuality() {
    String agentName = CSM_CLASSIFIER.getValue();
    Prompt prompt = nexusStoreProvider
        .prompts().lookup(agentName).get();
    assertNotNull(prompt, "Prompt should not be null.");

    PromptUnderTest promptUnderTest = new PromptUnderTest(
        agentName,
        prompt.getSystemInstruction(),
        prompt.getPromptText(),
        Set.of("gcsFilePath", "sourceClassification",
               "extractedCandidates"),
        "output",
        AgentTypeProfile.CLASSIFICATION,
        prompt.getResponseSchema());

    PromptQualityReport report =
        analyzer.analyze(promptUnderTest);

    assertThat(report)
        .printReport(0.75)
        .passesThreshold(0.75)
        .hasNoCriticalIssues();
}'''

add_code_block(slide, 0.8, 2.15, 6.5, 5.3, junit_code, 11)

# Right — Test execution output (text reproduction)
add_textbox(slide, 7.5, 1.8, 5.5, 0.3,
            "Test Execution Output", 14, ACCENT_RED, True)

report_output = '''PROMPT QUALITY REPORT: document-summarizer
Profile: EXTRACTION

Overall Score: 0.75 / 1.00  PASS (threshold: 0.50)

Dimension          Score  Weight  Contrib
CLARITY             1.00   0.10    0.100
SPECIFICITY         0.58   0.15    0.088
GROUNDEDNESS        0.92   0.25    0.229
OUTPUT_CONTRACT     0.83   0.15    0.125
CONSTRAINT_COVERAGE 0.20   0.15    0.030
CONSISTENCY         1.00   0.10    0.100
TOKEN_EFFICIENCY    1.00   0.05    0.050
INJECTION_RESISTANCE 0.63  0.05    0.031

Weakest: CONSTRAINT_COVERAGE (0.20)

Issues: 9 total (0 critical, 3 warning, 6 info)
WARN [SPC-004] No positive examples found
WARN [CON-001] No instructions for empty input
WARN [INJ-001] No defence against embedded prompts

Suggestions:
1. Add 2+ positive examples
2. Use proper JSON types: "id": 1 not "1"
3. Show nullable fields as null in example
4. Add empty input handling instruction
5. Add ambiguous case guidance
6. Add prompt injection defence'''

add_code_block(slide, 7.5, 2.15, 5.3, 5.3, report_output, 9)

# Bottom note
add_textbox(slide, 0.8, 6.8, 11.5, 0.5,
            "No extra service, no API key, no network call. Just a dependency "
            "on the classpath. Runs in milliseconds.",
            14, ACCENT_AMBER)


# ============================================================
# SLIDE — Getting Started
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 0.8, 0.6, 11.7, 0.6,
            "Getting Started", 30, WHITE, True)
add_accent_line(slide, 0.8, 1.15, 5, ACCENT_GREEN)

add_textbox(slide, 0.8, 1.4, 11.7, 0.4,
            "Three dependencies. A few properties. You have the whole framework.",
            16, LIGHT_GRAY)

# Maven dependencies
maven_code = '''<!-- Nexus AI, workflow orchestration + agent pipeline -->
<dependency>
    <groupId>com.db.clm</groupId>
    <artifactId>nexus-ai</artifactId>
    <version>LATEST</version>
</dependency>

<!-- Nexus AI Studio, graph visualization UI -->
<dependency>
    <groupId>com.db.clm</groupId>
    <artifactId>nexus-ai-studio</artifactId>
    <version>LATEST</version>
</dependency>

<!-- PromptLint, static prompt quality analyser -->
<dependency>
    <groupId>com.db.clm</groupId>
    <artifactId>clm-prompt-lint</artifactId>
    <version>LATEST</version>
</dependency>'''

add_code_block(slide, 0.8, 1.9, 6.0, 4.5, maven_code, 12)

# Properties (from real application-local.yaml)
add_textbox(slide, 7.2, 1.9, 5.5, 0.35,
            "application-local.yaml", 14, ACCENT_AMBER, True)

props_code = '''clm:
  nexus:
    ai:
      enabled: true
      wif:
        wif_provider: /path/provider.json
        wif_keystore: /path/keystore.json
      azure:
        tenant_id: ENC(...)
        client_id: ENC(...)
        scope: api://.../.default
        grant_type: client_credentials
      google:
        project_id: db-dev-daa2-dbclm
        location: europe-west4
        transport: REST
        credentials:
          project_number: ENC(...)
          workload_identity_pool_id: ENC(...)
          service_account_email: ENC(...)
      rate-limit:
        enabled: true
        requests-per-second: 0.5
        max-bucket-size: 10
      studio:
        enabled: true
        path: /studio'''

add_code_block(slide, 7.2, 2.3, 5.5, 4.1, props_code, 9)


# ============================================================
# SLIDE — Thank You & Q&A
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)

add_textbox(slide, 1.0, 2.5, 11.3, 1.0,
            "Thank You", 48, WHITE, True, PP_ALIGN.CENTER)
add_textbox(slide, 1.0, 3.6, 11.3, 0.6,
            "Questions & Discussion", 28, ACCENT_BLUE, False, PP_ALIGN.CENTER)

add_textbox(slide, 3.0, 5.0, 7.3, 0.4,
            "Akshay Dipta, CLM Tech, Senior Engineer", 16, LIGHT_GRAY,
            False, PP_ALIGN.CENTER)


# ============================================================
# SAVE
# ============================================================
output_path = "/Users/akshaydipta/Documents/promotion/RCP_session/Nexus_AI_PromptLint_RCP.pptx"
prs.save(output_path)
print(f"Saved: {output_path}")
print(f"Slides: {len(prs.slides)}")
