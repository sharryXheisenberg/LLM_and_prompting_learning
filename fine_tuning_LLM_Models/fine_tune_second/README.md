## **What is Fine-tuning?**

**Fine-tuning** is taking a pre-trained model and **training at least one internal model parameter** (i.e. weights). In the context of LLMs, what this typically accomplishes is transforming a general-purpose base model (e.g. GPT-3) into a specialized model for a particular use case (e.g. ChatGPT)

The key upside of this approach is that models can achieve better performance while requiring (far) fewer manually labeled examples compared to models that solely rely on supervised training.

---

### **Why Fine-tune**
Fine-tuning not only improves the performance of a base model, but a **smaller (fine-tuned) model can often outperform larger (more expensive) models** on the set of tasks on which it was trained.A big problem in LLMs have a finite context window. Thus, the model may perform sub-optimally on tasks that require a large knowledge base or domain-specific information

<!-- <p align="center">
  <em>Figure 1: End-to-end workflow of fine-tuning a Large Language Model</em>
</p> -->

---

### **3 Ways to Fine-tune**

There are 3 generic ways one can fine-tune a model: **self-supervised, supervised, and reinforcement learning**. These are not mutually exclusive in that any combination of these three approaches can be used in succession to fine-tune a single model.


1. **Self-supervised Learning**  
   Self-supervised learning consists of **training a model based on the inherent structure of the training data**. In the context of LLMs, what this typically looks like is given a sequence of words (or tokens, to be more precise), predict the next word (token).

2. **Supervised Learning**  
   This involves **training a model on input-output pairs for a particular task**. An example is instruction tuning, which aims to improve model performance in answering questions or responding to user prompts. The key step in supervised learning is curating a training dataset. A simple way to do this is to create question-answer pairs and integrate them into a prompt template 

3. **Reinforcement Learning**  
   Reinforcement learning (RL) to fine-tune models. RL uses a **reward model to guide the training of the base model**. This can take many different forms, but the basic idea is to train the reward model to score language model completions such that they reflect the preferences of human labelers.
---

### **Options for Parameter Training**
When it comes to fine-tuning a model with ~100M-100B parameters, one needs to be thoughtful of computational costs. Toward this end, an important question is – which parameters do we (re)train?

1. **Option 1: Retrain all parameters**
The first option is to train all internal model parameters (called full parameter tuning). While this option is simple (conceptually), it is the most computationally expensive. Additionally, a known issue with full parameter tuning is the phenomenon of **catastrophic forgetting**. This is where the **model "forgets" useful information it "learned" in its initial training**.

2. **Option 2: Transfer Learning**
The big idea with transfer learning (TL) is to preserve the useful representations/features the model has learned from past training when applying the model to a new task. This generally consists of **dropping "the head" of a neural network (NN) and replacing it with a new one (e.g. adding new layers with randomized weights)**. Note: The head of an NN includes its final layers, which translate the model’s internal representations to output values.

3. **Option 3: Parameter Efficient Fine-tuning (PEFT)**
PEFT involves **augmenting a base model with a relatively small number of trainable parameters**. The key result of this is a fine-tuning methodology that demonstrates comparable performance to full parameter tuning at a **tiny fraction of the computational and storage cost**.

In Low-Rank Adaptation (LoRA), the original weight matrix is kept frozen, and a low-rank update is learned during fine-tuning. The forward computation is defined as:

$$
h(x) = W_0 x + \Delta W x = W_0 x + BAx
$$

where:

- $W_0, \Delta W \in \mathbb{R}^{d \times k}$
- $B \in \mathbb{R}^{d \times r}$
- $A \in \mathbb{R}^{r \times k}$
- $r \ll \min(d, k)$

<p align="center">
  <em>Figure: Weight decomposition in LoRA showing low-rank adaptation during fine-tuning.</em>
</p>

Where h() = a hidden layer that will be tuned, x = the input to h(), W₀ = the original weight matrix for the h, and ΔW = a matrix of trainable parameters injected into h. ΔW is decomposed according to ΔW=BA, where ΔW is a d by k matrix, B is d by r, and A is r by k. r is the assumed "intrinsic rank" of ΔW (which can be as small as 1 or 2)

---
