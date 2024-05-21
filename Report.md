# Report 
A 4-page, double-column PDF report (4 pages excluding references), following a standard structure (where applicable): abstract, introduction, related work, (brief) data collection, dataset description with summary statistics, methods with math and description of main algorithms, results and findings, conclusions. This report will be evaluated according to how clearly and succinctly it is written, if the style is appropriate (e.g., figures with captions), if it contains all relevant contents, and how solid the results are.

## Abstract 
Large Language Models are known for perpetuating if not amplifying the biases of society, but often the issues with analysing them are due to the lack of universalizability of the methods. This research will address the biases that occur in one of the most popular at LLM at the moment - ChatGPT to assess the differences in stereotypical bias between language. The language that will be analysed is latvian, as there is little research regarding this and as two people out of this research are Latvians. The method we want to use is mainly prompt probing. This method was chosen based on a literature review regarding various approaches. 

We would analyse ChatGPT-4o with prompts to analyse stereotypical implicit biases. This paper was chosen for replication based on the availability in data of the exact prompts that were used to investigate bias

Possibly cross validation between the prompts to analyse the 
differences. 

## Introduction

As LLMs are becoming more increasingly used in everyday life. There has arisen a need to detect and mitigate biases. There are various methods in how to approach this including creating new scores and data sets to gain better insight. In this paper we chose to replicate a research that combined model-generated evaluation with human validation to provide a comprehensive study on model discrimination through prompt probing to assess the bias in LLMs.

In hopes of answering the question : to what extent ChatGPT - 4o, Gemini, BLOOM, LLaMA2 show a difference in bias when encountering prompts in different languages?

The main focus is on ChatGPT as research using Context Association Tests to measure stereotypical biases by comparing how a model compares to an idealistic model showed that ChatGPT compared to other models exhibited more idealistic scores (Nadeem et al., 2020). Furthermore, this is the hottest topic at the moment has been analysing ChatGPT, which was the first to come out and the fastest company to gain a million users in a day. However, this company keeps growing both in users and its products. Just a few days ago OpenAI launched their newest model of ChatGPT that includes more languages as the company strives for accessibility.  




##  Background and Experimental Setup
...

## Method
...
Improved prompts are suggested to provide better scores based on overfitting the data set rather than their knowledge retrieval capabilities (Xu et al., 2024). 


## Prompt Biases 
...

A proposed way to mitigate negative impacts of prompt bias in factual knowledge extraction is by using the representation vector of prompt-only querying (Xu et al., 2024). Based on their experiments this approach can rectify inflated benchmark performance. 

## Discussion 
...

#### Mitigating bias 

* Reinforcement Learning regarding the mitigation of biases is quite interesting in training LLM’s. As it does not mitigate the biases, but only helps the user not gain unwanted answers. 


## Conclusion 
...


