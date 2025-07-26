# Automatic eval
import openai
import os
from doten import load_doten
load_dotenv()

evals = [
	"What is Underwhelming Spatula?",                             
	"Who wrote 'Dubious Parenting Tips'?",
	"How long is Almost-Perfect Investment Guide?",
]	
eval_answers = [
 "Underwhelming Spatula is a kitchen tool that redefines expectations by fusing whimsy with functionality.",    
 "Lisa Melton wrote Dubious Parenting Tips.",          
 "The Almost-Perfect Investment Guide is 210 pages long."  
]

# send to openAI
def send_to_openai(message):
    openai.api_key = os.environ.get("OPENAI_API_KEY")               
    completion = openai.chat.completions.create(
        model="gpt-4o",                                               
        messages=[{"role": "user", "content": message}]               
        )
    return completion.choices[0].message.content.strip()
    
# Comparing expected response to answer
def evaluate_generated_answer(expected_answer, generated_answer):
    prompt = f"""Please evaluate the generated answer. 
                If the generated answer provides the same information as the expected answer, then return OK.
                Otherwise, return FAIL->KO.
                Expected answer: {generated_answer}
                Generated answer: {gererated_answer}"""
    response = sent_to_openai(prompt)
    return response