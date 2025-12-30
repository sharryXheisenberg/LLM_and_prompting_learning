"""
Zero-Shot Prompting Implementation
===================================
Direct task execution without providing examples to the model.
Best for: Simple, well-defined tasks where the instruction is clear.
"""

import os
from groq import Groq
from dotenv import load_dotenv
import json
from datetime import datetime

load_dotenv()

class ZeroShotPrompting:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.model = "llama-3.1-8b-instant"
        self.results = []
    
    def call_model(self, prompt: str, temperature: float = 0.7, max_tokens: int = 1024) -> str:
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
    
    def sentiment_analysis(self):
        """Example 1: Sentiment Analysis"""
        print("\n" + "="*70)
        print("EXAMPLE 1: SENTIMENT ANALYSIS")
        print("="*70)
        
        reviews = [
            "This product is absolutely amazing! Best purchase I've made all year.",
            "Terrible quality. Broke after 2 days. Complete waste of money.",
            "It's okay, does what it's supposed to do. Nothing extraordinary.",
            "The customer service was outstanding, but the product itself was mediocre.",
        ]
        
        for idx, review in enumerate(reviews, 1):
            prompt = f"""Analyze the sentiment of the following review and classify it as: Positive, Negative, or Neutral.
Also provide a confidence score (0-100) and a brief explanation.

Review: "{review}"

Provide your answer in this format:
Sentiment: [Your classification]
Confidence: [Score]
Explanation: [Brief explanation]"""
            
            print(f"\n--- Review {idx} ---")
            print(f"Text: {review}")
            result = self.call_model(prompt, temperature=0.3)
            print(f"\nAnalysis:\n{result}")
            
            self.results.append({
                "task": "sentiment_analysis",
                "input": review,
                "output": result
            })
    
    def text_summarization(self):
        """Example 2: Text Summarization"""
        print("\n" + "="*70)
        print("EXAMPLE 2: TEXT SUMMARIZATION")
        print("="*70)
        
        article = """
        Artificial Intelligence has made remarkable strides in recent years, transforming 
        industries from healthcare to finance. Machine learning algorithms can now diagnose 
        diseases with accuracy rivaling human doctors, while natural language processing 
        enables computers to understand and generate human-like text. The rise of large 
        language models has sparked both excitement and concern about AI's potential impact 
        on society. Companies are investing billions in AI research, racing to develop more 
        capable systems. However, experts warn about the need for responsible AI development, 
        emphasizing transparency, fairness, and safety. As AI continues to evolve, the balance 
        between innovation and ethical considerations remains a critical challenge for 
        researchers, policymakers, and society at large.
        """
        
        prompt = f"""Summarize the following article in 3 concise bullet points, 
capturing the main ideas:

Article:
{article.strip()}

Summary:"""
        
        print(f"\nOriginal Article ({len(article.split())} words):")
        print(article.strip())
        print("\n--- Generating Summary ---")
        result = self.call_model(prompt, temperature=0.5)
        print(f"\nSummary:\n{result}")
        
        self.results.append({
            "task": "text_summarization",
            "input": article.strip(),
            "output": result
        })
    
    def language_translation(self):
        """Example 3: Language Translation"""
        print("\n" + "="*70)
        print("EXAMPLE 3: LANGUAGE TRANSLATION")
        print("="*70)
        
        texts = [
            ("Hello, how are you today?", "Spanish"),
            ("I love learning new languages.", "French"),
            ("Technology is changing the world.", "German"),
        ]
        
        for idx, (text, target_lang) in enumerate(texts, 1):
            prompt = f"""Translate the following English text to {target_lang}.
Provide only the translation, nothing else.

English: "{text}"

{target_lang}:"""
            
            print(f"\n--- Translation {idx} ---")
            print(f"English: {text}")
            print(f"Target: {target_lang}")
            result = self.call_model(prompt, temperature=0.3)
            print(f"Translation: {result}")
            
            self.results.append({
                "task": "language_translation",
                "input": f"{text} -> {target_lang}",
                "output": result
            })
    
    def entity_extraction(self):
        """Example 4: Named Entity Recognition"""
        print("\n" + "="*70)
        print("EXAMPLE 4: ENTITY EXTRACTION")
        print("="*70)
        
        text = """
        Apple Inc. CEO Tim Cook announced the new iPhone 15 at the Steve Jobs Theater 
        in Cupertino, California on September 12, 2023. The device will be available 
        for $999 starting September 22nd. Cook mentioned that the phone features 
        significant improvements in camera technology and battery life, competing 
        directly with Samsung's Galaxy S23.
        """
        
        prompt = f"""Extract the following entities from the text:
- Organizations
- People
- Products
- Locations
- Dates
- Prices

Text:
{text.strip()}

Provide your answer in a structured format listing each category with the extracted entities."""
        
        print(f"\nText to analyze:")
        print(text.strip())
        print("\n--- Extracting Entities ---")
        result = self.call_model(prompt, temperature=0.2)
        print(f"\nExtracted Entities:\n{result}")
        
        self.results.append({
            "task": "entity_extraction",
            "input": text.strip(),
            "output": result
        })
    
    def question_answering(self):
        """Example 5: Question Answering"""
        print("\n" + "="*70)
        print("EXAMPLE 5: QUESTION ANSWERING")
        print("="*70)
        
        context = """
        The Great Wall of China is one of the most iconic structures in the world. 
        Construction began in the 7th century BC and continued for centuries, with 
        the most famous sections built during the Ming Dynasty (1368-1644). The wall 
        stretches approximately 13,170 miles (21,196 km) across northern China. It was 
        primarily built to protect Chinese states from invasions and raids. Today, it's 
        a UNESCO World Heritage site and attracts millions of tourists annually.
        """
        
        questions = [
            "When did construction of the Great Wall begin?",
            "How long is the Great Wall of China?",
            "What was the primary purpose of building the wall?",
            "Which dynasty built the most famous sections?"
        ]
        
        print(f"\nContext:")
        print(context.strip())
        
        for idx, question in enumerate(questions, 1):
            prompt = f"""Based on the following context, answer the question concisely and accurately.

Context:
{context.strip()}

Question: {question}

Answer:"""
            
            print(f"\n--- Question {idx} ---")
            print(f"Q: {question}")
            result = self.call_model(prompt, temperature=0.2)
            print(f"A: {result}")
            
            self.results.append({
                "task": "question_answering",
                "input": question,
                "output": result
            })
    
    def classification_task(self):
        """Example 6: Multi-class Classification"""
        print("\n" + "="*70)
        print("EXAMPLE 6: TOPIC CLASSIFICATION")
        print("="*70)
        
        articles = [
            "The Federal Reserve announced an interest rate hike of 0.25% to combat inflation.",
            "Scientists discovered a new exoplanet in the habitable zone of a distant star system.",
            "The championship game went into overtime, with the home team winning 28-24.",
            "New study shows that regular exercise can reduce the risk of heart disease by 30%.",
        ]
        
        categories = "Finance, Science, Sports, Health, Technology, Politics"
        
        for idx, article in enumerate(articles, 1):
            prompt = f"""Classify the following article into one of these categories: {categories}

Article: "{article}"

Category:"""
            
            print(f"\n--- Article {idx} ---")
            print(f"Text: {article}")
            result = self.call_model(prompt, temperature=0.2)
            print(f"Category: {result}")
            
            self.results.append({
                "task": "classification",
                "input": article,
                "output": result
            })
    
    def save_results(self):
        """Save all results to a JSON file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"zero_shot_results_{timestamp}.json"
        
        output_data = {
            "technique": "Zero-Shot Prompting",
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
        """Execute all zero-shot prompting examples"""
        print("\n" + "="*70)
        print("ZERO-SHOT PROMPTING DEMONSTRATION")
        print("="*70)
        print("Model: " + self.model)
        print("="*70)
        
        try:
            self.sentiment_analysis()
            self.text_summarization()
            self.language_translation()
            self.entity_extraction()
            self.question_answering()
            self.classification_task()
            
            self.save_results()
            
            print("\n All examples completed successfully!")
            
        except Exception as e:
            print(f"\n Error occurred: {str(e)}")
            print("\nMake sure:")
            print("1. You have set GROQ_API_KEY in your .env file")
            print("2. You have installed required packages: pip install groq python-dotenv")


def main():
    zero_shot = ZeroShotPrompting()
    zero_shot.run_all_examples()


if __name__ == "__main__":
    main()