"""
Prompt Chaining Implementation
==============================
Breaking complex tasks into sequential prompts where each output feeds into the next.
Best for: Multi-stage workflows, complex analysis, content pipelines.
"""

import os
from groq import Groq
from dotenv import load_dotenv
import json
from datetime import datetime
import time

load_dotenv()

class PromptChaining:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.model = "llama-3.1-8b-instant"
        self.results = []
        self.chains = []
    
    def call_model(self, prompt: str, temperature: float = 0.7, max_tokens: int = 2048) -> str:
        """Make API call to Groq"""
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=self.model,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    
    def content_creation_pipeline(self):
        """Example 1: Blog Post Creation Pipeline"""
        print("\n" + "="*70)
        print("EXAMPLE 1: CONTENT CREATION PIPELINE")
        print("="*70)
        
        topic = "The Future of Remote Work"
        chain_record = {"workflow": "blog_post_creation", "steps": []}
        
        # Step 1: Generate outline
        print("\n STEP 1: Generating blog post outline...")
        prompt1 = f"""Create a detailed outline for a blog post about: {topic}

Include:
- A catchy title
- Introduction hook
- 4-5 main sections with subsections
- Conclusion
- Key takeaways

Provide only the outline."""
        
        outline = self.call_model(prompt1, temperature=0.7)
        print(f"\nOutline:\n{outline}")
        chain_record["steps"].append({
            "step": 1,
            "action": "generate_outline",
            "output": outline
        })
        
        # Step 2: Write introduction
        print("\n\n STEP 2: Writing introduction based on outline...")
        prompt2 = f"""Based on this outline:

{outline}

Write an engaging introduction (150-200 words) that:
- Hooks the reader
- Introduces the topic
- Previews what they'll learn

Introduction:"""
        
        introduction = self.call_model(prompt2, temperature=0.7, max_tokens=500)
        print(f"\nIntroduction:\n{introduction}")
        chain_record["steps"].append({
            "step": 2,
            "action": "write_introduction",
            "output": introduction
        })
        
        # Step 3: Expand first main section
        print("\n\n STEP 3: Expanding first main section...")
        prompt3 = f"""Based on this outline:

{outline}

And this introduction:

{introduction}

Write the first main section (300-400 words) with:
- Clear explanations
- Examples or statistics
- Smooth transitions

First Section:"""
        
        first_section = self.call_model(prompt3, temperature=0.7, max_tokens=800)
        print(f"\nFirst Section:\n{first_section}")
        chain_record["steps"].append({
            "step": 3,
            "action": "write_first_section",
            "output": first_section
        })
        
        # Step 4: Generate meta description
        print("\n\n STEP 4: Creating SEO meta description...")
        prompt4 = f"""Based on this blog post content:

Introduction:
{introduction}

First Section:
{first_section}

Write a compelling SEO meta description (150-160 characters) that summarizes the article.

Meta Description:"""
        
        meta_desc = self.call_model(prompt4, temperature=0.6, max_tokens=200)
        print(f"\nMeta Description:\n{meta_desc}")
        chain_record["steps"].append({
            "step": 4,
            "action": "generate_meta_description",
            "output": meta_desc
        })
        
        self.chains.append(chain_record)
    
    def data_analysis_workflow(self):
        """Example 2: Data Analysis Workflow"""
        print("\n" + "="*70)
        print("EXAMPLE 2: DATA ANALYSIS WORKFLOW")
        print("="*70)
        
        raw_data = """
        Sales Data Q4 2024:
        Product A: Jan $45K, Feb $52K, Mar $48K, Apr $61K
        Product B: Jan $38K, Feb $41K, Mar $39K, Apr $44K
        Product C: Jan $29K, Feb $33K, Mar $42K, Apr $51K
        
        Customer Feedback Scores (1-10):
        Product A: 8.2, 8.5, 8.1, 8.7
        Product B: 7.1, 7.3, 7.2, 7.5
        Product C: 6.8, 7.2, 7.9, 8.4
        """
        
        chain_record = {"workflow": "data_analysis", "steps": []}
        
        # Step 1: Extract and structure data
        print("\n STEP 1: Extracting and structuring data...")
        prompt1 = f"""Extract and structure this data clearly:

{raw_data}

Format as:
1. Sales trends for each product
2. Customer satisfaction trends
3. Key observations

Structured Data:"""
        
        structured = self.call_model(prompt1, temperature=0.3, max_tokens=800)
        print(f"\nStructured Data:\n{structured}")
        chain_record["steps"].append({
            "step": 1,
            "action": "structure_data",
            "output": structured
        })
        
        # Step 2: Calculate metrics
        print("\n\n STEP 2: Calculating key metrics...")
        prompt2 = f"""Based on this structured data:

{structured}

Calculate:
1. Growth rate for each product (Jan to Apr)
2. Average customer satisfaction per product
3. Best and worst performing products

Metrics:"""
        
        metrics = self.call_model(prompt2, temperature=0.2, max_tokens=600)
        print(f"\nCalculated Metrics:\n{metrics}")
        chain_record["steps"].append({
            "step": 2,
            "action": "calculate_metrics",
            "output": metrics
        })
        
        # Step 3: Identify insights
        print("\n\n STEP 3: Identifying insights and patterns...")
        prompt3 = f"""Based on these metrics:

{metrics}

Identify:
1. Key insights (what's working, what's not)
2. Patterns or correlations
3. Surprising findings

Insights:"""
        
        insights = self.call_model(prompt3, temperature=0.6, max_tokens=800)
        print(f"\nInsights:\n{insights}")
        chain_record["steps"].append({
            "step": 3,
            "action": "identify_insights",
            "output": insights
        })
        
        # Step 4: Generate recommendations
        print("\n\n STEP 4: Generating actionable recommendations...")
        prompt4 = f"""Based on these insights:

{insights}

And the original metrics:
{metrics}

Provide:
1. Top 3 actionable recommendations
2. Expected impact for each
3. Priority level (High/Medium/Low)

Recommendations:"""
        
        recommendations = self.call_model(prompt4, temperature=0.5, max_tokens=800)
        print(f"\nRecommendations:\n{recommendations}")
        chain_record["steps"].append({
            "step": 4,
            "action": "generate_recommendations",
            "output": recommendations
        })
        
        self.chains.append(chain_record)
    
    def customer_support_workflow(self):
        """Example 3: Customer Support Ticket Resolution"""
        print("\n" + "="*70)
        print("EXAMPLE 3: CUSTOMER SUPPORT WORKFLOW")
        print("="*70)
        
        ticket = """
        Customer: Sarah Johnson
        Issue: "I ordered a blue laptop case 2 weeks ago (Order #12345) but received 
        a red one. I need the blue case for a presentation next week. Also, I was 
        charged twice on my credit card. This is very frustrating!"
        """
        
        chain_record = {"workflow": "support_ticket", "steps": []}
        
        # Step 1: Categorize and prioritize
        print("\n STEP 1: Categorizing and prioritizing ticket...")
        prompt1 = f"""Analyze this support ticket:

{ticket}

Classify:
1. Issue categories (select all that apply)
2. Priority level (Low/Medium/High/Critical)
3. Sentiment (Positive/Neutral/Negative/Angry)
4. Urgency indicators

Classification:"""
        
        classification = self.call_model(prompt1, temperature=0.3)
        print(f"\nClassification:\n{classification}")
        chain_record["steps"].append({
            "step": 1,
            "action": "classify_ticket",
            "output": classification
        })
        
        # Step 2: Extract action items
        print("\n\n STEP 2: Extracting required actions...")
        prompt2 = f"""Based on this ticket:

{ticket}

And this classification:
{classification}

List all required actions to resolve this completely:
1. Immediate actions
2. Follow-up actions
3. Systems to check (orders, payments, inventory)

Action Items:"""
        
        actions = self.call_model(prompt2, temperature=0.4)
        print(f"\nAction Items:\n{actions}")
        chain_record["steps"].append({
            "step": 2,
            "action": "extract_actions",
            "output": actions
        })
        
        # Step 3: Draft response
        print("\n\n STEP 3: Drafting customer response...")
        prompt3 = f"""Based on:

Original ticket:
{ticket}

Required actions:
{actions}

Draft a professional, empathetic email response that:
1. Acknowledges all issues
2. Apologizes appropriately
3. Explains resolution steps
4. Provides timeline
5. Offers compensation if appropriate

Email Response:"""
        
        response = self.call_model(prompt3, temperature=0.6, max_tokens=800)
        print(f"\nDraft Response:\n{response}")
        chain_record["steps"].append({
            "step": 3,
            "action": "draft_response",
            "output": response
        })
        
        # Step 4: Create internal notes
        print("\n\n STEP 4: Creating internal tracking notes...")
        prompt4 = f"""Create internal notes for this ticket:

Ticket: {ticket}
Actions: {actions}
Response sent: {response}

Format:
- Summary (1 line)
- Actions taken
- Follow-up required
- Escalation (Yes/No)

Internal Notes:"""
        
        notes = self.call_model(prompt4, temperature=0.4)
        print(f"\nInternal Notes:\n{notes}")
        chain_record["steps"].append({
            "step": 4,
            "action": "create_notes",
            "output": notes
        })
        
        self.chains.append(chain_record)
    
    def research_synthesis_workflow(self):
        """Example 4: Research Synthesis Pipeline"""
        print("\n" + "="*70)
        print("EXAMPLE 4: RESEARCH SYNTHESIS WORKFLOW")
        print("="*70)
        
        sources = [
            "Study 1: Daily exercise reduces stress by 40% (University A, 2024)",
            "Study 2: 30 minutes of walking improves mood markers (Journal B, 2023)",
            "Study 3: Exercise linked to better sleep quality in 85% of participants (Institute C, 2024)"
        ]
        
        chain_record = {"workflow": "research_synthesis", "steps": []}
        
        # Step 1: Summarize each source
        print("\n STEP 1: Summarizing individual sources...")
        summaries = []
        for idx, source in enumerate(sources, 1):
            prompt = f"""Summarize the key findings from this research:

{source}

Include:
- Main finding
- Sample/methodology hint
- Year and source

Summary:"""
            
            summary = self.call_model(prompt, temperature=0.4, max_tokens=200)
            summaries.append(summary)
            print(f"\nSource {idx} Summary:\n{summary}")
        
        all_summaries = "\n\n".join(summaries)
        chain_record["steps"].append({
            "step": 1,
            "action": "summarize_sources",
            "output": all_summaries
        })
        
        # Step 2: Identify common themes
        print("\n\n STEP 2: Identifying common themes...")
        prompt2 = f"""Based on these research summaries:

{all_summaries}

Identify:
1. Common themes across studies
2. Converging findings
3. Areas of agreement

Themes:"""
        
        themes = self.call_model(prompt2, temperature=0.5)
        print(f"\nCommon Themes:\n{themes}")
        chain_record["steps"].append({
            "step": 2,
            "action": "identify_themes",
            "output": themes
        })
        
        # Step 3: Synthesize conclusions
        print("\n\n STEP 3: Synthesizing overall conclusions...")
        prompt3 = f"""Based on:

Original sources:
{chr(10).join(sources)}

Common themes:
{themes}

Synthesize:
1. Overall conclusions
2. Strength of evidence
3. Practical implications

Synthesis:"""
        
        synthesis = self.call_model(prompt3, temperature=0.5, max_tokens=800)
        print(f"\nSynthesis:\n{synthesis}")
        chain_record["steps"].append({
            "step": 3,
            "action": "synthesize_conclusions",
            "output": synthesis
        })
        
        # Step 4: Generate executive summary
        print("\n\n STEP 4: Creating executive summary...")
        prompt4 = f"""Create a brief executive summary (100 words) based on:

{synthesis}

Executive Summary:"""
        
        exec_summary = self.call_model(prompt4, temperature=0.5, max_tokens=300)
        print(f"\nExecutive Summary:\n{exec_summary}")
        chain_record["steps"].append({
            "step": 4,
            "action": "executive_summary",
            "output": exec_summary
        })
        
        self.chains.append(chain_record)
    
    def code_review_workflow(self):
        """Example 5: Code Review Pipeline"""
        print("\n" + "="*70)
        print("EXAMPLE 5: CODE REVIEW WORKFLOW")
        print("="*70)
        
        code = '''
def process_user_data(users):
    result = []
    for user in users:
        if user['age'] > 18:
            result.append({
                'name': user['name'],
                'email': user['email'],
                'status': 'adult'
            })
    return result

users = [
    {'name': 'Alice', 'age': 25, 'email': 'alice@email.com'},
    {'name': 'Bob', 'age': 17, 'email': 'bob@email.com'}
]
output = process_user_data(users)
'''
        
        chain_record = {"workflow": "code_review", "steps": []}
        
        # Step 1: Analyze code structure
        print("\n STEP 1: Analyzing code structure...")
        prompt1 = f"""Analyze this code's structure:

{code}

Evaluate:
1. Function clarity and naming
2. Code organization
3. Readability

Structure Analysis:"""
        
        structure = self.call_model(prompt1, temperature=0.4)
        print(f"\nStructure Analysis:\n{structure}")
        chain_record["steps"].append({
            "step": 1,
            "action": "analyze_structure",
            "output": structure
        })
        
        # Step 2: Identify potential bugs
        print("\n\n STEP 2: Identifying potential bugs and edge cases...")
        prompt2 = f"""Review this code for bugs:

{code}

Identify:
1. Potential runtime errors
2. Edge cases not handled
3. Logic issues

Bug Analysis:"""
        
        bugs = self.call_model(prompt2, temperature=0.4)
        print(f"\nBug Analysis:\n{bugs}")
        chain_record["steps"].append({
            "step": 2,
            "action": "identify_bugs",
            "output": bugs
        })
        
        # Step 3: Suggest improvements
        print("\n\n STEP 3: Suggesting improvements...")
        prompt3 = f"""Based on:

Original code:
{code}

Structure analysis:
{structure}

Bug analysis:
{bugs}

Suggest:
1. Performance improvements
2. Better error handling
3. Code style improvements

Improvements:"""
        
        improvements = self.call_model(prompt3, temperature=0.5)
        print(f"\nSuggested Improvements:\n{improvements}")
        chain_record["steps"].append({
            "step": 3,
            "action": "suggest_improvements",
            "output": improvements
        })
        
        # Step 4: Generate refactored code
        print("\n\n STEP 4: Generating refactored version...")
        prompt4 = f"""Refactor this code based on:

Original:
{code}

Improvements needed:
{improvements}

Provide the refactored code with comments explaining changes:"""
        
        refactored = self.call_model(prompt4, temperature=0.4, max_tokens=1000)
        print(f"\nRefactored Code:\n{refactored}")
        chain_record["steps"].append({
            "step": 4,
            "action": "refactor_code",
            "output": refactored
        })
        
        self.chains.append(chain_record)
    
    def save_results(self):
        """Save all chain results to a JSON file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"prompt_chaining_results_{timestamp}.json"
        
        output_data = {
            "technique": "Prompt Chaining",
            "model": self.model,
            "timestamp": timestamp,
            "total_workflows": len(self.chains),
            "workflows": self.chains
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n{'='*70}")
        print(f"Results saved to: {filename}")
        print(f"{'='*70}")
    
    def run_all_workflows(self):
        """Execute all prompt chaining workflows"""
        print("\n" + "="*70)
        print("PROMPT CHAINING DEMONSTRATION")
        print("="*70)
        print("Model: " + self.model)
        print("="*70)
        
        try:
            self.content_creation_pipeline()
            self.data_analysis_workflow()
            self.customer_support_workflow()
            self.research_synthesis_workflow()
            self.code_review_workflow()
            
            self.save_results()
            
            print("\n All workflows completed successfully!")
            
        except Exception as e:
            print(f"\n Error occurred: {str(e)}")
            print("\nMake sure GROQ_API_KEY is set in your .env file")


def main():
    chaining = PromptChaining()
    chaining.run_all_workflows()


if __name__ == "__main__":
    main()