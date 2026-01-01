

## **Fine Tuning Large Language Model (LLM)**
Fine-tuning refers to the process of taking a pre-trained model and adapting it to a specific task by training it further on a smaller, domain-specific dataset. It refines the model’s capabilities and improving its accuracy in specialized tasks without needing a massive dataset or expensive computational resources.

- Here I am implementing Fine Tuning Large Language Model using DialogSum Database but before implementation let's see the working and types.

- **Fine tuning follows this procedure**
![fine_tuning_process](assets/fine_tuning_llm_model.png)


#### **The general fine-tuning process can be broken down into following steps**
- 1. **Select Base Model:** Choose a pre-trained model based on our task and compute budget.
- 2. **Choose Fine-Tuning Method:** Select the most appropriate method like Instruction Fine-Tuning, Supervised Fine-Tuning, PEFT, lora, qlora, etc based on the task and dataset.
- 3. **Prepare Dataset:** Structure our data for task-specific training, ensuring the format matches the model's requirements.
- 4. **Training:** Use frameworks like TensorFlow, PyTorch or high-level libraries like Transformers to fine-tune the model.
-5.**Evaluate and Iterate:** Test the model, refine it as necessary and re-train to improve performance.

#### **Types of Fine Tuning Methods**
- 1. Supervised Fine-Tuning
- 2. Instruction Fine-Tuning
- 3. Parameter-Efficient Fine-Tuning (PEFT)
- 4. Reinforcement Learning with Human Feedback (RLHF)








