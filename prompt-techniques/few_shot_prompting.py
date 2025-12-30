"""
Few-Shot Prompting Implementation
==================================
Provides examples to guide the model's behavior and output format.
Best for: Tasks requiring specific formats, styles, or pattern recognition.
"""

import os
from groq import Groq
from dotenv import load_dotenv
import json
from datetime import datetime

load_dotenv()

class FewShotPrompting:
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
    
    def sentiment_classification_with_examples(self):
        """Example 1: Sentiment Analysis with Few-Shot Learning"""
        print("\n" + "="*70)
        print("EXAMPLE 1: SENTIMENT CLASSIFICATION (FEW-SHOT)")
        print("="*70)
        
        prompt = """Classify the sentiment of customer reviews as: Positive, Negative, or Neutral.

Examples:

Review: "This laptop exceeded all my expectations! Fast, reliable, and great battery life."
Sentiment: Positive

Review: "Completely disappointed. The product stopped working after a week."
Sentiment: Negative

Review: "It's decent. Does the job but nothing impressive."
Sentiment: Neutral

Review: "Amazing customer service! They resolved my issue within minutes."
Sentiment: Positive

Review: "The quality is poor and it's overpriced. Not worth it at all."
Sentiment: Negative

Now classify these new reviews:

Review: "The design is sleek and modern. I'm very satisfied with this purchase."
Sentiment:"""
        
        print("\nPrompt structure: Provided 5 examples before asking for classification")
        print("\n--- Testing New Review ---")
        result = self.call_model(prompt, temperature=0.3)
        print(f"Result: {result}")
        
        self.results.append({
            "task": "sentiment_classification",
            "examples_provided": 5,
            "output": result
        })
        
        # Test multiple new reviews
        test_reviews = [
            "Broke on the first day. Absolutely terrible.",
            "It works fine, no complaints but nothing special either.",
            "Best investment ever! Highly recommend to everyone!"
        ]
        
        for idx, review in enumerate(test_reviews, 1):
            test_prompt = prompt.rsplit("Review:", 1)[0] + f"\nReview: \"{review}\"\nSentiment:"
            print(f"\n--- Test Review {idx} ---")
            print(f"Input: {review}")
            result = self.call_model(test_prompt, temperature=0.3)
            print(f"Output: {result}")
            
            self.results.append({
                "task": "sentiment_classification",
                "input": review,
                "output": result
            })
    
    def email_response_generation(self):
        """Example 2: Professional Email Response Generation"""
        print("\n" + "="*70)
        print("EXAMPLE 2: EMAIL RESPONSE GENERATION")
        print("="*70)
        
        prompt = """Generate professional email responses based on the customer inquiry.

Example 1:
Customer: "Hi, I haven't received my order yet. It's been 10 days."
Response: "Dear Customer,

Thank you for reaching out. I sincerely apologize for the delay in your order delivery. I've checked your order status and will prioritize this issue immediately. I'll update you within 24 hours with the tracking information and expected delivery date.

We appreciate your patience.

Best regards,
Customer Support Team"

Example 2:
Customer: "The product I received is defective. What should I do?"
Response: "Dear Customer,

I'm sorry to hear about the defective product. We take quality seriously and want to make this right. Please reply with your order number and photos of the defect. We'll process a replacement or full refund immediately, whichever you prefer.

Thank you for bringing this to our attention.

Best regards,
Customer Support Team"

Example 3:
Customer: "Can I change my shipping address? My order hasn't shipped yet."
Response: "Dear Customer,

Thank you for contacting us. I'd be happy to help update your shipping address. Since your order hasn't shipped yet, we can make this change. Please provide the new complete shipping address, and I'll update it right away.

Thanks for letting us know promptly!

Best regards,
Customer Support Team"

Now generate a response for this customer inquiry:

Customer: "I need to cancel my subscription. How do I do that?"
Response:"""
        
        print("\nProviding 3 email response examples as templates...")
        result = self.call_model(prompt, temperature=0.6)
        print(f"\nGenerated Response:\n{result}")
        
        self.results.append({
            "task": "email_generation",
            "examples_provided": 3,
            "output": result
        })
    
    def code_pattern_completion(self):
        """Example 3: Code Generation with Pattern Learning"""
        print("\n" + "="*70)
        print("EXAMPLE 3: CODE PATTERN COMPLETION")
        print("="*70)
        
        prompt = """Complete the Python function following the pattern shown in examples:

Example 1:
# Function: Calculate factorial
def factorial(n):
    \"\"\"Calculate factorial of n\"\"\"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

Example 2:
# Function: Check if string is palindrome
def is_palindrome(s):
    \"\"\"Check if string is palindrome\"\"\"
    s = s.lower().replace(" ", "")
    return s == s[::-1]

Example 3:
# Function: Find maximum in list
def find_max(lst):
    \"\"\"Find maximum element in list\"\"\"
    if not lst:
        return None
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val

Now complete this function:

# Function: Calculate fibonacci number
def fibonacci(n):
    \"\"\"Calculate nth fibonacci number\"\"\""""
        
        print("\nLearning from 3 code examples...")
        result = self.call_model(prompt, temperature=0.4)
        print(f"\nGenerated Code:\n{result}")
        
        self.results.append({
            "task": "code_generation",
            "pattern": "function_completion",
            "output": result
        })
    
    def product_description_writing(self):
        """Example 4: Product Description in Specific Style"""
        print("\n" + "="*70)
        print("EXAMPLE 4: PRODUCT DESCRIPTION WRITING")
        print("="*70)
        
        prompt = """Write engaging product descriptions following this style:

Example 1:
Product: Wireless Earbuds
Description: "Experience freedom like never before. These ultra-lightweight wireless earbuds deliver crystal-clear sound quality with deep bass that'll make your favorite songs come alive. With 24-hour battery life and IPX7 waterproof rating, they're perfect for your active lifestyle. Touch controls make switching songs effortless. Your soundtrack, untethered."

Example 2:
Product: Smart Watch
Description: "Your health companion on your wrist. This sleek smartwatch tracks your heart rate, sleep patterns, and activity levels with precision. Stay connected with notifications, calls, and apps right from your wrist. The vibrant AMOLED display looks stunning, while the 7-day battery life keeps you going. Fitness meets fashion."

Example 3:
Product: Portable Blender
Description: "Smoothies anywhere, anytime. This compact powerhouse blends fruits, vegetables, and ice into silky perfection in just 30 seconds. USB rechargeable design means no outlets needed. The BPA-free bottle doubles as your drinking cup. Healthy living just got easier. Blend, sip, conquer."

Now write a description for this product:

Product: Laptop Stand
Description:"""
        
        print("\nLearning writing style from 3 examples...")
        result = self.call_model(prompt, temperature=0.7)
        print(f"\nGenerated Description:\n{result}")
        
        self.results.append({
            "task": "product_description",
            "style": "engaging_lifestyle",
            "output": result
        })
        
        # Generate more descriptions
        products = [
            "Mechanical Keyboard",
            "Desk Lamp",
            "Water Bottle"
        ]
        
        for product in products:
            test_prompt = prompt.rsplit("Product:", 1)[0] + f"\nProduct: {product}\nDescription:"
            print(f"\n--- Generating for {product} ---")
            result = self.call_model(test_prompt, temperature=0.7)
            print(f"Result: {result}")
            
            self.results.append({
                "task": "product_description",
                "product": product,
                "output": result
            })
    
    def data_extraction_structured(self):
        """Example 5: Structured Data Extraction"""
        print("\n" + "="*70)
        print("EXAMPLE 5: STRUCTURED DATA EXTRACTION")
        print("="*70)
        
        prompt = """Extract key information from job postings and format as JSON.

Example 1:
Job Posting: "Senior Software Engineer needed at TechCorp in San Francisco. 5+ years experience with Python and AWS required. Salary: $150k-$180k. Remote work available."
Output: {
  "title": "Senior Software Engineer",
  "company": "TechCorp",
  "location": "San Francisco",
  "experience": "5+ years",
  "skills": ["Python", "AWS"],
  "salary": "$150k-$180k",
  "remote": true
}

Example 2:
Job Posting: "Marketing Manager position at BrandCo in New York. Must have 3 years in digital marketing and social media. Competitive salary. On-site only."
Output: {
  "title": "Marketing Manager",
  "company": "BrandCo",
  "location": "New York",
  "experience": "3 years",
  "skills": ["Digital Marketing", "Social Media"],
  "salary": "Competitive",
  "remote": false
}

Example 3:
Job Posting: "Junior Data Analyst at DataWorks in Austin. Looking for someone with SQL and Excel skills. Entry level welcome. $60k-$75k. Hybrid work model."
Output: {
  "title": "Junior Data Analyst",
  "company": "DataWorks",
  "location": "Austin",
  "experience": "Entry level",
  "skills": ["SQL", "Excel"],
  "salary": "$60k-$75k",
  "remote": "hybrid"
}

Now extract from this job posting:

Job Posting: "Full Stack Developer at StartupXYZ in Seattle. Need expertise in React, Node.js, and MongoDB. 4+ years required. $120k-$140k. Fully remote position."
Output:"""
        
        print("\nExtracting structured data using 3 examples as templates...")
        result = self.call_model(prompt, temperature=0.2)
        print(f"\nExtracted Data:\n{result}")
        
        self.results.append({
            "task": "data_extraction",
            "format": "json",
            "output": result
        })
    
    def creative_story_continuation(self):
        """Example 6: Creative Writing Style Learning"""
        print("\n" + "="*70)
        print("EXAMPLE 6: CREATIVE STORY CONTINUATION")
        print("="*70)
        
        prompt = """Continue the story in the same narrative style:

Example 1:
Beginning: "The old clock struck midnight."
Continuation: "Its chimes echoed through the empty mansion, each toll a reminder of time slipping away. Sarah clutched the dusty letter tighter, her hands trembling not from the cold, but from what she'd just discovered about her grandfather's past."

Example 2:
Beginning: "The spaceship's alarm blared."
Continuation: "Red lights pulsed across the cockpit as Captain Morrison's fingers flew over the controls. Asteroid field ahead, fuel running low, and backup systems failing. She'd trained for this scenario a hundred times, but training simulations never captured the raw taste of fear."

Example 3:
Beginning: "The cafe was unusually quiet today."
Continuation: "Steam rose lazily from untouched coffee cups as patrons stared at their phones in shocked silence. The news had broken minutes ago, and nobody quite knew how to process it. Maria set down her notepad, realizing she wasn't going to serve anyone anytime soon."

Now continue this story:

Beginning: "The forest path disappeared behind them."
Continuation:"""
        
        print("\nLearning narrative style from examples...")
        result = self.call_model(prompt, temperature=0.8)
        print(f"\nStory Continuation:\n{result}")
        
        self.results.append({
            "task": "creative_writing",
            "style": "narrative_continuation",
            "output": result
        })
    
    def save_results(self):
        """Save all results to a JSON file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"few_shot_results_{timestamp}.json"
        
        output_data = {
            "technique": "Few-Shot Prompting",
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
        """Execute all few-shot prompting examples"""
        print("\n" + "="*70)
        print("FEW-SHOT PROMPTING DEMONSTRATION")
        print("="*70)
        print("Model: " + self.model)
        print("="*70)
        
        try:
            self.sentiment_classification_with_examples()
            self.email_response_generation()
            self.code_pattern_completion()
            self.product_description_writing()
            self.data_extraction_structured()
            self.creative_story_continuation()
            
            self.save_results()
            
            print("\n All examples completed successfully!")
            
        except Exception as e:
            print(f"\n Error occurred: {str(e)}")
            print("\nMake sure GROQ_API_KEY is set in your .env file")


def main():
    few_shot = FewShotPrompting()
    few_shot.run_all_examples()


if __name__ == "__main__":
    main()