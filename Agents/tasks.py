from crewai import Task
from tools import tool
from agents import news_research_agent, news_writer

research_task = Task(
    description = ("""Identify the next big trend in {topic}.
                   Focus on identifying pros and cons and the overall narratives.
                   Your finall report should clearly articulate  the key points,
                   its market opportunity and potential impact on the industry"""),
    expected_output = "a comprehensive 3 paragraphs long report on the latest AI trends.",
    tools = [],
    agent = news_research_agent
)
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=news_writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)