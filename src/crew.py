from crewai import Crew, Process
from .agents import data_analyst_agent, trading_strategy_agent, execution_agent, risk_management_agent
from .tasks import data_analysis_task, strategy_development_task, execution_planning_task, risk_assessment_task
from .config import LLM

financial_trading_crew = Crew(
    agents=[data_analyst_agent, trading_strategy_agent, execution_agent, risk_management_agent],
    tasks=[data_analysis_task, strategy_development_task, execution_planning_task, risk_assessment_task],
    manager_llm=LLM,
    process=Process.hierarchical,
    verbose=True
)