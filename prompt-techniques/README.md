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

- **zero_shot_prompting**
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












