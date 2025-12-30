"""
Chain of Thought (CoT) Prompting Implementation
===============================================
Encourages the model to break down complex problems into step-by-step reasoning.
Best for: Math problems, logical reasoning, complex analysis, debugging.
"""

import os
from groq import Groq
from dotenv import load_dotenv
import json
from datetime import datetime

load_dotenv()

class ChainOfThoughtPrompting:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.model = "llama-3.1-8b-instant"
        self.results = []
    
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
    
    def math_word_problem(self):
        """Example 1: Math Word Problems with Step-by-Step Solution"""
        print("\n" + "="*70)
        print("EXAMPLE 1: MATH WORD PROBLEMS")
        print("="*70)
        
        problems = [
            {
                "problem": "A store sells apples for $3 per pound and oranges for $2 per pound. If John buys 4 pounds of apples and 6 pounds of oranges, and he pays with a $50 bill, how much change will he get back?",
                "difficulty": "Easy"
            },
            {
                "problem": "A train travels at 60 mph for 2 hours, then increases its speed to 80 mph for the next 3 hours. What is the total distance traveled?",
                "difficulty": "Medium"
            },
            {
                "problem": "In a class of 40 students, 60% are girls. If 25% of the girls and 40% of the boys wear glasses, how many students in total wear glasses?",
                "difficulty": "Medium"
            }
        ]
        
        for idx, item in enumerate(problems, 1):
            prompt = f"""Solve this math problem step by step. Show your reasoning clearly.

Problem: {item['problem']}

Let's solve this step by step:

Step 1: Identify what we know
Step 2: Determine what we need to find
Step 3: Set up the calculation
Step 4: Solve
Step 5: Verify the answer

Solution:"""
            
            print(f"\n--- Problem {idx} ({item['difficulty']}) ---")
            print(f"Problem: {item['problem']}")
            print("\nSolving step by step...")
            result = self.call_model(prompt, temperature=0.3)
            print(f"\n{result}")
            
            self.results.append({
                "task": "math_problem",
                "difficulty": item['difficulty'],
                "problem": item['problem'],
                "output": result
            })
    
    def logical_reasoning(self):
        """Example 2: Logical Reasoning and Deduction"""
        print("\n" + "="*70)
        print("EXAMPLE 2: LOGICAL REASONING")
        print("="*70)
        
        puzzle = """
        Five friends - Alice, Bob, Carol, David, and Emma - are sitting in a row.
        - Alice is not at either end
        - Bob is sitting next to Alice
        - Carol is sitting at one of the ends
        - David is not sitting next to Carol
        - Emma is sitting between two people
        
        Question: What is the order of people from left to right?
        """
        
        prompt = f"""Solve this logical puzzle using step-by-step reasoning.

Puzzle:
{puzzle.strip()}

Let's analyze this systematically:

Step 1: List all the constraints
Step 2: Start with definite positions (Carol is at an end)
Step 3: Apply each constraint one by one
Step 4: Eliminate impossible arrangements
Step 5: Find the valid arrangement

Solution:"""
        
        print(f"\nPuzzle:\n{puzzle.strip()}")
        print("\nReasoning through the puzzle...")
        result = self.call_model(prompt, temperature=0.3)
        print(f"\n{result}")
        
        self.results.append({
            "task": "logical_reasoning",
            "puzzle_type": "arrangement",
            "output": result
        })
        
        # Second puzzle
        riddle = """
        If all Bloops are Razzies and all Razzies are Lazzies, are all Bloops definitely Lazzies?
        Also, if some Lazzies are Jazzies, can we conclude that some Bloops are Jazzies?
        """
        
        prompt2 = f"""Solve this logical reasoning problem step by step.

Problem:
{riddle.strip()}

Let's use logical reasoning:

Step 1: Identify the logical relationships (if-then statements)
Step 2: Visualize using sets or categories
Step 3: Apply transitive property where applicable
Step 4: Check each conclusion
Step 5: Provide the final answer with justification

Answer:"""
        
        print(f"\n\nLogical Riddle:\n{riddle.strip()}")
        print("\nApplying logical reasoning...")
        result2 = self.call_model(prompt2, temperature=0.3)
        print(f"\n{result2}")
        
        self.results.append({
            "task": "logical_reasoning",
            "puzzle_type": "syllogism",
            "output": result2
        })
    
    def code_debugging(self):
        """Example 3: Code Debugging with Reasoning"""
        print("\n" + "="*70)
        print("EXAMPLE 3: CODE DEBUGGING")
        print("="*70)
        
        buggy_code = '''
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

# Test
scores = [85, 90, 78, 92, 88]
result = calculate_average(scores)
print(f"Average: {result}")

# This works fine, but what if we pass an empty list?
empty_scores = []
result2 = calculate_average(empty_scores)  # This will crash!
'''
        
        prompt = f"""Debug this code by analyzing it step by step.

Code:
{buggy_code}

Please debug this code using the following steps:

Step 1: Identify the bug (what will go wrong and when)
Step 2: Explain why this bug occurs (root cause analysis)
Step 3: Describe the potential consequences
Step 4: Propose a fix with explanation
Step 5: Provide the corrected code

Analysis:"""
        
        print(f"\nBuggy Code:\n{buggy_code}")
        print("\nDebugging step by step...")
        result = self.call_model(prompt, temperature=0.4)
        print(f"\n{result}")
        
        self.results.append({
            "task": "code_debugging",
            "language": "python",
            "output": result
        })
    
    def decision_making_analysis(self):
        """Example 4: Complex Decision Making"""
        print("\n" + "="*70)
        print("EXAMPLE 4: DECISION MAKING ANALYSIS")
        print("="*70)
        
        scenario = """
        You're a project manager deciding between two software development approaches:
        
        Option A: Monolithic Architecture
        - Faster initial development (3 months)
        - Lower upfront cost ($50,000)
        - Harder to scale later
        - Single point of failure
        - Team is familiar with this approach
        
        Option B: Microservices Architecture
        - Slower initial development (6 months)
        - Higher upfront cost ($120,000)
        - Easier to scale
        - More resilient
        - Team needs training (additional 2 weeks and $10,000)
        
        The project must launch within 8 months, and you have a budget of $150,000.
        The application is expected to grow 300% in users over the next 2 years.
        """
        
        prompt = f"""Analyze this decision systematically using step-by-step reasoning.

Scenario:
{scenario.strip()}

Let's analyze this decision thoroughly:

Step 1: Identify key constraints (time, budget, requirements)
Step 2: Evaluate Option A (pros, cons, risks)
Step 3: Evaluate Option B (pros, cons, risks)
Step 4: Consider short-term vs long-term implications
Step 5: Calculate total costs including hidden costs
Step 6: Assess risk factors
Step 7: Make a recommendation with justification

Analysis:"""
        
        print(f"\nScenario:\n{scenario.strip()}")
        print("\nAnalyzing decision step by step...")
        result = self.call_model(prompt, temperature=0.5, max_tokens=2048)
        print(f"\n{result}")
        
        self.results.append({
            "task": "decision_making",
            "domain": "software_architecture",
            "output": result
        })
    
    def scientific_reasoning(self):
        """Example 5: Scientific Hypothesis Testing"""
        print("\n" + "="*70)
        print("EXAMPLE 5: SCIENTIFIC REASONING")
        print("="*70)
        
        experiment = """
        Observation: Plants in the north-facing window of your house are growing slower 
        than plants in the south-facing window, even though you water them equally.
        
        Question: Why might this be happening, and how would you test your hypothesis?
        """
        
        prompt = f"""Apply scientific reasoning to explain this observation and design an experiment.

Observation:
{experiment.strip()}

Let's approach this scientifically:

Step 1: State the observation clearly
Step 2: Identify possible variables (what could cause this difference?)
Step 3: Form a hypothesis (what's your best explanation?)
Step 4: Design an experiment to test the hypothesis
Step 5: Predict expected results if hypothesis is correct
Step 6: Consider alternative explanations
Step 7: Describe how to analyze the results

Scientific Analysis:"""
        
        print(f"\nExperiment:\n{experiment.strip()}")
        print("\nApplying scientific method...")
        result = self.call_model(prompt, temperature=0.5)
        print(f"\n{result}")
        
        self.results.append({
            "task": "scientific_reasoning",
            "domain": "botany",
            "output": result
        })
    
    def business_strategy_analysis(self):
        """Example 6: Business Strategy Breakdown"""
        print("\n" + "="*70)
        print("EXAMPLE 6: BUSINESS STRATEGY ANALYSIS")
        print("="*70)
        
        situation = """
        A small coffee shop is facing increased competition from a new Starbucks opening 
        nearby. Current monthly revenue: $25,000. Profit margin: 20%. Regular customers: 150.
        
        The coffee shop is considering three strategies:
        1. Lower prices by 15% to compete
        2. Focus on specialty drinks and premium experience (20% price increase)
        3. Add lunch menu and extend hours (requires $15,000 investment)
        
        Question: Which strategy should they pursue and why?
        """
        
        prompt = f"""Analyze this business situation using strategic thinking and step-by-step reasoning.

Situation:
{situation.strip()}

Let's analyze this strategically:

Step 1: Assess current situation and key metrics
Step 2: Identify the core problem and competitive threat
Step 3: Analyze Strategy 1 (price reduction)
   - Impact on revenue and profit
   - Risks and benefits
Step 4: Analyze Strategy 2 (premium positioning)
   - Impact on revenue and profit
   - Risks and benefits
Step 5: Analyze Strategy 3 (menu expansion)
   - Impact on revenue and profit
   - Risks and benefits
Step 6: Consider market positioning and brand identity
Step 7: Make a recommendation with clear reasoning
Step 8: Suggest implementation steps

Strategic Analysis:"""
        
        print(f"\nBusiness Situation:\n{situation.strip()}")
        print("\nAnalyzing strategy step by step...")
        result = self.call_model(prompt, temperature=0.5, max_tokens=2048)
        print(f"\n{result}")
        
        self.results.append({
            "task": "business_strategy",
            "domain": "competitive_analysis",
            "output": result
        })
    
    def ethical_dilemma_reasoning(self):
        """Example 7: Ethical Reasoning"""
        print("\n" + "="*70)
        print("EXAMPLE 7: ETHICAL DILEMMA ANALYSIS")
        print("="*70)
        
        dilemma = """
        You're a software engineer at a social media company. You've discovered that 
        the algorithm prioritizes sensational/controversial content because it increases 
        engagement by 40%. However, research shows this is contributing to misinformation 
        spread and user anxiety. Your manager says engagement metrics are critical for 
        the company's upcoming funding round. What should you do?
        """
        
        prompt = f"""Analyze this ethical dilemma using structured moral reasoning.

Dilemma:
{dilemma.strip()}

Let's reason through this ethically:

Step 1: Identify all stakeholders and their interests
Step 2: Identify the ethical principles at stake
Step 3: Consider the consequences of each possible action
Step 4: Apply ethical frameworks:
   - Utilitarianism: Greatest good for greatest number?
   - Deontology: What are your duties and obligations?
   - Virtue Ethics: What would a virtuous person do?
Step 5: Consider long-term vs short-term implications
Step 6: Identify your sphere of influence and responsibility
Step 7: Propose a course of action with ethical justification

Ethical Analysis:"""
        
        print(f"\nEthical Dilemma:\n{dilemma.strip()}")
        print("\nReasoning through ethical considerations...")
        result = self.call_model(prompt, temperature=0.5, max_tokens=2048)
        print(f"\n{result}")
        
        self.results.append({
            "task": "ethical_reasoning",
            "domain": "technology_ethics",
            "output": result
        })
    
    def save_results(self):
        """Save all results to a JSON file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"chain_of_thought_results_{timestamp}.json"
        
        output_data = {
            "technique": "Chain of Thought Prompting",
            "model": self.model,
            "timestamp": timestamp,
            "total_tasks": len(self.results),
            "results": self.results
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n{'='*70}")
        print(f"Results saved to: {filename}")
        print(f"{'='*70}")
    
    def run_all_examples(self):
        """Execute all chain of thought prompting examples"""
        print("\n" + "="*70)
        print("CHAIN OF THOUGHT PROMPTING DEMONSTRATION")
        print("="*70)
        print("Model: " + self.model)
        print("="*70)
        
        try:
            self.math_word_problem()
            self.logical_reasoning()
            self.code_debugging()
            self.decision_making_analysis()
            self.scientific_reasoning()
            self.business_strategy_analysis()
            self.ethical_dilemma_reasoning()
            
            self.save_results()
            
            print("\n All examples completed successfully!")
            
        except Exception as e:
            print(f"\n Error occurred: {str(e)}")
            print("\nMake sure GROQ_API_KEY is set in your .env file")


def main():
    cot = ChainOfThoughtPrompting()
    cot.run_all_examples()


if __name__ == "__main__":
    main()