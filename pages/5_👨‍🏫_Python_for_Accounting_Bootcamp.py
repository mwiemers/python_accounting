import streamlit as st
import pandas as pd
from load_css import local_css


st.set_page_config(
    page_title='Python Workshop Format',
    page_icon='👨‍🏫'
)

local_css("css/style.css")

st.title("Python for Accounting Bootcamp Format")

st.markdown("""

## Python for Accounting Bootcamp Format
            
### Workshop Format

The primary focus of our workshops is to support you in developing skills and strategies that will enable you to continue to learn programming 
and related digital skills independently. Our lessons are designed as projects which are broken down into a series of smaller, more maneagble tasks. 
To solve these tasks, you will use the same resources that coders around the world rely on when they don't know how to do something – 
online resources/tools, colleagues, and trial and error.
            
This bootcamp runs from 10-5pm. We will run an introduction session to explain the format of the bootcamp and run regular reviews to
ensure that everyone is at the same pace.

| Time          | Topic                                            |
| ------------- | ------------------------------------------------ |
| 10:20 – 11:20 | Part 1 - Plotting Stock Prices                   |
| 11:20 – 12:30 | Part 2 - Calculating Returns                     |
| 12:30 – 13:30 | Lunch break                                      |
| 13:30 – 15:00 | Part 3 - Complex Return Plot                     |
| 15:00 – 17:00 | Part 4 - Margins Plot using Financial Statements |

            
Each of the notebooks will take you roughly 1 hour to complete. By the end of this bootcamp everyone should have completed all four projects.
            
""",
    unsafe_allow_html=True
)
