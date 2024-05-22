# Report 
A 4-page, double-column PDF report (4 pages excluding references), following a standard structure (where applicable): abstract, introduction, related work, (brief) data collection, dataset description with summary statistics, methods with math and description of main algorithms, results and findings, conclusions. This report will be evaluated according to how clearly and succinctly it is written, if the style is appropriate (e.g., figures with captions), if it contains all relevant contents, and how solid the results are.

## Abstract 
Large Language Models are known for perpetuating, if not amplifying, the biases of society, but often the issues with analysing them are due to the lack of universalizability (???) of the methods. This research will address the biases that occur in one of the most popular at LLM at the moment - ChatGPT, to assess the differences in stereotypical bias between two languages. The language that will be analysed is Latvian, as there is little research regarding thi,s and as two people out of this research group are Latvians. The method we want to use is mainly prompt probing, which is one of the most popular methods for evaluating task specific use ccases. This method was chosen based on a literature review regarding various approaches. 

We would analyse ChatGPT-4o with prompts acquired from to Tamkin et al. (2023), with an aim to analyse stereotypical implicit biases. This paper was chosen for replication based on the availability in data of the exact prompts used.



## Introduction

As LLMs are becoming more increasingly used in everyday life. There has arisen a need[??] to detect and mitigate biases. There are various methods in how to approach this including creating new scores and data sets to gain better insight (Kotek et al., 2023). In this paper we chose to replicate a research that combined model-generated evaluation with human validation to provide a comprehensive study on model discrimination through prompt probing to assess the bias in LLMs.

In hopes of answering the question : to what extent ChatGPT-4o (and/or alternatively Gemini, BLOOM, LLaMA2) exhibits a difference in bias when encountering prompts in Latvian compared to English?

[what does this sentence even mean] _The main focus is on ChatGPT as research using Context Association Tests to measure stereotypical biases by comparing how a model compares to an idealistic model showed that ChatGPT compared to other models exhibited more idealistic scores (Nadeem et al., 2020)_. Additionally, the analysis of ChatGPT has been acquiring the most attention due to the model's swift growth in popularity, with record-breaking one million users acquired within a day. Along with the increasing number of users, ChatGPT has also undergone substantial enhancements, exemplified by the recent release of GPT-4o that is said to include more languages, achieving increased accessibility.  Nonetheless, there is a wide gap between smaller open-source models and larger ones based on the systems performance from both the system and user perspective, which could be explored further (Sun et al., 2023). 



##  Background and Experimental Setup


## Method
#### Theoretical background 
Tamkin et al. (2023) presented a method for evaluating and quantifying discriminatory outputs from LMs, specifically testing Claude 2.0 model. Their work focused on identifying and mitigating bias using English prompts for various decision-making scenarios. This study seeks to replicate and extend their research by assessing Chat-GPT4o on the difference in exhibited bias between English and Latvian. Considering the global population of Latvian speakers being less than 2 million, in contrast to an estimated 1.45 billion English speakers worldwide, language models are equipped with a significantly larger corpus of training data in English. As a result, they exhibit superior performance when processing English prompts, while smaller-scale languages remain significantly more prone to amplifying cultural stereotypes. Understanding bias in multilingual LMs is crucial for ensuring fair and ethical applications across diverse languages and directing efforts to mitigate and prevent discrimination from becoming codified with the increased use of algorithms across various industries.

#### Experimental setup 

We will utilize the existing dataset of prompts developed by Tamkin et al. (2023), encompassing over 90 diverse topic areas for realistic decision-making scenarios. These prompts have been validated by a human evaluation study, achieving high ratings on quality. The prompts will be translated into grammatically accurate and culturally appropriate Latvian by using Google API, and then cross-evaluated by two native Latvian speakers to ensure a reliable translation. The resulting dataset will comprise of **NUMBER** prompts (... in English, ... in Latvian) covering a range of decision-making domains, both high-risk (like loan approvals, employment opportunities, and criminal justice) and low-risk (such as approving a merchandise return). Each prompt will contain placeholders for varying demographic information (e.g., name, age, location) to assess potential bias based on these attributes.
We will employ ChatGPT4o to evaluate the translated prompts and output a yes/no decision, with "yes" being the favourable outcome for the hypothetical person in question. The model's outputs will be analyzed using the discrimination score metric outlined by Tamkin et al. (2023). This score quantifies the degree of bias exhibited by the model's decisions based on demographic variations within the prompts.
...
[???? ] Improved prompts are suggested to provide better scores based on overfitting the data set rather than their knowledge retrieval capabilities (Xu et al., 2024). 

The primary algorithm used will be the built-in processing capabilities of ChatGPT4o. We will not be modifying the internal algorithms of the model itself. The focus will be on analyzing the model's outputs for potential bias based on the translated prompts. Each prompt (English and Latvian) will be fed individually to a new session of ChatGPT4o to eliminate influence across prompts. 

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
Tamkin, A., Askell, A., Lovitt, L., Durmus, E., Joseph, N., Kravec, S., Nguyen, K., Kaplan, J., & Ganguli, D. (2023). Evaluating and Mitigating Discrimination in Language Model Decisions. ArXiv (Cornell University). https://doi.org/10.48550/arxiv.2312.03689
