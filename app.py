from openai import OpenAI

#Bring in the stock prices function

from stock_data import get_stock_prices

import streamlit as st


#Bring the instructor library
import instructor

#Bring in the Base Model class
from pydantic import BaseModel

# Create a client
client=OpenAI(
    api_key='jhjhjhjh1233',
    base_url='http://localhost:8000/v1'
)

#Create a patched client
client=instructor.patch(client=client)

#structure what we want to extract
class ResponseModel(BaseModel):
    ticker:str
    days:int

st.title('Fake OpenAI Server')

prompt=st.chat_input('Pass your prompt here')

# if the user types a prompt and hit enter
if prompt:
    st.chat_message('user').markdown(prompt)


# Function calling LLM call

response=client.chat.completions.create(
    # which model we want to use
    model="mistral-function-calling",

    # pass through our prompt

    messages=[{
        'role':'user',
         'content':prompt
    }],

    #Add stream
    # stream=True

    response_model=ResponseModel,

    
)

st.chat_message("ai").markdown(response)

try:
    prices=get_stock_prices(response.ticker,response.days)
    st.chat_message("ai").markdown(prices)

    # summary output + prices
    fullresponse=client.chat.completions.create(
    # which model we want to use
        model="mixtral",

        # pass through our prompt

        messages=[{
            'role':'user',
            'content':prompt+"\n"+str(prices) # important prices should be string
        }],

        #Add stream
        stream=True
    )
    with st.chat_message('ai'):
        completed_message=""
        message=st.empty()
        for chunk in fullresponse:
        #if the value is not none print it out
            if chunk.choices[0].delta.content is not None:
                completed_message+=chunk.choices[0].delta.content
                message.markdown(completed_message)

except:
    st.chat_message("ai").markdown("Something went wrong")

# with st.chat_message('ai'):
#     completed_message=""
#     message=st.empty()
#     for chunk in response:
#     #if the value is not none print it out
#         if chunk.choices[0].delta.content is not None:
#             completed_message+=chunk.choices[0].delta.content
#             message.markdown(completed_message)


#Streaming the response out

    
#print it out 
# print(response.choices[0].message.content)
