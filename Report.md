# Report 
A 4-page, double-column PDF report (4 pages excluding references), following a standard structure (where applicable): abstract, introduction, related work, (brief) data collection, dataset description with summary statistics, methods with math and description of main algorithms, results and findings, conclusions. This report will be evaluated according to how clearly and succinctly it is written, if the style is appropriate (e.g., figures with captions), if it contains all relevant contents, and how solid the results are.

## Abstract 
Large Language Models are known for perpetuating if not amplifying the biases of society, but often the issues with analysing them are due to the lack of universalizability of the methods. This research will address the biases that occur in one of the most popular at LLM at the moment - ChatGPT to assess the differences in stereotypical bias between language. The language that will be analysed is latvian, as there is little research regarding this and as two people out of this research are Latvians. The method we want to use is mainly prompt probing, which is one of the most popular methods for evaluating task specific tasks. This method was chosen based on a literature review regarding various approaches. 

We would analyse ChatGPT-4o with prompts to analyse stereotypical implicit biases. This paper was chosen for replication based on the availability in data of the exact prompts that were used to investigate bias

Possibly cross validation between the prompts to analyse the 
differences. 

## Introduction

As LLMs are becoming more increasingly used in everyday life. There has arisen a need to detect and mitigate biases. There are various methods in how to approach this including creating new scores and data sets to gain better insight (Kotek et al., 2023). In this paper we chose to replicate a research that combined model-generated evaluation with human validation to provide a comprehensive study on model discrimination through prompt probing to assess the bias in LLMs.

In hopes of answering the question : to what extent ChatGPT - 4o, Gemini, BLOOM, LLaMA2 show a difference in bias when encountering prompts in different languages?

The main focus is on ChatGPT as research using Context Association Tests to measure stereotypical biases by comparing how a model compares to an idealistic model showed that ChatGPT compared to other models exhibited more idealistic scores (Nadeem et al., 2020). Furthermore, this is the hottest topic at the moment has been analysing ChatGPT, which was the first to come out and the fastest company to gain a million users in a day. However, this company keeps growing both in users and its products. Just a few days ago OpenAI launched their newest model of ChatGPT that includes more languages as the company strives for accessibility.  Nonetheless, there is a wide gap between smaller open-source models and larger ones based on the systems performance from both the system and user perspective, which could be explored further (Sun et al., 2023). 



##  Background and Experimental Setup
...


## Method
#### Theoretical background 
#### Experimental setup 

...
Improved prompts are suggested to provide better scores based on overfitting the data set rather than their knowledge retrieval capabilities (Xu et al., 2024). 


## Prompt Biases 
...

Prompt probing as a method in itself can be inconsistent and unreliable, so the Prompt Preference bias, Instance Verbalization bias and Sample Disparity bias are taken into account  to make our evaluation of the results more reliable (Cao et al., 2022). 


## Discussion 
...

#### Mitigating bias 
A proposed way to mitigate negative impacts of prompt bias in factual knowledge extraction is by using the representation vector of prompt-only querying (Xu et al., 2024). Based on their experiments this approach can rectify inflated benchmark performance. 

Reinforcement Learning regarding the mitigation of biases is quite interesting in training LLM’s. As it does not mitigate the biases, but only helps the user not gain unwanted answers. 


## Conclusion 
...




### References 
References Cao, B., Lin, H., Han, X., Liu, F., & Sun, L. (2022). Can Prompt Probe Pretrained Language Models? Understanding the Invisible Risks from a Causal View. https://arxiv.org/pdf/2203.12258Kotek  
H., Dockum, R., & Sun, D. (2023). Gender bias and stereotypes in Large Language Models. Proceedings of the ACM Collective Intelligence Conference. https://doi.org/10.1145/3582269.3615599Nadeem   
M., Bethke, A., & Reddy, S. (2020). StereoSet: Measuring stereotypical bias in pretrained language models. https://arxiv.org/pdf/2004.09456Sun   
D. Q., Abzaliev, A., Kotek, H., Xiu, Z., Klein, C., & Williams, J. D. (2023, November 7). DELPHI: Data for Evaluating LLMs’ Performance in Handling Controversial Issues. ArXiv.org. https://doi.org/10.48550/arXiv.2310.18130Tamkin   
A., Askell, A., Lovitt, L., Durmus, E., Joseph, N., Kravec, S., Nguyen, K., Kaplan, J., & Ganguli, D. (2023). Evaluating and Mitigating Discrimination in Language Model Decisions. In  arXiv.org. https://doi.org/10.48550/arxiv.2312.03689Xu   
Z., Peng, K., Ding, L., Tao, D., & Lu, X. (2024). Take Care of Your Prompt Bias! Investigating and Mitigating Prompt Bias in Factual Knowledge Extraction. https://arxiv.org/pdf/2403.09963v1
