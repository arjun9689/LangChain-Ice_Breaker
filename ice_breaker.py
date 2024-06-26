from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChains

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

def ice_breaker_with(name:str) -> str:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)
    summary_template = """
        given the information {information} about a person I want to create:
        1. A short summary
        2. two interesting facts about them
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    chain = LLMChains(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/nagarjun-s-b8470343/")

    res = chain.invoke(input={"information": linkedin_data})

    print(res)



if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker Enter")
    ice_breaker_with(name="Eden Marco")

