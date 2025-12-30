### Prompting Techniques 

#### **1.Zero-shot Prompting** 
- Zero-shot prompting means that the prompt used to interact with the model won't contain examples or demonstrations. The zero-shot prompt directly instructs the model to perform a task without any additional examples to steer it.

- **Prompt:**
```bash 
Classify the text into neutral, negative or positive. 
Text: I think the vacation is okay.
Sentiment:
```
- **Output:**
```bash
Neutral
```

#### **2.Few-Shot Prompting**
- While large-language models demonstrate remarkable zero-shot capabilities, they still fall short on more complex tasks when using the zero-shot setting. Few-shot prompting can be used as a technique to enable in-context learning where we provide demonstrations in the prompt to steer the model to better performance.

**Limitations of Few-shot Prompting**
- Standard few-shot prompting works well for many tasks but is still not a perfect technique, especially when dealing with more complex reasoning tasks. Let's demonstrate why this is the case. Do you recall the previous example where we provided the following task:
-Few-shot prompting is not enough to get reliable responses for reasoning problem.

#### **3.Chain-of-Thought Prompting**
Chain-of-thought (CoT) prompting enables complex reasoning capabilities through intermediate reasoning steps. You can combine it with few-shot prompting to get better results on more complex tasks that require reasoning before responding.

- **Zero-shot COT Prompting** 
The idea of zero-shot CoT  that essentially involves adding "Let's think step by step" to the original prompt.

- **Prompt:**
```bash
I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?
```
- **Output:**
```bash 
11 apples
```
- This is incorrect But we can optimize the the prompt to get the special prompt

- **Tweaked prompt**
```bash
I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?
Let's think step by step.
```

- **Output**
```bash
First, you started with 10 apples.
You gave away 2 apples to the neighbor and 2 to the repairman, so you had 6 apples left.
Then you bought 5 more apples, so now you had 11 apples.
Finally, you ate 1 apple, so you would remain with 10 apples.
```
##### **Automatic Chain-of-Thought (Auto-CoT)**
This work proposes Auto-CoT, which samples questions with diversity and generates reasoning chains to construct the demonstrations.
Auto-CoT consists of two main stages:
- Stage **1.question clustering:** partition questions of a given dataset into a few clusters.
- Stage **2: demonstration sampling:** select a representative question from each cluster and generate its reasoning chain using Zero-Shot-CoT with simple heuristics.

#### **4.Prompt Chaining**
To improve the reliability and performance of LLMs, one of the important prompt engineering techniques is to break tasks into its subtasks. Once those subtasks have been identified, the LLM is prompted with a subtask and then its response is used as input to another prompt. This is what's referred to as prompt chaining, where a task is split into subtasks with the idea to create a chain of prompt operations.
Prompt chaining is useful to accomplish complex tasks which an LLM might struggle to address if prompted with a very detailed prompt. In prompt chaining, chain prompts perform transformations or additional processes on the generated responses before reaching a final desired state.
Besides achieving better performance, prompt chaining helps to boost the transparency of your LLM application, increases controllability, and reliability. This means that you can debug problems with model responses much more easily and analyze and improve performance in the different stages that need improvement.Prompt chaining is particularly useful when building LLM-powered conversational assistants and improving the personalization and user experience of your applications.

#### **Results of each technique with llama-3.1-8b-instant**

- **1.zero_shot_prompting**
```bash
ZERO-SHOT PROMPTING DEMONSTRATION
======================================================================
Model: llama-3.1-8b-instant
======================================================================

======================================================================
EXAMPLE 1: SENTIMENT ANALYSIS
======================================================================

--- Review 1 ---
Text: This product is absolutely amazing! Best purchase I've made all year.

Analysis:
Sentiment: Positive
Confidence: 100
Explanation: The review uses superlatives such as "absolutely amazing" and "best purchase," indicating a very strong positive sentiment. The language used is enthusiastic and unambivalent, suggesting a high level of confidence in the classification.

--- Review 2 ---
Text: Terrible quality. Broke after 2 days. Complete waste of money.

Analysis:
Sentiment: Negative
Confidence: 100
Explanation: The review explicitly states "Terrible quality" and "Complete waste of money," which are strong negative indicators. Additionally, the product broke after only 2 days, further emphasizing the reviewer's dissatisfaction. The language used is straightforward and critical, leaving no doubt about the reviewer's sentiment.

--- Review 3 ---
Text: It's okay, does what it's supposed to do. Nothing extraordinary.

Analysis:
Sentiment: Neutral
Confidence: 80
Explanation: The review states that the product "does what it's supposed to do," which implies a level of satisfaction with its functionality. However, the phrase "nothing extraordinary" suggests that the product lacks exceptional qualities or features, leading to a neutral overall sentiment. The confidence score is 80 because the review is straightforward and lacks strong emotional language, making it difficult to classify as strongly positive or negative.

--- Review 4 ---
Text: The customer service was outstanding, but the product itself was mediocre.

Analysis:
Sentiment: Mixed
Confidence: 80
Explanation: The review starts with a positive statement about the customer service, which suggests that the reviewer was impressed with the company's support. However, the second part of the review states that the product itself was "mediocre," which is a neutral to slightly negative assessment. This mixed sentiment makes it difficult to classify the review as purely positive or negative, hence the classification as "Mixed."

======================================================================
EXAMPLE 2: TEXT SUMMARIZATION
======================================================================

Original Article (108 words):
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

--- Generating Summary ---

Summary:
Here are 3 concise bullet points summarizing the article:

• Artificial Intelligence has made significant progress in various industries, including healthcare and finance, with machine learning algorithms achieving human-like accuracy in disease diagnosis and natural language processing enabling human-like text generation.
• The rapid development of large language models has sparked both excitement and concern about AI's potential impact on society, highlighting the need for responsible AI development.
• Experts emphasize the importance of balancing innovation with ethical considerations, such as transparency, fairness, and safety, to ensure that AI development aligns with societal values and benefits.

======================================================================
EXAMPLE 3: LANGUAGE TRANSLATION
======================================================================

--- Translation 1 ---
English: Hello, how are you today?
Target: Spanish
Translation: "Hola, ¿cómo estás hoy?"

--- Translation 2 ---
English: I love learning new languages.
Target: French
Translation: "J'adore apprendre de nouvelles langues."

--- Translation 3 ---
English: Technology is changing the world.
Target: German
Translation: "Die Technologie verändert die Welt."

======================================================================
EXAMPLE 4: ENTITY EXTRACTION
======================================================================

Text to analyze:
Apple Inc. CEO Tim Cook announced the new iPhone 15 at the Steve Jobs Theater
        in Cupertino, California on September 12, 2023. The device will be available
        for $999 starting September 22nd. Cook mentioned that the phone features
        significant improvements in camera technology and battery life, competing
        directly with Samsung's Galaxy S23.

--- Extracting Entities ---

Extracted Entities:
Here's the extracted entities in a structured format:

**Organizations:**
1. Apple Inc.
2. Samsung

**People:**
1. Tim Cook

**Products:**
1. iPhone 15
2. Galaxy S23

**Locations:**
1. Steve Jobs Theater
2. Cupertino, California

**Dates:**
1. September 12, 2023
2. September 22nd

**Prices:**
1. $999

======================================================================
EXAMPLE 5: QUESTION ANSWERING
======================================================================

Context:
The Great Wall of China is one of the most iconic structures in the world.
        Construction began in the 7th century BC and continued for centuries, with
        the most famous sections built during the Ming Dynasty (1368-1644). The wall
        stretches approximately 13,170 miles (21,196 km) across northern China. It was
        primarily built to protect Chinese states from invasions and raids. Today, it's
        a UNESCO World Heritage site and attracts millions of tourists annually.

--- Question 1 ---
Q: When did construction of the Great Wall begin?
A: Construction of the Great Wall began in the 7th century BC.

--- Question 2 ---
Q: How long is the Great Wall of China?
A: Approximately 13,170 miles (21,196 km).

--- Question 3 ---
Q: What was the primary purpose of building the wall?
A: The primary purpose of building the Great Wall of China was to protect Chinese states from invasions and raids.

--- Question 4 ---
Q: Which dynasty built the most famous sections?
A: The Ming Dynasty (1368-1644) built the most famous sections of the Great Wall of China.

======================================================================
EXAMPLE 6: TOPIC CLASSIFICATION
======================================================================

--- Article 1 ---
Text: The Federal Reserve announced an interest rate hike of 0.25% to combat inflation.
Category: Finance. 

This article is related to the Federal Reserve, which is a central banking system, and the announcement of an interest rate hike, which is a monetary policy decision. This suggests that the article is about finance and economics.

--- Article 2 ---
Text: Scientists discovered a new exoplanet in the habitable zone of a distant star system.
Category: Category: Science

--- Article 3 ---
--- Article 3 ---
Text: The championship game went into overtime, with the home team winning 28-24.
Category: Category: Sports.

--- Article 4 ---
--- Article 3 ---
Text: The championship game went into overtime, with the home team winning 28-24.
Category: Category: Sports.

--- Article 4 ---
--- Article 3 ---
Text: The championship game went into overtime, with the home team winning 28-24.
Category: Category: Sports.
--- Article 3 ---
--- Article 3 ---
Text: The championship game went into overtime, with the home team winning 28-24.
Category: Category: Sports.

--- Article 4 ---
Text: New study shows that regular exercise can reduce the risk of heart disease by 30%.
Category: The category for the given article is: Health.
```


- **2.few_shot_prompting**
```bash 
======================================================================
FEW-SHOT PROMPTING DEMONSTRATION
======================================================================
Model: llama-3.1-8b-instant
======================================================================

======================================================================
EXAMPLE 1: SENTIMENT CLASSIFICATION (FEW-SHOT)
======================================================================

Prompt structure: Provided 5 examples before asking for classification

--- Testing New Review ---
Result: Sentiment: Positive

The review mentions that the design is "sleek and modern" and the customer is "very satisfied," indicating a positive experience.

--- Test Review 1 ---
Input: Broke on the first day. Absolutely terrible.
Output: Sentiment: Negative

The review mentions that the product "Broke on the first day" which indicates a negative experience, and the word "terrible" further emphasizes the negative sentiment.

--- Test Review 2 ---
Input: It works fine, no complaints but nothing special either.
Output: Sentiment: Neutral

The review states that the product works fine and there are no complaints, but it also mentions that it's nothing special. This indicates a neutral sentiment, as the reviewer is neither extremely satisfied nor dissatisfied.

--- Test Review 3 ---
Input: Best investment ever! Highly recommend to everyone!
Output: Sentiment: Positive

The review uses positive language such as "Best investment ever" and "Highly recommend," indicating a very positive sentiment.

======================================================================
EXAMPLE 2: EMAIL RESPONSE GENERATION
======================================================================

Providing 3 email response examples as templates...

Generated Response:
Customer Inquiry Response:

"Dear Customer,

Thank you for reaching out. I'm happy to assist you with canceling your subscription. Please note that cancellations must be processed before the next billing cycle to avoid any further charges.

To cancel your subscription, please reply with your subscription order number or the name associated with the account. Alternatively, you can log in to your account on our website and follow the cancellation instructions. If you need assistance with the process, I'll be happy to guide you through it.

Please let me know how I can further assist you.

Best regards,
Customer Support Team"

======================================================================
EXAMPLE 3: CODE PATTERN COMPLETION
======================================================================

Learning from 3 code examples...

Generated Code:
Here's the completed Python function to calculate the nth Fibonacci number:

python
def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


However, this function has a time complexity of O(2^n) due to the repeated calculations involved in the recursive calls. This can be optimized using memoization or dynamic programming to achieve a time complexity of O(n).

Here's the optimized version:

python
def fibonacci(n, memo = {}):
    """Calculate nth Fibonacci number"""
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        memo[n] = result
        return result


In this version, we store the Fibonacci numbers as we calculate them in a dictionary called `memo`. Before calculating a Fibonacci number, we check if it's already in `memo`. If it is, we return the stored value instead of recalculating it.

Alternatively, you can use a loop to calculate the Fibonacci numbers in O(n) time complexity:

python
def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib_prev = 0
    fib_curr = 1
    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next
    return fib_curr


This version uses a loop to calculate the Fibonacci numbers iteratively, avoiding the repeated calculations involved in the recursive calls.

======================================================================
EXAMPLE 4: PRODUCT DESCRIPTION WRITING
======================================================================

Learning writing style from 3 examples...

Generated Description:
Product: Laptop Stand
Description: "Elevate your workspace, elevate your productivity. Our laptop stand is designed to help you work in comfort and style. With a sturdy metal construction and adjustable height settings, you can customize your setup to fit your needs. The sleek, compact design won't take up too much space, making it perfect for home offices, coffee shops, or co-working spaces. Say goodbye to hunching over your laptop and hello to improved posture and reduced eye strain. Upgrade your workspace, upgrade your workflow."

--- Generating for Mechanical Keyboard ---
Result: Product: Mechanical Keyboard
Description: "Unleash your typing potential. This high-performance mechanical keyboard is designed for gamers, coders, and writers who demand precision and speed. With customizable switches, 1000Hz polling rate, and N-key rollover, every keystroke is registered with accuracy. The compact tenkeyless design and sleek aluminum frame add a touch of elegance to your workspace. Type like a pro, perform like a champion."   

--- Generating for Desk Lamp ---
Result: Product: Desk Lamp
Description: "Illuminate your workspace with precision and style. This sleek desk lamp casts a warm, ambient light that perfectly complements your home office or study space. With adjustable arm and tilt control, you can direct the light exactly where you need it. An energy-efficient LED bulb and long-lasting 10-year lifespan ensure years of reliable performance. Work, read, or create under the perfect glow."        

--- Generating for Water Bottle ---
Result: Product: Water Bottle
Description: "Hydrate the smart way. This refillable water bottle is designed to keep you refreshed on-the-go. Made from BPA-free, durable materials, it's built to withstand the rigors of your active lifestyle. Double-walled insulation keeps drinks hot or cold for hours. The sleek design and interchangeable caps mean you can personalize your hydration experience. Drink up, live more."

======================================================================
EXAMPLE 5: STRUCTURED DATA EXTRACTION
======================================================================

Extracting structured data using 3 examples as templates...

Extracted Data:
Here's the extracted information in JSON format:

{
  "title": "Full Stack Developer",
  "company": "StartupXYZ",
  "location": "Seattle",
  "experience": "4+ years",
  "skills": ["React", "Node.js", "MongoDB"],
  "salary": "$120k-$140k",
  "remote": true
}

======================================================================
EXAMPLE 6: CREATIVE STORY CONTINUATION
======================================================================

Learning narrative style from examples...

Story Continuation:
"The forest path disappeared behind them, leaving only the faint rustle of dry leaves and the faint scent of damp earth. Emily slowed her pace, her eyes locked on the fading trees as the landscape shifted to a more open, rolling terrain. She couldn't shake the feeling they were being herded towards something, but James's hand on her shoulder only tightened his grip on the backpack, a sign that he was just as uncertain as she was.

The sun beat down on them, relentless in its intensity, yet Emily felt a chill run down her spine as she caught a glimpse of their trail behind them. The trees seemed to close in, their branches twisted and gnarled, as if trying to snare them in some ancient, supernatural trap. She spun around, but there was nothing to see, just the quiet, oppressive stillness of the wilderness. James tugged her forward, and she followed, her heart pounding in her chest, as they vanished into the unknown."
```



- **3.Chain_of_thought_prompting**
```bash 
======================================================================
CHAIN OF THOUGHT PROMPTING DEMONSTRATION
======================================================================
Model: llama-3.1-8b-instant
======================================================================

======================================================================
EXAMPLE 1: MATH WORD PROBLEMS
======================================================================

--- Problem 1 (Easy) ---
Problem: A store sells apples for $3 per pound and oranges for $2 per pound. If John buys 4 pounds of apples and 6 pounds of oranges, and he pays with a $50 bill, how much change will he get back?

Solving step by step...

Let's solve the problem step by step.

**Step 1: Identify what we know**

- The price of apples is $3 per pound.
- The price of oranges is $2 per pound.
- John buys 4 pounds of apples.
- John buys 6 pounds of oranges.
- John pays with a $50 bill.

**Step 2: Determine what we need to find**

We need to find out how much change John will get back after paying for the apples and oranges.

**Step 3: Set up the calculation**

To find the total cost of the apples and oranges, we need to multiply the price per pound by the number of pounds for each fruit.

- Total cost of apples: 4 pounds * $3/pound = $12
- Total cost of oranges: 6 pounds * $2/pound = $12
- Total cost of both fruits: $12 (apples) + $12 (oranges) = $24

**Step 4: Solve**

Now that we know the total cost of the fruits, we can find the change by subtracting the total cost from the amount John paid with.

- Change = Amount paid - Total cost
- Change = $50 - $24
- Change = $26

**Step 5: Verify the answer**

To verify the answer, we can check if the calculation is correct.

- Total cost of apples: 4 pounds * $3/pound = $12
- Total cost of oranges: 6 pounds * $2/pound = $12
- Total cost of both fruits: $12 + $12 = $24
- Change: $50 - $24 = $26

The calculation is correct, and John will get $26 in change.

--- Problem 2 (Medium) ---
Problem: A train travels at 60 mph for 2 hours, then increases its speed to 80 mph for the next 3 hours. What is the total distance traveled?

Solving step by step...

Let's solve the problem step by step.

**Step 1: Identify what we know**

- The train travels at 60 mph for 2 hours.
- The train then increases its speed to 80 mph for the next 3 hours.
- The speed of the train is constant during each time period.

**Step 2: Determine what we need to find**

- We need to find the total distance traveled by the train.

**Step 3: Set up the calculation**

To find the total distance traveled, we need to calculate the distance traveled during each time period and add them together.

Distance = Speed x Time

For the first time period (60 mph for 2 hours):
Distance1 = 60 mph x 2 hours = 120 miles

For the second time period (80 mph for 3 hours):
Distance2 = 80 mph x 3 hours = 240 miles

**Step 4: Solve**

The total distance traveled is the sum of the distances traveled during each time period:
Total Distance = Distance1 + Distance2
= 120 miles + 240 miles
= 360 miles

**Step 5: Verify the answer**

To verify the answer, we can check if it makes sense in the context of the problem. The train travels at 60 mph for 2 hours, which is a total of 120 miles. Then, it increases its speed to 80 mph for the next 3 hours, which is a total of 240 miles. Adding these two distances together, we get 120 miles + 240 miles = 360 miles, which matches our answer.

Therefore, the total distance traveled by the train is 360 miles.

--- Problem 3 (Medium) ---
Problem: In a class of 40 students, 60% are girls. If 25% of the girls and 40% of the boys wear glasses, how many students in total wear glasses?

Solving step by step...

Let's break down the solution step by step.

**Step 1: Identify what we know**

- Total number of students in the class: 40
- Percentage of girls in the class: 60%
- Percentage of boys in the class: 40% (since the remaining percentage is boys)
- Percentage of girls who wear glasses: 25%
- Percentage of boys who wear glasses: 40%

**Step 2: Determine what we need to find**

We need to find the total number of students who wear glasses.

**Step 3: Set up the calculation**

First, let's find the number of girls and boys in the class:

- Number of girls: 60% of 40 = 0.6 * 40 = 24
- Number of boys: 40% of 40 = 0.4 * 40 = 16

Next, let's find the number of girls and boys who wear glasses:

- Number of girls who wear glasses: 25% of 24 = 0.25 * 24 = 6
- Number of boys who wear glasses: 40% of 16 = 0.4 * 16 = 6.4

**Step 4: Solve**

Now, let's find the total number of students who wear glasses by adding the number of girls and boys who wear glasses:

Total number of students who wear glasses = Number of girls who wear glasses + Number of boys who wear glasses
= 6 + 6.4
= 12.4

Since we can't have a fraction of a student, we'll round up to the nearest whole number (because you can't have a fraction of a person). However, in this case, we will keep the answer as a decimal for accuracy.

**Step 5: Verify the answer**

To verify our answer, let's check if it makes sense:

- We know that the total number of students is 40.
- We also know that the percentage of girls who wear glasses is 25% and the percentage of boys who wear glasses is 40%.
- If we calculate the total number of students who wear glasses using these percentages, we should get the same answer.

Let's calculate the total number of students who wear glasses using the percentages:

Total number of students who wear glasses = (25% of 24) + (40% of 16)
= 0.25 * 24 + 0.4 * 16
= 6 + 6.4
= 12.4

Our answer is correct.

Therefore, the total number of students who wear glasses is approximately 12.4.

======================================================================
EXAMPLE 2: LOGICAL REASONING
======================================================================

Puzzle:
Five friends - Alice, Bob, Carol, David, and Emma - are sitting in a row.
        - Alice is not at either end
        - Bob is sitting next to Alice
        - Carol is sitting at one of the ends
        - David is not sitting next to Carol
        - Emma is sitting between two people

        Question: What is the order of people from left to right?

Reasoning through the puzzle...

Let's solve the puzzle step by step.

**Step 1: List all the constraints**

1. Alice is not at either end.
2. Bob is sitting next to Alice.
3. Carol is sitting at one of the ends.
4. David is not sitting next to Carol.
5. Emma is sitting between two people.

**Step 2: Start with definite positions (Carol is at an end)**

Since Carol is at one of the ends, we have two possibilities:

- Carol is at the left end: C _ _ _ _
- Carol is at the right end: _ _ _ _ C

**Step 3: Apply each constraint one by one**

Let's start with the first possibility: Carol is at the left end.

- Alice is not at either end, so she can be in the second, third, or fourth position.
- Bob is sitting next to Alice, so if Alice is in the second position, Bob must be in the first position. If Alice is in the third position, Bob must be in the second position. If Alice is in the fourth position, Bob must be in the third position.

Now, let's consider the second possibility: Carol is at the right end.

- Alice is not at either end, so she can be in the second, third, or fourth position.
- Bob is sitting next to Alice, so if Alice is in the second position, Bob must be in the first position. If Alice is in the third position, Bob must be in the second position. If Alice is in the fourth position, Bob must be in the third position.

**Step 4: Eliminate impossible arrangements**

Let's analyze the possibilities:

- Carol is at the left end:
  - If Alice is in the second position, Bob is in the first position, and we have: B A _ _ C.
  - If Alice is in the third position, Bob is in the second position, and we have: B _ A _ C.
  - If Alice is in the fourth position, Bob is in the third position, and we have: B _ _ A C.
- Carol is at the right end:
  - If Alice is in the second position, Bob is in the first position, and we have: B A _ _ C.
  - If Alice is in the third position, Bob is in the second position, and we have: _ A B _ C.
  - If Alice is in the fourth position, Bob is in the third position, and we have: _ _ B A C.

Now, let's apply the constraint that David is not sitting next to Carol. We can eliminate the following possibilities:

- Carol is at the left end: B A _ _ C (David is next to Carol)
- Carol is at the right end: B A _ _ C (David is next to Carol)

The remaining possibilities are:

- Carol is at the left end: B _ A _ C
- Carol is at the right end: _ A B _ C

**Step 5: Find the valid arrangement**

Let's apply the constraint that Emma is sitting between two people. We can eliminate the following possibilities:

- Carol is at the left end: B _ A _ C (Emma is not between two people)
- Carol is at the right end: _ A B _ C (Emma is not between two people)

The remaining possibility is:

- Carol is at the right end: _ A B _ C

Now, let's apply the constraint that Emma is sitting between two people. We can see that the only valid arrangement is:

- Carol is at the right end: _ A B _ C
- Emma is sitting between Bob and Alice, so we have: _ A E B C

The final answer is:

The order of people from left to right is: David, Alice, Emma, Bob, Carol.


Logical Riddle:
If all Bloops are Razzies and all Razzies are Lazzies, are all Bloops definitely Lazzies?
        Also, if some Lazzies are Jazzies, can we conclude that some Bloops are Jazzies?

Applying logical reasoning...

Let's solve this logical reasoning problem step by step.

**Step 1: Identify the logical relationships (if-then statements)**

1. If all Bloops are Razzies (B → R)
2. If all Razzies are Lazzies (R → L)
3. If some Lazzies are Jazzies (L ∩ J ≠ ∅)

**Step 2: Visualize using sets or categories**

Let's represent the sets as follows:

- B: Bloops
- R: Razzies
- L: Lazzies
- J: Jazzies

We have the following relationships:

- B ⊆ R (all Bloops are Razzies)
- R ⊆ L (all Razzies are Lazzies)
- L ∩ J ≠ ∅ (some Lazzies are Jazzies)

**Step 3: Apply transitive property where applicable**

Since B ⊆ R and R ⊆ L, we can apply the transitive property to conclude that B ⊆ L (all Bloops are Lazzies).

**Step 4: Check each conclusion**

- Conclusion 1: Are all Bloops definitely Lazzies?
Yes, based on the transitive property, we can conclude that all Bloops are Lazzies.

- Conclusion 2: Can we conclude that some Bloops are Jazzies?
No, we cannot conclude that some Bloops are Jazzies. We only know that all Bloops are Lazzies, but we do not have any information about the relationship between Lazzies and Jazzies.

**Step 5: Provide the final answer with justification**

The final answer is:

- Conclusion 1: Yes, all Bloops are definitely Lazzies.
- Conclusion 2: No, we cannot conclude that some Bloops are Jazzies.

Justification: Based on the logical relationships and transitive property, we can conclude that all Bloops are Lazzies, but we do not have enough information to conclude that some Bloops are Jazzies.

======================================================================
EXAMPLE 3: CODE DEBUGGING
======================================================================

Buggy Code:

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

# Test
scores = 85, 90, 78, 92, 88]
result = calculate_average(scores)
print(f"Average: {result}")

# This works fine, but what if we pass an empty list?
empty_scores = []
result2 = calculate_average(empty_scores)  # This will crash!


Debugging step by step...

**Step 1: Identify the bug**

The bug occurs when an empty list is passed to the `calculate_average` function. This will result in a ZeroDivisionError when trying to calculate the average by dividing the total by the length of the list.

**Step 2: Explain why this bug occurs (root cause analysis)**

The root cause of this bug is that the `calculate_average` function does not handle the case where the input list is empty. When an empty list is passed to the function, the `len(numbers)` expression returns 0, which causes the division by zero error when calculating the average.

**Step 3: Describe the potential consequences**

The potential consequences of this bug are:

* The program will crash with a ZeroDivisionError when an empty list is passed to the `calculate_average` function.
* The program will not provide a meaningful result for the average when an empty list is passed.
* The program may be difficult to debug, as the error message may not clearly indicate the root cause of the problem.

**Step 4: Propose a fix with explanation**

To fix this bug, we can add a simple check at the beginning of the `calculate_average` function to return a special value (e.g., `None` or a message indicating that the list is empty) when the input list is empty. This will prevent the division by zero error and provide a more meaningful result.

**Step 5: Provide the corrected code**

Here is the corrected code:
```python
def calculate_average(numbers):
    if len(numbers) == 0:
        return None  # or return "Cannot calculate average for an empty list"
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

# Test
scores = [85, 90, 78, 92, 88]
result = calculate_average(scores)
print(f"Average: {result}")

empty_scores = []
result2 = calculate_average(empty_scores)
print(f"Average: {result2}")  # Now this will print "Average: None"

Alternatively, we can use a more Pythonic approach using the `sum` function and a conditional expression:
python
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else None

# Test
scores = [85, 90, 78, 92, 88]
result = calculate_average(scores)
print(f"Average: {result}")

empty_scores = []
result2 = calculate_average(empty_scores)
print(f"Average: {result2}")  # Now this will print "Average: None"

This code uses the fact that the `sum` function returns 0 for an empty list, and the conditional expression `numbers` will be `False` (i.e., `0`) when the list is empty, causing the function to return `None`.

======================================================================
EXAMPLE 4: DECISION MAKING ANALYSIS
======================================================================

Scenario:
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

Analyzing decision step by step...

**Step 1: Identify key constraints (time, budget, requirements)**

- Time constraint: The project must launch within 8 months.
- Budget constraint: The budget is $150,000.
- Requirements constraint: The application is expected to grow 300% in users over the next 2 years, which implies a need for scalability.   

**Step 2: Evaluate Option A (pros, cons, risks)**

- Pros:
  - Faster initial development (3 months).
  - Lower upfront cost ($50,000).
  - Team is familiar with this approach, which could lead to faster learning and development.
- Cons:
  - Harder to scale later, which may lead to performance issues and decreased user experience.
  - Single point of failure, which could result in application downtime and data loss.
- Risks:
  - Inability to scale the application to meet growing user demands.
  - Potential for increased maintenance and support costs due to a single point of failure.

**Step 3: Evaluate Option B (pros, cons, risks)**

- Pros:
  - Easier to scale, which can handle growing user demands.
  - More resilient, which reduces the risk of single points of failure.
- Cons:
  - Slower initial development (6 months).
  - Higher upfront cost ($120,000).
  - Team needs training (additional 2 weeks and $10,000).
- Risks:
  - Higher upfront cost may be a challenge if the budget is tight.
  - Training the team may lead to delays and additional costs.

**Step 4: Consider short-term vs long-term implications**

- Option A provides faster initial development and lower upfront costs, but it may lead to scalability issues and increased maintenance costs in the long term.
- Option B takes longer to develop and costs more upfront, but it provides easier scalability and resilience, which can save costs and improve user experience in the long term.

**Step 5: Calculate total costs including hidden costs**

- Option A:
  - Initial development cost: $50,000.
  - Potential hidden costs (e.g., maintenance, scalability issues): unknown.
- Option B:
  - Initial development cost: $120,000 (including training).
  - Potential hidden costs (e.g., training, potential delays): unknown.

**Step 6: Assess risk factors**

- Option A has a higher risk of scalability issues and single points of failure, which can lead to increased maintenance costs and decreased user experience.
- Option B has a higher upfront cost, but it provides easier scalability and resilience, which can save costs and improve user experience in the long term.

**Step 7: Make a recommendation with justification**

Based on the analysis, I recommend **Option B: Microservices Architecture**. Although it takes longer to develop and costs more upfront, it provides easier scalability and resilience, which can save costs and improve user experience in the long term. The expected growth of 300% in users over the next 2 years makes scalability a critical requirement, and Option B is better equipped to handle this growth. Additionally, the additional cost of training the team is a one-time investment that can pay off in the long term by reducing maintenance costs and improving user experience.

Justification:

- The time constraint of 8 months can be met by Option B, as the initial development cost is $120,000, which is within the budget of $150,000.
- The budget constraint can be met by Option B, as the upfront cost is $120,000, which is within the budget.
- The requirements constraint of scalability can be met by Option B, as it provides easier scalability and resilience.
- The risks associated with Option A (scalability issues, single points of failure) are mitigated by Option B, which provides easier scalability and resilience.
- The additional cost of training the team is a one-time investment that can pay off in the long term by reducing maintenance costs and improving user experience.

======================================================================
EXAMPLE 5: SCIENTIFIC REASONING
======================================================================

Experiment:
Observation: Plants in the north-facing window of your house are growing slower
        than plants in the south-facing window, even though you water them equally.

        Question: Why might this be happening, and how would you test your hypothesis?

Applying scientific method...

**Step 1: State the observation clearly**

Plants in the north-facing window of my house are growing slower than plants in the south-facing window, despite receiving equal amounts of water.

**Step 2: Identify possible variables (what could cause this difference?)**

Several variables could contribute to the observed difference in plant growth:

1. **Light intensity**: South-facing windows receive more direct sunlight, which may provide more light energy for photosynthesis.
2. **Light duration**: South-facing windows receive sunlight for a longer period, potentially extending the time for photosynthesis.        
3. **Temperature**: South-facing windows may be warmer due to direct sunlight, potentially affecting plant growth.
4. **Humidity**: North-facing windows may be cooler and more humid, potentially affecting plant growth.
5. **Nutrient availability**: Soil nutrients may be depleted in the north-facing window due to slower plant growth.

**Step 3: Form a hypothesis (what's your best explanation?)**

Based on the possible variables, I hypothesize that the difference in plant growth is due to the **difference in light intensity and duration** between the north-facing and south-facing windows. Specifically, I predict that the south-facing plants receive more light energy, allowing them to grow faster.

**Step 4: Design an experiment to test the hypothesis**

**Experiment:** "Effect of Light Intensity and Duration on Plant Growth"

1. **Materials**:
        * 12 identical plants (same species, age, and soil conditions)
        * 2 identical planters (same size, material, and drainage)
        * 4 identical light sources (LED grow lights or fluorescent lights)
        * 2 identical windows (north-facing and south-facing)
2. **Setup**:
        * Divide the 12 plants into 4 groups of 3 plants each.
        * Place each group in a separate planter, with the same soil and watering conditions.
        * Place 2 groups in the north-facing window and 2 groups in the south-facing window.
        * Use the light sources to provide identical light conditions for the plants in both windows.
3. **Variables to control**:
        * Watering: Water all plants equally, using a consistent schedule.
        * Temperature: Use a thermometer to monitor and maintain a consistent temperature (around 20°C) in both windows.
        * Humidity: Use a hygrometer to monitor and maintain a consistent humidity level (around 50%) in both windows.
4. **Independent variable**: Light intensity and duration ( manipulated by adjusting the light sources).
5. **Dependent variable**: Plant growth (measured by height and leaf area).

**Step 5: Predict expected results if hypothesis is correct**

If the hypothesis is correct, I predict that the south-facing plants will grow faster and taller than the north-facing plants, with a larger leaf area.

**Step 6: Consider alternative explanations**

Other possible explanations for the observed difference include:

1. **Temperature**: If the south-facing window is warmer, it may affect plant growth.
2. **Humidity**: If the north-facing window is more humid, it may affect plant growth.
3. **Nutrient availability**: If the soil in the north-facing window is depleted of nutrients, it may affect plant growth.

**Step 7: Describe how to analyze the results**

To analyze the results, I will:

1. **Measure plant growth**: Measure the height and leaf area of each plant at the beginning and end of the experiment.
2. **Compare results**: Compare the growth of plants in the north-facing and south-facing windows.
3. **Statistical analysis**: Use statistical methods (e.g., t-test, ANOVA) to determine if the differences in plant growth are statistically significant.

By following these steps, I can design an experiment to test my hypothesis and provide a scientific explanation for the observed difference in plant growth between the north-facing and south-facing windows.

======================================================================
EXAMPLE 6: BUSINESS STRATEGY ANALYSIS
======================================================================

Business Situation:
A small coffee shop is facing increased competition from a new Starbucks opening
        nearby. Current monthly revenue: $25,000. Profit margin: 20%. Regular customers: 150.

        The coffee shop is considering three strategies:
        1. Lower prices by 15% to compete
        2. Focus on specialty drinks and premium experience (20% price increase)
        3. Add lunch menu and extend hours (requires $15,000 investment)

        Question: Which strategy should they pursue and why?

Analyzing strategy step by step...

**Step 1: Assess current situation and key metrics**

- Current monthly revenue: $25,000
- Profit margin: 20%
- Regular customers: 150
- Competition from a new Starbucks opening nearby

**Step 2: Identify the core problem and competitive threat**

The core problem is the threat posed by the new Starbucks store, which may attract the coffee shop's regular customers and reduce its revenue and market share. The competitive threat is the loss of customers and revenue due to the perceived quality and convenience offered by Starbucks.

**Step 3: Analyze Strategy 1 (price reduction)**

- **Impact on revenue and profit:**
  - Lowering prices by 15% would likely lead to an increase in sales volume, as customers may be more likely to visit the coffee shop if prices are lower.
  - However, the reduced price may also lead to a decrease in profit, as the coffee shop's profit margin is 20%. A 15% price reduction would result in a 12% decrease in revenue, but only a 10% decrease in costs. This would lead to a 2% decrease in profit margin.

- **Risks and benefits:**
  - Benefits: Increased sales volume, potentially more customers, and a perceived value proposition for customers.
  - Risks: Reduced profit margin, potential loss of premium image, and decreased revenue per customer.

**Step 4: Analyze Strategy 2 (premium positioning)**

- **Impact on revenue and profit:**
  - Increasing prices by 20% would likely lead to a decrease in sales volume, as customers may be deterred by the higher prices.
  - However, the premium positioning would allow the coffee shop to maintain its profit margin and potentially increase revenue per customer.

- **Risks and benefits:**
  - Benefits: Maintained or increased profit margin, perceived premium image, and potentially more loyal customers.
  - Risks: Reduced sales volume, potentially fewer customers, and decreased revenue.

**Step 5: Analyze Strategy 3 (menu expansion)**

- **Impact on revenue and profit:**
  - Adding a lunch menu and extending hours would likely lead to an increase in revenue, as customers may be more likely to visit the coffee shop for a meal or to relax during extended hours.
  - However, the investment of $15,000 would need to be recouped through increased sales, and the coffee shop's profit margin may be affected by the increased costs of food and labor.

- **Risks and benefits:**
  - Benefits: Increased revenue, potentially more customers, and a more comprehensive offering.
  - Risks: Increased costs, potentially decreased profit margin, and the need to invest in new equipment and staff.

**Step 6: Consider market positioning and brand identity**

The coffee shop's brand identity is focused on a premium experience and high-quality products. The new Starbucks store may be perceived as a more convenient and affordable option, but the coffee shop's premium image and loyal customer base could be a strength in this situation.  

**Step 7: Make a recommendation with clear reasoning**

Based on the analysis, I recommend Strategy 2 (premium positioning). This strategy aligns with the coffee shop's brand identity and would allow it to maintain its profit margin while potentially increasing revenue per customer. While the new Starbucks store may attract some customers, the coffee shop's loyal customer base and premium image would help it maintain its market share.

**Step 8: Suggest implementation steps**

To implement Strategy 2, the coffee shop could:

1. Invest in high-quality ingredients and equipment to maintain its premium image.
2. Develop a loyalty program to reward its loyal customers and encourage repeat business.
3. Train staff to provide exceptional customer service and maintain the coffee shop's premium image.
4. Consider offering limited-time promotions or special deals to attract new customers and maintain market share.
5. Continuously monitor sales and customer feedback to adjust the strategy as needed.

======================================================================
EXAMPLE 7: ETHICAL DILEMMA ANALYSIS
======================================================================

Ethical Dilemma:
You're a software engineer at a social media company. You've discovered that
        the algorithm prioritizes sensational/controversial content because it increases
        engagement by 40%. However, research shows this is contributing to misinformation
        spread and user anxiety. Your manager says engagement metrics are critical for
        the company's upcoming funding round. What should you do?

Reasoning through ethical considerations...

**Step 1: Identify all stakeholders and their interests**

1. **Users**: Their interests are to access accurate information, reduce anxiety, and engage with content that is relevant and safe.        
2. **Company**: Their interest is to increase engagement metrics, secure funding, and maintain a competitive edge.
3. **Investors**: Their interest is to see a return on investment, which is tied to the company's performance.
4. **Research Community**: Their interest is to see accurate and reliable information being disseminated.
5. **Software Engineer (You)**: Your interest is to do what is right, maintain your integrity, and not contribute to harm.

**Step 2: Identify the ethical principles at stake**

1. **Beneficence**: Do good and promote the well-being of users and the community.
2. **Non-maleficence**: Do no harm and avoid contributing to misinformation and anxiety.
3. **Autonomy**: Respect the autonomy of users to make informed decisions.
4. **Justice**: Ensure fairness and equity in the dissemination of information.

**Step 3: Consider the consequences of each possible action**

1. **Option 1: Ignore the issue and prioritize engagement metrics**:
        * Short-term benefits: Company secures funding, and engagement metrics improve.
        * Long-term consequences: Contributing to misinformation, user anxiety, and damage to the company's reputation.
2. **Option 2: Report the issue to management and suggest alternative solutions**:
        * Short-term benefits: Company may consider alternative solutions, and users may benefit from accurate information.
        * Long-term consequences: Company may still prioritize engagement metrics, but there may be a chance for positive change.
3. **Option 3: Develop a solution to address the issue without management's knowledge**:
        * Short-term benefits: Users may benefit from accurate information, and the company's reputation may improve.
        * Long-term consequences: Company may not be aware of the solution, and it may not be scalable or sustainable.

**Step 4: Apply ethical frameworks**

### Utilitarianism

* **Option 1**: Maximizes engagement metrics, but causes harm to users and the community.
* **Option 2**: May lead to greater good for the greatest number by promoting accurate information and reducing anxiety.
* **Option 3**: Uncertain, as it depends on the effectiveness and scalability of the solution.

### Deontology

* **Option 1**: Violates duties to do no harm and promote the well-being of users.
* **Option 2**: Respects duties to do good and avoid harm.
* **Option 3**: May be seen as a duty to act in the best interest of users and the community.

### Virtue Ethics

* **Option 1**: Fails to demonstrate virtues such as compassion, empathy, and integrity.
* **Option 2**: Demonstrates virtues such as honesty, responsibility, and respect for users.
* **Option 3**: May demonstrate virtues such as initiative, creativity, and a commitment to doing good.

**Step 5: Consider long-term vs short-term implications**

* **Option 1**: Prioritizes short-term gains, but risks long-term consequences.
* **Option 2**: May lead to long-term benefits by promoting accurate information and reducing anxiety.
* **Option 3**: Uncertain, as it depends on the effectiveness and scalability of the solution.

**Step 6: Identify your sphere of influence and responsibility**

* As a software engineer, you have a responsibility to act in the best interest of users and the community.
* You have the power to develop solutions that promote accurate information and reduce anxiety.

**Step 7: Propose a course of action with ethical justification**

Based on the analysis, I propose **Option 2: Report the issue to management and suggest alternative solutions**. This option respects the duties to do good and avoid harm, promotes accurate information and reduces anxiety, and demonstrates virtues such as honesty, responsibility, and respect for users. It also acknowledges the company's interest in securing funding, but prioritizes the well-being of users and the community. By reporting the issue and suggesting alternative solutions, you can contribute to a positive change and maintain your integrity as a software engineer.
```



- **4.prompt_chaining**
```bash
======================================================================
PROMPT CHAINING DEMONSTRATION
======================================================================
Model: llama-3.1-8b-instant
======================================================================

======================================================================
EXAMPLE 1: CONTENT CREATION PIPELINE
======================================================================

 STEP 1: Generating blog post outline...

Outline:
**I. Title:** "Reimagining the Workspace: Navigating the Future of Remote Work"

**II. Introduction Hook:**
- "Welcome to a new era of work flexibility: where boundaries blur and innovation thrives."
- Brief overview of the growth and impact of remote work.

**III. Main Sections:**

**A. "The Shift to Remote Work: Trends and Statistics"**
- Overview of the rise of remote work
- Statistics on remote work adoption and growth
- Industry-specific trends and statistics

**B. "Benefits of Remote Work: Productivity, Employee Happiness, and the Environment"**
- Productivity benefits of remote work
- Employee happiness and engagement in remote work settings
- Environmental benefits of reduced commuting and office energy consumption

**C. "Challenges and Strategies for Effective Remote Work"**
- Common challenges of remote work (communication, isolation, time management)
- Strategies for overcoming these challenges (communication tools, virtual team-building, self-care)
- Best practices for remote work management and leadership

**D. "Future of Remote Work: Emerging Technologies and Trends"**
- Emerging technologies (AI, AR, VR) and their impact on remote work
- Trends in virtual collaboration and communication tools
- Potential future directions for remote work (smart offices, virtual reality workspaces)

**E. "The Future of the Office: Adapting to a Remote-Centric World"**
- The future of traditional office spaces
- Hybrid work models and flexible office spaces
- Strategies for office spaces to adapt to a remote work-centric world

**IV. Conclusion**

**V. Key Takeaways**

- Summary of main points
- Final thoughts on the future of remote work and its impact on the world of work.


 STEP 2: Writing introduction based on outline...

Introduction:
**Welcome to a new era of work flexibility: where boundaries blur and innovation thrives.**

The landscape of work is undergoing a profound transformation. Gone are the days of rigid 9-to-5 routines and cramped cubicles. As the world becomes increasingly interconnected, the lines between work and personal life are blurring, and a new era of work flexibility is dawning.  

Remote work has been on the rise for years, and its impact is being felt far and wide. According to recent statistics, remote work adoption has skyrocketed, with an estimated 4.7 million employees working from home at least half of the time. But remote work is more than just a trend – it's a revolution that's redefining the way we work, communicate, and collaborate.

In this report, we'll take a deep dive into the world of remote work, exploring the trends, statistics, and strategies that are shaping the future of work. We'll examine the benefits and challenges of remote work, and explore the emerging technologies and trends that will define the next generation of work. Join us on a journey to reimagine the workspace and navigate the future of remote work.


 STEP 3: Expanding first main section...

First Section:
**The Shift to Remote Work: Trends and Statistics**

As we navigate the future of remote work, it's essential to understand the trends and statistics that have shaped this shift. The landscape of work has undergone a significant transformation, and remote work has emerged as a dominant force in the modern work environment.

**The Rise of Remote Work**

Remote work, also known as telecommuting or working from home, has been on the rise for years. According to a study by Gallup, the percentage of employed adults working remotely at least some of the time has increased from 31% in 2015 to 43% in 2020. This trend is expected to continue, with an estimated 73% of companies planning to allow remote work full-time or part-time by 2028.

**Industry-Specific Trends and Statistics**

While remote work is becoming more prevalent across industries, some sectors are leading the charge. The tech industry, for example, has been at the forefront of remote work adoption, with companies like Amazon and Microsoft embracing flexible work arrangements. In fact, a survey by Upwork found that 63% of tech companies have remote workers, compared to 45% in other industries.

The healthcare industry is also seeing a significant shift towards remote work, with telehealth services becoming increasingly popular. According to a report by Grand View Research, the global telehealth market is expected to reach $185.6 billion by 2025, growing at a CAGR of 32.1%.

**Remote Work Adoption by Region**

The adoption of remote work varies by region. A survey by PwC found that 70% of employees in the United States work remotely at least one day a week, compared to 50% in Europe and 40% in Asia. However, these numbers are expected to change as more companies adopt flexible work arrangements and remote work becomes the new norm.

In conclusion, the shift to remote work is a significant trend that's transforming the way we work. With remote work adoption increasing across industries and regions, it's essential for businesses to understand the benefits and challenges of remote work and adapt their strategies accordingly. In the next section, we'll explore the benefits of remote work, including productivity, employee happiness, and environmental benefits.


 STEP 4: Creating SEO meta description...

Meta Description:
"Discover the future of work: trends, statistics, and strategies on remote work adoption, productivity, and employee happiness, redefining the modern work environment."

======================================================================
EXAMPLE 2: DATA ANALYSIS WORKFLOW
======================================================================

 STEP 1: Extracting and structuring data...

Structured Data:
**Structured Sales Data Q4 2024**

### 1. Sales Trends for Each Product

| Product | January | February | March | April |
| --- | --- | --- | --- | --- |
| Product A | $45K | $52K | $48K | $61K |
| Product B | $38K | $41K | $39K | $44K |
| Product C | $29K | $33K | $42K | $51K |

### 2. Customer Satisfaction Trends

| Product | January | February | March | April |
| --- | --- | --- | --- | --- |
| Product A | 8.2 | 8.5 | 8.1 | 8.7 |
| Product B | 7.1 | 7.3 | 7.2 | 7.5 |
| Product C | 6.8 | 7.2 | 7.9 | 8.4 |

### 3. Key Observations

- **Sales Trends:**
  - Product A shows a consistent increase in sales throughout Q4 2024, with a significant jump in April.
  - Product B experiences a relatively flat sales trend, with minimal variation throughout the quarter.
  - Product C exhibits a notable increase in sales in March and April, indicating a potential shift in customer demand.

- **Customer Satisfaction Trends:**
  - Product A maintains a high customer satisfaction score throughout Q4 2024, with an average score of 8.4.
  - Product B has a relatively stable customer satisfaction score, averaging 7.3.
  - Product C shows a significant improvement in customer satisfaction, with an average score of 7.6.

- **Overall Observations:**
  - Product A appears to be the most successful product in terms of sales and customer satisfaction.
  - Product C shows promise, with increasing sales and improved customer satisfaction.
  - Product B requires further analysis to identify areas for improvement.


 STEP 2: Calculating key metrics...

Calculated Metrics:
### Calculations

#### 1. Growth Rate for Each Product (Jan to Apr)

To calculate the growth rate for each product, we'll use the formula:

Growth Rate = ((April Sales - January Sales) / January Sales) * 100

| Product | January Sales | April Sales | Growth Rate |
| --- | --- | --- | --- |
| Product A | $45K | $61K | ((61 - 45) / 45) * 100 = 35.56% |
| Product B | $38K | $44K | ((44 - 38) / 38) * 100 = 15.79% |
| Product C | $29K | $51K | ((51 - 29) / 29) * 100 = 76.55% |

#### 2. Average Customer Satisfaction per Product

To calculate the average customer satisfaction per product, we'll take the average of the customer satisfaction scores for each product.    

| Product | Average Customer Satisfaction |
| --- | --- |
| Product A | (8.2 + 8.5 + 8.1 + 8.7) / 4 = 8.375 |
| Product B | (7.1 + 7.3 + 7.2 + 7.5) / 4 = 7.325 |
| Product C | (6.8 + 7.2 + 7.9 + 8.4) / 4 = 7.675 |

#### 3. Best and Worst Performing Products

Based on the calculations above, we can determine the best and worst performing products.

**Best Performing Product:** Product A (highest growth rate and average customer satisfaction)
**Worst Performing Product:** Product B (lowest growth rate and average customer satisfaction)

### Conclusion

Based on the calculations, Product A appears to be the most successful product in terms of sales and customer satisfaction, while Product B requires further analysis to identify areas for improvement. Product C shows promise, with increasing sales and improved customer satisfaction.


 STEP 3: Identifying insights and patterns...

Insights:
### Key Insights

1. **Product A is the top performer**: With the highest growth rate (35.56%) and average customer satisfaction (8.375), Product A is the most successful product in terms of sales and customer satisfaction.
2. **Product B needs improvement**: Product B has the lowest growth rate (15.79%) and average customer satisfaction (7.325), indicating that it requires further analysis to identify areas for improvement.
3. **Product C shows promise**: Although not the top performer, Product C has a significant growth rate (76.55%) and improved customer satisfaction, suggesting that it is worth continuing to develop and market.

### Patterns or Correlations

1. **Positive correlation between growth rate and customer satisfaction**: The products with higher growth rates (Product A and Product C) also have higher average customer satisfaction scores, suggesting a positive correlation between the two metrics.
2. **Negative correlation between growth rate and product performance**: The product with the lowest growth rate (Product B) also has the lowest average customer satisfaction score, indicating a negative correlation between the two metrics.

### Surprising Findings

1. **Product C's high growth rate**: Despite having a lower average customer satisfaction score than Product A, Product C has a significantly higher growth rate (76.55% vs. 35.56%), which may indicate that its growth is driven by factors other than customer satisfaction.
2. **Product B's low customer satisfaction**: Despite having a relatively high sales growth rate (15.79%) compared to other products, Product B also has a low average customer satisfaction score, which may indicate underlying issues with its product or customer experience.       


 STEP 4: Generating actionable recommendations...

Recommendations:
### Actionable Recommendations

Based on the insights, patterns, and correlations, here are three actionable recommendations:

#### 1. **Conduct a thorough analysis of Product B's customer experience**

* **Expected Impact:** Improve customer satisfaction score by 1.5 points, leading to a 10% increase in sales growth rate.
* **Priority Level:** High
* **Action:** Conduct surveys, gather feedback from customers, and analyze customer complaints to identify areas for improvement. Implement changes to enhance the customer experience, such as improving product quality, reducing wait times, or enhancing customer support.

#### 2. **Invest in Product C's marketing and development**

* **Expected Impact:** Increase Product C's growth rate by 20%, leading to a 15% increase in overall sales.
* **Priority Level:** Medium
* **Action:** Develop a targeted marketing campaign to increase awareness and demand for Product C. Invest in product development to address any limitations or pain points that may be hindering its growth.

#### 3. **Monitor and adjust Product A's growth strategy**

* **Expected Impact:** Maintain Product A's growth rate, preventing a potential decline in sales.
* **Priority Level:** Low
* **Action:** Continuously monitor Product A's sales and customer satisfaction trends. Adjust the growth strategy as needed to prevent complacency and maintain market share. Consider investing in product development or marketing to further accelerate growth.

These recommendations are designed to address the key insights and patterns identified in the analysis, with a focus on improving customer satisfaction, increasing sales growth, and maintaining market share.

======================================================================
EXAMPLE 3: CUSTOMER SUPPORT WORKFLOW
======================================================================

 STEP 1: Categorizing and prioritizing ticket...

Classification:
**Classification:**

1. **Issue categories:**
   - Order issue (incorrect item received)
   - Payment issue (charged twice)
   - Product availability (blue laptop case not available)
   - Customer satisfaction (frustration)

2. **Priority level:** High
   - The customer received the wrong item, was charged twice, and has a presentation next week, making it a high-priority issue.

3. **Sentiment:** Angry
   - The customer uses strong language ("very frustrating") to express their dissatisfaction and frustration.

4. **Urgency indicators:**
   - Time-sensitive: The customer has a presentation next week, indicating a time-sensitive issue.
   - Emphasis on immediate resolution: The customer's use of "I need the blue case" and "this is very frustrating" suggests that they require a prompt resolution.


 STEP 2: Extracting required actions...

Action Items:
**Immediate Actions:**

1. **Verify Order and Payment Information:**
   - Check the order details (Order #12345) to confirm the incorrect item received and the duplicate charge.
   - Review the customer's payment history to identify the duplicate charge.

2. **Issue Refund for Duplicate Charge:**
   - Process a refund for the duplicate charge to the customer's credit card.

3. **Rush Order for Correct Item:**
   - Expedite the shipping of the correct blue laptop case to the customer.
   - Provide the customer with tracking information for the correct order.

4. **Apologize and Acknowledge Customer's Concerns:**
   - Respond to the customer with a sincere apology for the inconvenience and frustration caused.
   - Acknowledge their urgency and assure them that a resolution is being worked on.

5. **Assess Product Availability:**
   - Check the inventory for the blue laptop case to determine if it's available in stock.
   - If not available, explore alternative options, such as expedited shipping or a replacement item.

**Follow-up Actions:**

1. **Verify Delivery of Correct Item:**
   - Follow up with the customer to confirm that they have received the correct blue laptop case.

2. **Check for Any Further Issues:**
   - Review the customer's account to ensure that there are no other issues or concerns.

3. **Monitor Customer Satisfaction:**
   - Keep a close eye on the customer's satisfaction level and respond promptly to any further concerns or issues.

**Systems to Check:**

1. **Orders System:**
   - Verify the order details, including the item received and the shipping information.
   - Check for any other issues or concerns related to the order.

2. **Payments System:**
   - Review the customer's payment history to identify the duplicate charge.
   - Process a refund for the duplicate charge.

3. **Inventory System:**
   - Check the inventory for the blue laptop case to determine if it's available in stock.
   - Update the inventory levels to reflect the correct item received by the customer.

4. **Customer Relationship Management (CRM) System:**
   - Update the customer's account with the resolution details and any follow-up actions.
   - Monitor the customer's satisfaction level and respond promptly to any further concerns or issues.


 STEP 3: Drafting customer response...

Draft Response:
Subject: Urgent Resolution for Order #12345

Dear Sarah,

I am writing to apologize sincerely for the inconvenience and frustration you have experienced with your order #12345. We understand the urgency of your situation, and I am committed to resolving this issue promptly.

First and foremost, I want to acknowledge that you received the incorrect item - a red laptop case instead of the blue one you ordered. I also apologize for the duplicate charge on your credit card. You can be assured that we are taking immediate action to rectify these issues.  

To resolve the issue, we will be processing a refund for the duplicate charge to your credit card immediately. You should receive the refund within 3-5 business days. We will also expedite the shipping of the correct blue laptop case to you. You will receive a tracking number via email once the order is shipped, which should be within the next 24 hours.

Regarding the availability of the blue laptop case, we have checked our inventory and unfortunately, we are currently out of stock. However, we are working closely with our suppliers to expedite the shipment of the correct item. We will keep you updated on the expected delivery date.

As a gesture of goodwill, we would like to offer you a 10% discount on your next purchase. We value your business and appreciate your patience and understanding in this matter.

Please note that we will follow up with you to confirm that you have received the correct blue laptop case and to ensure that you are satisfied with the resolution. If you have any further concerns or issues, please do not hesitate to reach out to us.

Thank you for bringing this to our attention, and we look forward to resolving this issue to your satisfaction.

Best regards,

[Your Name]
Customer Service Representative
[Company Name]
[Contact Information]

This email response acknowledges all the issues, apologizes sincerely, explains the resolution steps, provides a timeline, and offers compensation as a gesture of goodwill.


 STEP 4: Creating internal tracking notes...

Internal Notes:
**Internal Notes:**

**Summary:** Urgent resolution for Order #12345, incorrect item received and duplicate charge, expedited shipping and refund processed.     

**Actions taken:**

1. **Verified Order and Payment Information:** Confirmed incorrect item received and duplicate charge on Order #12345.
2. **Issued Refund for Duplicate Charge:** Processed refund for duplicate charge to customer's credit card.
3. **Rushed Order for Correct Item:** Expedited shipping of correct blue laptop case to customer, provided tracking information.
4. **Acknowledged Customer's Concerns:** Responded to customer with sincere apology and assurance of resolution.
5. **Assessed Product Availability:** Checked inventory for blue laptop case, currently out of stock, but working with suppliers to expedite shipment.

**Follow-up required:**

1. **Verify Delivery of Correct Item:** Follow up with customer to confirm receipt of correct blue laptop case.
2. **Check for Any Further Issues:** Review customer's account for any other concerns or issues.
3. **Monitor Customer Satisfaction:** Keep a close eye on customer's satisfaction level and respond promptly to any further concerns.       

**Escalation:** No escalation required at this time.

**Systems checked:**

1. **Orders System:** Verified order details, shipping information, and inventory levels.
2. **Payments System:** Reviewed customer's payment history and processed refund for duplicate charge.
3. **Inventory System:** Checked inventory levels for blue laptop case and updated accordingly.
4. **Customer Relationship Management (CRM) System:** Updated customer's account with resolution details and follow-up actions.

**Response sent:** Urgent Resolution for Order #12345 email sent to customer with explanation of resolution steps, timeline, and compensation as a gesture of goodwill.

**Next steps:**

- Follow up with customer to confirm receipt of correct blue laptop case.
- Review customer's account for any other concerns or issues.
- Monitor customer satisfaction level and respond promptly to any further concerns.

======================================================================
EXAMPLE 4: RESEARCH SYNTHESIS WORKFLOW
======================================================================

 STEP 1: Summarizing individual sources...

Source 1 Summary:
Main finding:
Daily exercise reduces stress by 40%.

Sample/methodology hint:
The study was conducted by University A in 2024, but there is not enough information to provide more details about the sample or methodology.

Year and source:
2024, University A

Source 2 Summary:
There is not enough information provided about the research. However, based on the given information, here's a possible summary:

 Main finding: 30 minutes of walking improves mood markers.
 Sample/methodology hint: The study involved walking for 30 minutes, but the specific details about the sample size, demographics, and methodology are not provided.
 Year and source: Journal B, 2023.

Source 3 Summary:
Main finding: Exercise was linked to better sleep quality in 85% of participants.

Sample/methodology hint: The study involved a sample of participants, but the exact details are not provided.

Year and source: 2024, Institute C.


 STEP 2: Identifying common themes...

Common Themes:
Based on the provided research summaries, I can identify the following common themes across studies:

1. **Physical activity has a positive impact on mental and physical health**: All three studies suggest that physical activity, in some form, has a beneficial effect on health. This can include reducing stress, improving mood, and enhancing sleep quality.
2. **Exercise as a general intervention**: The studies do not specify a particular type of exercise, but rather that exercise in general has a positive effect on health outcomes.
3. **Quantifiable benefits**: Each study reports a specific percentage or percentage of participants who experienced improved outcomes, suggesting that the benefits of exercise are measurable and quantifiable.

Converging findings:

1. **Exercise is linked to improved mental health**: The first two studies suggest that exercise is associated with reduced stress and improved mood, indicating a connection between physical activity and mental well-being.
2. **Exercise has a positive impact on sleep quality**: The third study found that exercise was linked to better sleep quality in 85% of participants, reinforcing the idea that physical activity has a beneficial effect on physical health.

Areas of agreement:

1. **Exercise is a beneficial activity**: All three studies conclude that exercise has a positive impact on health outcomes, whether it's reducing stress, improving mood, or enhancing sleep quality.
2. **Physical activity has a measurable effect**: The studies report specific percentages or outcomes, indicating that the benefits of exercise are quantifiable and can be measured.


 STEP 3: Synthesizing overall conclusions...

Synthesis:
**Overall Conclusions:**

Based on the converging findings and areas of agreement across the three studies, it can be concluded that exercise has a profound impact on both mental and physical health. The evidence suggests that regular physical activity can reduce stress, improve mood, and enhance sleep quality, leading to improved overall well-being.

**Strength of Evidence:**

The strength of evidence is moderate to strong, given the following factors:

1. **Consistency**: All three studies report similar findings, indicating a consistent relationship between exercise and improved health outcomes.
2. **Quantifiability**: The studies provide specific percentages or outcomes, allowing for a clear understanding of the benefits of exercise.
3. **Generalizability**: While the studies do not specify a particular type of exercise, they suggest that exercise in general has a positive effect on health outcomes, making the findings more generalizable.

However, the strength of evidence could be strengthened by:

1. **Replication**: Additional studies replicating the findings would increase confidence in the results.
2. **Long-term follow-up**: Studies with longer follow-up periods would provide more insight into the long-term effects of exercise on health outcomes.
3. **Diverse populations**: Studies involving diverse populations, including those with different ages, ethnicities, and health conditions, would increase the generalizability of the findings.

**Practical Implications:**

The findings of these studies have significant practical implications for individuals, healthcare providers, and policymakers. Some potential implications include:

1. **Promoting exercise as a preventive measure**: Healthcare providers can recommend exercise as a preventive measure to reduce stress, improve mood, and enhance sleep quality.
2. **Developing exercise programs**: Exercise programs can be designed to target specific health outcomes, such as stress reduction or sleep improvement.
3. **Policy initiatives**: Policymakers can implement initiatives to increase access to exercise opportunities, such as public parks, recreational facilities, or community programs.
4. **Individual behavior change**: Individuals can make lifestyle changes by incorporating regular exercise into their daily routine to improve their mental and physical health.

Overall, the synthesis of these studies provides a compelling case for the importance of exercise in maintaining good health and well-being.


 STEP 4: Creating executive summary...

Executive Summary:
**Executive Summary (100 words)**

This synthesis of three studies demonstrates the profound impact of exercise on both mental and physical health. Regular physical activity reduces stress, improves mood, and enhances sleep quality, leading to improved overall well-being. The evidence is moderate to strong, with consistency, quantifiability, and generalizability supporting the findings. To strengthen the evidence, replication, long-term follow-up, and diverse population studies are recommended. The practical implications are significant, with potential applications in healthcare, policy, and individual behavior change. By promoting exercise as a preventive measure, developing targeted exercise programs, and increasing access to exercise opportunities, individuals and society can benefit from the numerous health advantages of regular physical activity.

======================================================================
EXAMPLE 5: CODE REVIEW WORKFLOW
======================================================================

 STEP 1: Analyzing code structure...

Structure Analysis:
**Function Clarity and Naming:**

The function name `process_user_data` is somewhat generic and does not clearly convey the purpose of the function. A more descriptive name would be `filter_adults` or `get_adult_users`, as it indicates that the function is filtering users based on their age.

The function takes a single argument `users`, which is a list of dictionaries. This is clear and concise.

**Code Organization:**

The code is well-organized in terms of structure. It uses a clear and consistent indentation scheme, and the logic is easy to follow.       

However, the function could be improved by using a more Pythonic way of filtering the list, such as using a list comprehension:

python
def filter_adults(users):
    return [user for user in users if user['age'] > 18]


This code achieves the same result as the original code but is more concise and readable.

**Readability:**

The code is generally easy to read, with clear variable names and a consistent indentation scheme. However, the original code could benefit from some additional comments to explain the purpose of the function and the logic behind it.

Here is an updated version of the code with improved function clarity, code organization, and readability:

```python
def filter_adults(users):
    """
    Filters a list of users based on their age, returning only users who are adults (age > 18).

    Args:
        users (list): A list of dictionaries, where each dictionary represents a user with 'name', 'age', and 'email' keys.

    Returns:
        list: A list of dictionaries representing the adult users.
    """
    return [user for user in users if user['age'] > 18]

users = [
    {'name': 'Alice', 'age': 25, 'email': 'alice@email.com'},
    {'name': 'Bob', 'age': 17, 'email': 'bob@email.com'}
]
output = filter_adults(users)
print(output)


This updated code is more concise, readable, and maintainable, making it easier for others to understand and work with.


 STEP 2: Identifying potential bugs and edge cases...

Bug Analysis:
**Bug Analysis**

### 1. Potential Runtime Errors

1. **KeyError**: The code assumes that every user dictionary will have the keys 'name', 'age', and 'email'. However, if any of these keys are missing, a KeyError will be raised. To handle this, we can add a check to ensure that the required keys exist before trying to access them.

2. **TypeError**: The code assumes that the 'age' value will always be a number. However, if the 'age' value is not a number, a TypeError will be raised when trying to compare it to 18. To handle this, we can add a check to ensure that the 'age' value is a number before trying to compare it.

### 2. Edge Cases Not Handled

1. **Empty List**: If the input list 'users' is empty, the function will return an empty list, which is the expected behavior. However, it's worth noting that this is an edge case that should be handled explicitly.

2. **Non-List Input**: If the input 'users' is not a list, the function will raise a TypeError when trying to iterate over it. To handle this, we can add a check to ensure that the input is a list.

3. **Null Input**: If the input 'users' is None, the function will raise an AttributeError when trying to iterate over it. To handle this, we can add a check to ensure that the input is not None.

### 3. Logic Issues

1. **Status Logic**: The code sets the 'status' to 'adult' if the user's age is greater than 18. However, this logic is simplistic and may not cover all possible scenarios. For example, what if the user's age is 18? Should they be considered an adult or a minor? To handle this, we can add more nuanced logic to determine the user's status.

Here's an updated version of the code that addresses these issues:

```python
def process_user_data(users):
    """
    Processes user data and returns a list of users who are adults.

    Args:
        users (list): A list of user dictionaries.

    Returns:
        list: A list of user dictionaries with 'status' set to 'adult' if the user is an adult.
    """
    if not isinstance(users, list):
        raise ValueError("Input must be a list")

    result = []
    for user in users:
        if user is None:
            continue
        if not isinstance(user, dict):
            continue
        if 'name' not in user or 'age' not in user or 'email' not in user:
            continue
        if not isinstance(user['age'], (int, float)):
            continue
        if user['age'] > 18:
            result.append({
                'name': user['name'],
                'email': user['email'],
                'status': 'adult'
            })
        elif user['age'] == 18:
            result.append({
                'name': user['name'],
                'email': user['email'],
                'status': 'young adult'
            })
        else:
                'email': user['email'],
                'status': 'young adult'
            })
        else:
        else:
            result.append({
                'name': user['name'],
                'email': user['email'],
                'status': 'minor'
            })
    return result

users = [
    {'name': 'Alice', 'age': 25, 'email': 'alice@email.com'},
    {'name': 'Bob', 'age': 17, 'email': 'bob@email.com'}
]
output = process_user_data(users)
print(output)


This updated code adds checks to handle potential runtime errors, edge cases, and logic issues. It also includes more nuanced logic to determine the user's status based on their age.


STEP 3: Suggesting improvements...

Suggested Improvements:
**Performance Improvements**

1.  **Use List Comprehension**: Instead of using a for loop to iterate over the list and append elements to the result list, use a list comprehension. This can be more efficient and concise.

    ```python
result = [
    {
        'name': user['name'],
        'email': user['email'],
        'status': 'adult' if user['age'] > 18 else 'young adult' if user['age'] == 18 else 'minor'
    }
    for user in users
    if isinstance(user, dict) and 'name' in user and 'age' in user and 'email' in user and isinstance(user['age'], (int, float))
]


2.  **Use Built-in Functions**: Instead of using a for loop to iterate over the list and check if the 'age' value is a number, use the `all()` function with a generator expression. This can be more efficient and concise.

    ```python
result = [
    {
        'name': user['name'],
        'email': user['email'],
        'status': 'adult' if user['age'] > 18 else 'young adult' if user['age'] == 18 else 'minor'
    }
    for user in users
    if isinstance(user, dict) and 'name' in user and 'age' in user and 'email' in user and isinstance(user['age'], (int, float))
]


3.  **Use Set Operations**: Instead of using a for loop to iterate over the list and check if the 'age' value is a number, use set operations. This can be more efficient and concise.

    ```python
result = [
    {
        'name': user['name'],
        'email': user['email'],
        'status': 'adult' if user['age'] > 18 else 'young adult' if user['age'] == 18 else 'minor'
    }
    for user in set(users)
    if isinstance(user, dict) and 'name' in user and 'age' in user and 'email' in user and isinstance(user['age'], (int, float))
]


**Better Error Handling**

1.  **Use Try-Except Blocks**: Instead of using a for loop to iterate over the list and check if the 'age' value is a number, use try-except blocks. This can be more efficient and concise.

    ```python
try:
    result = [
        {
            'name': user['name'],
            'email': user['email'],
            'status': 'adult' if user['age'] > 18 else 'young adult' if user['age'] == 18 else 'minor'
        }
        for user in users
        if isinstance(user, dict) and 'name' in user and 'age' in user and 'email' in user and isinstance(user['age'], (int, float))        
    ]
except KeyError as e:
    print(f"Error: {e}")
except TypeError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")


2.  **Use Custom Error Messages**: Instead of using a generic error message, use custom error messages. This can be more informative and helpful.

    ```python
try:
    result = [
        {
            'name': user['name'],
            'email': user['email'],
            'status': 'adult' if user['age'] > 18 else 'young adult' if user['age'] == 18 else 'minor'
        }
        for user in users
        if isinstance(user, dict) and 'name' in user and 'age' in user and 'email' in user and isinstance(user['age'], (int, float))        
    ]
except KeyError as e:
    print(f"Error: Missing key '{e.args[0]}' in user dictionary")
except TypeError as e:
    print(f"Error: Invalid type '{type(e).__name__}' for value '{e.args[0]}'")
except Exception as e:
    print(f"Error: Unknown error '{e.args[0]}'")


**Code Style Improvements**

1.  **Use Consistent Indentation**: Instead of using inconsistent indentation, use consistent indentation. This can make the code more readable and maintainable.

    ```python
result = [
    {
        'name': user['name'],
        'email': user['email'],
        'status': 'adult' if user['age'] > 18 else 'young adult' if user['age'] == 18 else 'minor'
    }
    for user in users
    if isinstance(user, dict) and 'name' in user and 'age' in user and 'email' in user and isinstance(user['age'], (int, float))
]


2.  **Use Docstrings**: Instead of using comments to explain the code, use docstrings. This can make the code more readable and maintainable.

    ```python
def process_user_data(users):
    """
    Processes user data and returns a list of users who are adults.

    Args:
        users (list): A list of user dictionaries.

    Returns:
        list: A list of user dictionaries with 'status' set to 'adult' if the user is an adult.

    Raises:
        KeyError: If a user dictionary is missing a required key.
        TypeError: If a user dictionary has an invalid type for a value.
        Exception: If an unknown error occurs.
    """
    try:
        result = [
            {
                'name': user['name'],
                'email': user['email'],
                'status': 'adult' if user['age'] > 18 else 'young adult' if user['age'] == 18 else 'minor'
            }
            for user in users
            if isinstance(user, dict) and 'name' in user and 'age' in user and 'email' in user and isinstance(user['age'], (int, float))    
        ]
        return result
    except KeyError as e:
        print(f"Error: Missing key '{e.args[0]}' in user dictionary")
    except TypeError as e:
        print(f"Error: Invalid type '{type(e).__name__}' for value '{e.args[0]}'")
    except Exception as e:
        print(f"Error: Unknown error '{e.args[0]}'")


3.  **Use Type Hints**: Instead of using comments to explain the types of variables, use type hints. This can make the code more readable and maintainable.

    ```python
def process_user_data(users: list[dict]) -> list[dict]:
    """
    Processes user data and returns a list of users who are adults.

    Args:
        users (list[dict]): A list of user dictionaries.

    Returns:
        list[dict]: A list of user dictionaries with 'status' set to 'adult' if the user is an adult.

    Raises:
        KeyError: If a user dictionary is missing a required key.
        TypeError: If a user dictionary has an invalid type for a value.
        Exception: If an unknown error occurs.
    """
    try:
        result = [
            {
                'name': user['name'],
                'email': user['email'],
                'status': 'adult' if user['age'] > 18 else 'young adult' if user['age'] == 18 else 'minor'
            }
            for user in users
            if isinstance(user, dict) and 'name' in user and 'age' in user and 'email' in user and isinstance(user['age'], (int, float))    
        ]
        return result
    except KeyError as e:
        print(f"Error: Missing key '{e.args[0]}' in user dictionary")
    except TypeError as e:
        print(f"Error: Invalid type '{type(e).__name__}' for value '{e.args[0]}'")
    except Exception as e:
        print(f"Error: Unknown error '{e.args[0]}'")
```













