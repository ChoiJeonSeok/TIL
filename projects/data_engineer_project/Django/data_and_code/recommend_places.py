import pandas as pd
import random

# Load the data
data = pd.read_csv('국민여행조사데이터_20230724.csv')

def recommend_places(data, gender, age, companion):
    # Filter data based on the input
    filtered_data = data[(data['성별'] == gender) & 
                        (data['연령대'] == age) & 
                        (data['동반자유형'] == companion)]
    
    # Sort by rating and select top 15
    top_places = filtered_data.sort_values('평점', ascending=False).head(15)
    
    # Randomly select 5 places
    recommended_places = top_places.sample(5)
    
    return recommended_places

# Test the function
# recommended_places = recommend_places(data, '남', '20대', '비가족')
# recommended_places_cities = recommended_places['시군구'].tolist()
# recommended_places_cities