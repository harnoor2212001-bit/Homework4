import json
import sys
from datetime import datetime

def calculate_debt_metrics(debt_list):
    today = datetime.now()
    total_principal = 0
    weighted_sum = 0
    results = []

    for item in debt_list:
        try:
            # Parse date and calculate days remaining
            m_date = datetime.strptime(item['maturity_date'], '%m/%d/%Y')
            days_left = (m_date - today).days
            
            # Aggregate data for weighted average
            principal = float(item['principal'])
            rate = float(item['interest_rate'].replace('%', '')) / 100
            
            total_principal += principal
            weighted_sum += (principal * rate)
            
            results.append({
                "name": item['name'],
                "principal": f"${principal:,.2f}",
                "days_to_maturity": days_left,
                "bucket": "Current" if days_left < 365 else "Long-term"
            })
        except Exception as e:
            results.append({"name": item.get('name', 'Unknown'), "error": str(e)})

    w_avg_rate = (weighted_sum / total_principal) if total_principal > 0 else 0
    
    return {
        "analysis": results,
        "weighted_average_interest_rate": f"{w_avg_rate:.4%}",
        "total_outstanding_principal": f"${total_principal:,.2f}"
    }

if __name__ == "__main__":
    # The agent passes a JSON string via stdin
    input_data = json.load(sys.stdin)
    output = calculate_debt_metrics(input_data)
    print(json.dumps(output, indent=2))