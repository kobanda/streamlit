import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from streamlit import set_page_config

#make a dashboard and make the page wide config
set_page_config(layout='wide')
st.header("Impact of the AI on Inventory")

#bring in the data
df = pd.read_csv("intelligence.csv")
#st.write(df)
# data cleaning and mapping
#rename the culmns into short meaningful names

# Dictionary of new column names
new_column_names = {
    'Timestamp': 'timestamp',
    'Please confirm the following before proceeding:': 'consent_confirmed',
    'What is your role or job title?': 'job_title',
    'How long have you worked in your current position?': 'experience_years',
    'How long has your organization been using AI in inventory or supply chain management?': 'ai_use_duration',
    'What is the size of the company that you work in?': 'company_size',
    'Your organization primarily operate in which sector?': 'industry_sector',
    'Which AI technologies are currently implemented in your organization/Company?': 'ai_technologies_used',
    'Before implementing AI, What was your average inventory turnover ratio?': 'pre_ai_turnover_ratio',
    'Before implementing AI, on average, how many stockouts occurred per month?': 'pre_ai_stockouts',
    'Before implementing AI, what was your monthly cost of labor in inventory operations?': 'pre_ai_labor_cost',
    'Before implementing AI, what was your monthly logistics and transportation cost?': 'pre_ai_logistics_cost',
    'Before implementing AI, how frequently did you experience delayed order fulfilment?': 'pre_ai_delayed_orders',
    'After implementing AI, what is your current average inventory turnover ratio?': 'post_ai_turnover_ratio',
    'After Implementing AI, how many stockouts occur per month now?': 'post_ai_stockouts',
    'After implementing AI, What is your current monthly labor cost in inventory?': 'post_ai_labor_cost',
    'After implementing AI, what is your current monthly logistics and transportation cost?': 'post_ai_logistics_cost',
    'After implementing AI, how frequently do you now experience delayed order fulfilment?': 'post_ai_delayed_orders',
    'AI has significantly reduced inventory-related errors in your organization.': 'ai_error_reduction',
    'Your have experienced fewer stockouts since implementing AI': 'ai_fewer_stockouts',
    'AI-based replenishment is more flexible than your previous semi-automated system': 'ai_replenishment_flexibility',
    'Automation in your organization distribution centers has decreased both costs and wait times.': 'ai_automation_cost_time',
    'Your organization/Company has seen improvements in order fulfilment efficiency.': 'ai_fulfilment_efficiency',
    'Predictive analytics have improved your organization inventory forecasting accuracy': 'ai_forecasting_accuracy',
    'Initial setup costs were a significant barrier to adopting AI.': 'ai_setup_barrier',
    'Data privacy and security concerns influence your organization AI adoption decisions': 'ai_privacy_concerns',
    'AI systems are easy to use and integrate into existing operations in your organization/company': 'ai_usability',
    'I trust the recommendations provided by AI systems': 'ai_trust',
    'Your organization/company dependency on AI systems has grown over time.': 'ai_dependency_growth',
    'AI helps your company/organization identify and prevent overstocking and spoilage': 'ai_prevent_overstock',
    'What factors influenced your organization’s decision to adopt or not adopt AI for inventory management?': 'ai_adoption_factors',
    'Would you recommend AI-based inventory systems to other organizations?': 'ai_recommendation',
    'AI tools have made your organization supply chain more resilient during disruptions.': 'ai_resilience',
    'How satisfied are you with the performance of AI in your supply chain management?': 'ai_satisfaction',
    'How would you rate your confidence in AI-based decision-making': 'ai_confidence',
    'In which areas has AI had the most significant positive impact in your organization?': 'ai_impact_areas',
    'Before implementing AI,how frequently did you experience delayed order fulfilment?': 'pre_ai_delayed_orders'
}


# Rename columns
# 2. Replace multiple spaces inside column names with a single space
df.columns = df.columns.str.replace(r'\s+', ' ', regex=True)
# 3. Fix specific typo (example: "ow frequently" -> "how frequently")
df.columns = df.columns.str.replace(' ow frequently', 'how frequently', regex=False)
df.columns = df.columns.str.strip()
df.rename(columns=new_column_names, inplace=True)

#repace the missing data with NaN
df.replace(['', ' ', 'NA', 'N/A', 'None', 'Missing', 'nan'], np.nan, inplace=True)
st.write(df.head())
#code the data
# company size
company_size_map = {
    'Less than 50 employees': 1,
    '50 - 200 Employees': 2,
    '200 - 400 Employees': 3,
    'More than 500 employees': 4
}
df['company_size_code']= df.company_size.map(company_size_map)
experience_map = {
    'Less than 1 year': 1,
    '1-2 years': 2,
    '3 - 5 years': 3,
    'More than 5 years': 4
}
df['experience_code'] = df['experience_years'].map(experience_map)
ai_duration_map = {
    'Less than 12 months': 1,
    '1 - 2 years': 2,
    '3 - 5 years': 3,
    'Over 5 Years': 4
}

df['ai_use_duration_code'] = df['ai_use_duration'].map(ai_duration_map)
pre_turnover_map = {
    'Less than 2': 1,
    '2 – 4': 2,
    '5 – 7': 3,
    '8 – 10': 4,
    'More than 10': 5,
    'Not Sure': 0  # Or use: np.nan if you prefer
}

df['pre_turnover_code'] = df['pre_ai_turnover_ratio'].map(pre_turnover_map)
stockout_map = {
    'None': 0,
    '1-2 times': 1,
    '3- 5 times': 2,
    'Over 5 times': 3,
    'Not Sure': 99  # or np.nan
}
df['pre_stockouts_code'] = df['pre_ai_stockouts'].map(stockout_map)

labor_cost_map = {
    'Less than $1,000': 1,
    '$1,000 – $4,999': 2,
    '$5,000 – $9,999': 3,
    '$10,000 – $19,999': 4,
    '$20,000 or more': 5,
    'Not sure': 0  # or np.nan
}
df['pre_labor_cost_code'] = df['pre_ai_labor_cost'].map(labor_cost_map)
logistics_cost = {
    'Less than $1,000': 1,
    '$1,000 – $4,999': 2,
    '$5,000 – $9,999': 3,
    '$10,000 – $19,999': 4,
    '$20,000 or more': 5,
    'Not sure': 0  # or np.nan
}
df['pre_ai_logistics_cost_code'] = df['pre_ai_logistics_cost'].map(logistics_cost)
# Define the mapping for frequency of delayed orders
delayed_order_map = {
    'Rarely': 1,
    'Occasionally': 2,
    'Frequently': 3,
    'Very Frequently': 4
}
# Apply it to your DataFrame (assuming the column is named correctly)
df['pre_delayed_orders_code'] = df['pre_ai_delayed_orders'].map(delayed_order_map)
# Define the mapping for post-AI inventory turnover ratio
turnover_map = {
    'Less than 2': 1,
    '2 – 4': 2,
    '5 – 7': 3,
    '8 – 10': 4,
    'More than 10': 5,
    'Not sure': 0  # Or use np.nan for missing
}

# Apply the mapping
df['post_turnover_code'] = df['post_ai_turnover_ratio'].map(turnover_map)
post_stockouts_map = {
    'None': 0,
    '1 – 2 times': 1,
    '3 – 5 times': 2,
    '6 – 10 times': 3,
    'More than 10 times': 4,
    'Not sure': 5  # or use np.nan if treating as missing
}

df['post_stockouts_code'] = df['post_ai_stockouts'].map(post_stockouts_map)
labor_cost2_map = {
    'Less than $1,000': 1,
    '$1,000 – $4,999': 2,
    '$5,000 – $9,999': 3,
    '$10,000 – $19,999': 4,
    '$20,000 or more': 5,
    'Not sure': 0  # or np.nan
}
df['post_labor_cost_code'] = df['post_ai_labor_cost'].map(labor_cost2_map)
logistics_cost2 = {
    'Less than $1,000': 1,
    '$1,000 – $4,999': 2,
    '$5,000 – $9,999': 3,
    '$10,000 – $19,999': 4,
    '$20,000 or more': 5,
    'Not sure': 0  # or np.nan
}
df['post_ai_logistics_cost_code'] = df['post_ai_logistics_cost'].map(logistics_cost)
delayed_order2_map = {
    'Rarely': 1,
    'Occasionally': 2,
    'Frequently': 3,
    'Very Frequently': 4
}
# Apply it to your DataFrame (assuming the column is named correctly)
df['post_delayed_orders_code'] = df['post_ai_delayed_orders'].map(delayed_order_map)
# Define the mapping dictionary for ai_error_reduction
ai_error_reduction_map = {
    'Strongly Disagree': 1,
    'Disagree': 2,
    'Neutral': 3,
    'Agree': 4,
    'Strongly Agree': 5
}

# Apply the mapping to the DataFrame
df['ai_error_reduction_code'] = df['ai_error_reduction'].map(ai_error_reduction_map)
ai_fewer_stockouts_map = {
    'Strongly disagree': 1,
    'Disagree': 2,
    'Neutral': 3,
    'Agree': 4,
    'Strong Agree': 5
}

df['ai_fewer_stockouts_code'] = df['ai_fewer_stockouts'].map(ai_fewer_stockouts_map)
ai_replenishment_flexibility_map = {
    'Strongly disagree': 1,
    'Disagree': 2,
    'Neutral': 3,
    'Agree': 4,
    'Strongly agree': 5
}

df['ai_replenishment_flexibility_code'] = df['ai_replenishment_flexibility'].map(ai_replenishment_flexibility_map)
ai_automation_cost_time_map = {
    'Yes': 1,
    'No': 2,
    'Maybe': 3
}

df['ai_automation_cost_time_code'] = df['ai_automation_cost_time'].map(ai_automation_cost_time_map)
ai_fulfilment_efficiency_map = {
    'Strongly disagree': 1,
    'Disagree': 2,
    'Neutral': 3,
    'Agree': 4,
    'Strongly agree': 5
}

df['ai_fulfilment_efficiency_code'] = df['ai_fulfilment_efficiency'].map(ai_fulfilment_efficiency_map)
ai_forecasting_accuracy_map = {
    'Strongly disagree': 1,
    'Disagree': 2,
    'Neutral': 3,
    'Agree': 4,
    'Strongly agree': 5
}

df['ai_forecasting_accuracy_code'] = df['ai_forecasting_accuracy'].map(ai_forecasting_accuracy_map)
ai_setup_barrier_map = {
    'Yes': 1,
    'No': 2,
    'Maybe': 3
}

df['ai_setup_barrier_code'] = df['ai_setup_barrier'].map(ai_setup_barrier_map)
ai_privacy_concerns_map = {
    'Strongly disagree': 1,
    'Disagree': 2,
    'Neutral': 3,
    'Agree': 4,
    'Strongly agree': 5
}

df['ai_privacy_concerns_code'] = df['ai_privacy_concerns'].map(ai_privacy_concerns_map)
ai_usability_map = {
    'Strongly Disagree': 1,
    'Disagree': 2,
    'Neutral': 3,
    'Agree': 4,
    'Strongly Agree': 5
}

df['ai_usability_code'] = df['ai_usability'].map(ai_usability_map)
ai_trust_map = {
    'Stronly Disagree': 1,
    'Disagree': 2,
    'Neutral': 3,
    'Agree': 4,
    'Strongly Agree': 5
}

df['ai_trust_code'] = df['ai_trust'].map(ai_trust_map)
ai_dependency_growth_map = {
    'Strongly disagree': 1,
    'Disagree': 2,
    'Neutral': 3,
    'Agree': 4,
    'Strongly agree': 5
}

df['ai_dependency_growth_code'] = df['ai_dependency_growth'].map(ai_dependency_growth_map)
ai_prevent_overstock_map = {
    'Strongly disagree': 1,
    'Disagree': 2,
    'Neutral': 3,
    'Agree': 4,
    'Strongly agree': 5
}

df['ai_prevent_overstock_code'] = df['ai_prevent_overstock'].map(ai_prevent_overstock_map)
ai_recommendation_map = {
    'Yes': 1,
    'No': 2,
    'Maybe': 3
}

df['ai_recommendation_code'] = df['ai_recommendation'].map(ai_recommendation_map)
ai_resilience_map = {
    'Yes': 1,
    'No': 2,
    'Maybe': 3
}

df['ai_resilience_code'] = df['ai_resilience'].map(ai_resilience_map)
ai_satisfaction_map = {
    'Very Dissatisfied': 1,
    'Dissatisfied': 2,
    'Neutral': 3,
    'Satisfied': 4,
    'Very Satisfied': 5
}

df['ai_satisfaction_code'] = df['ai_satisfaction'].map(ai_satisfaction_map)
ai_confidence_map = {
    'Very Low': 1,
    'Low': 2,
    'Moderate': 3,
    'High': 4,
    'Very High': 5
}

df['ai_confidence_code'] = df['ai_confidence'].map(ai_confidence_map)
# Define mapping for post-AI inventory turnover ratio

for col in df:
    st.write(col)

# columns for analysis
cols_to_select = [
    'company_size_code',
    'experience_code',
    'ai_use_duration_code',
    'pre_turnover_code',
    'pre_stockouts_code',
    'pre_labor_cost_code',
    'pre_ai_logistics_cost_code',
    'pre_delayed_orders_code',
    'post_turnover_code',
    'post_stockouts_code',
    'post_labor_cost_code',
    'post_ai_logistics_cost_code',
    'post_delayed_orders_code',
    'ai_error_reduction_code',
    'ai_fewer_stockouts_code',
    'ai_replenishment_flexibility_code',
    'ai_automation_cost_time_code',
    'ai_fulfilment_efficiency_code',
    'ai_forecasting_accuracy_code',
    'ai_setup_barrier_code',
    'ai_privacy_concerns_code',
    'ai_usability_code',
    'ai_trust_code',
    'ai_dependency_growth_code',
    'ai_prevent_overstock_code',
    'ai_recommendation_code',
    'ai_resilience_code',
    'ai_satisfaction_code',
    'ai_confidence_code'
]
st.subheader('After implementing AI,  what is your current average inventory turnover ratio?')
#st.write(df[cols_to_select])
#lets see graph of stockouts
col1,col2 = st.columns(2)
plot_bar = px.bar(data_frame=df,
                   x='pre_ai_stockouts',
                   y='pre_stockouts_code',
                   title = 'Stockouts Before AI'
                   )
plot_bar2 = px.bar(data_frame=df,
                   x='post_ai_stockouts',
                   y='post_stockouts_code',
                   title = 'Stockouts After AI'
                   )
col3,col4 = st.columns(2)
plot_bar3 = px.bar(data_frame=df,
                   x='pre_ai_turnover_ratio',
                   y='pre_turnover_code',
                   title = 'Inventory Before AI'
                   )
plot_bar4 = px.bar(data_frame=df,
                   x='post_ai_turnover_ratio',
                   y='post_turnover_code',
                   title = 'Inventory After AI'
                   )
#show the graph
col1.plotly_chart(plot_bar)
col2.plotly_chart(plot_bar2)
col1.plotly_chart(plot_bar3)
col2.plotly_chart(plot_bar4)

