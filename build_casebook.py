from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

out = Path('output/pdf'); out.mkdir(parents=True, exist_ok=True)
pdf = out / 'AI_PM_Portfolio_Casebook.pdf'
styles = getSampleStyleSheet()
story = []
def add(title, body):
    story.extend([Paragraph(title, styles['Heading1']), Paragraph(body, styles['BodyText']), Spacer(1, 12)])
add('AI Product Manager Portfolio', 'Global Seller Growth and Applied AI Product Delivery')
add('Portfolio positioning', 'Four independent working MVPs demonstrate product discovery, technical judgment, stakeholder alignment, AI evaluation, and safe delivery. All datasets, metrics, outcomes, and examples are synthetic portfolio demonstrations.')
story.append(PageBreak())
add('Unified product narrative', 'Opportunity Discovery identifies where product investment may create value. Seller Growth Copilot turns performance signals into explainable actions. Seller Support Automation scales safe help. Marketing Lead Discovery RAG demonstrates source-grounded research with hybrid retrieval, reranking, citations, and evaluation.')
add('Technical PM framework', 'Use AI for ambiguity and unstructured language; use APIs for facts; use deterministic logic for explicit rules; use restricted tools for actions; use human approval for high-risk decisions.')
story.append(PageBreak())
add('Project case studies', 'AI Seller Growth Copilot: diagnoses seller growth blockers and tracks recommendations to outcomes. Marketplace Opportunity Discovery: scores seller opportunities and recommends roadmap initiatives. AI Seller Support Automation: classifies tickets, retrieves approved guidance, drafts responses, and escalates policy-sensitive requests. Marketing Lead Discovery RAG: produces cited lead profiles from synthetic approved sources.')
add('Stakeholder and pilot plan', 'Align sellers, seller-success and support teams, engineering, data and analytics, policy, finance, and leadership around shared metrics: task completion, quality, safety, cost, and operational readiness.')
story.append(PageBreak())
add('RAG and agent decisions', 'Evaluate retrieval with Recall@K, Precision@K, relevance, and ranking quality. Evaluate generation with groundedness, completeness, and citation correctness. Keep identity, authorization, policy, tool validation, human approval, and audit outside the model boundary.')
add('Links', 'GitHub: https://github.com/hahAI111/ai-pm-portfolio<br/>Demo video: https://github.com/hahAI111/ai-pm-portfolio/releases/tag/v1.0-portfolio-demo')
SimpleDocTemplate(str(pdf), pagesize=A4, rightMargin=45, leftMargin=45, topMargin=40, bottomMargin=40).build(story)
print(pdf.resolve())
