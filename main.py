import json
import openai
import pandas as pandas
import matplotlib.pyplot as plt
import streamlit as st
import yfinance as yf

openai.API_KEY = open('API_KEY', 'r').read()
