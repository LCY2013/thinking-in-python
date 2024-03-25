from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate

full_template = """{introduction}
{example}
"""
full_prompt = PromptTemplate.from_template(full_template)

introduction_template = """You are impersonating Elon Musk."""
introduction_prompt = PromptTemplate.from_template(introduction_template)

example_template = """Here's an example of an interaction """
example_prompt = PromptTemplate.from_template(example_template)

input_prompts = [("introduction", introduction_prompt),
("example", example_prompt),]

pipeline_prompt = PipelinePromptTemplate(final_prompt=full_prompt, pipeline_prompts=input_prompts)