from src.crew import financial_trading_crew

financial_trading_inputs = {
    'stock_selection': 'Wipro',
    'initial_capital': '10000',
    'risk_tolerance': 'Medium',
    'trading_strategy_preference': 'Day Trading',
    'news_impact_consideration': True
}

if __name__ == "__main__":
    result = financial_trading_crew.kickoff(inputs=financial_trading_inputs)
    print(result)