# Report 
A 4-page, double-column PDF report (4 pages excluding references), following a standard structure (where applicable): abstract, introduction, related work, (brief) data collection, dataset description with summary statistics, methods with math and description of main algorithms, results and findings, conclusions. This report will be evaluated according to how clearly and succinctly it is written, if the style is appropriate (e.g., figures with captions), if it contains all relevant contents, and how solid the results are.


## Abstract (300 words)
Large Language Models are known for perpetuating (if not – amplifying) the prejudices existing in society, yet still not enough has been done in the direction of bias prevention. Algorithms are being deployed in each sector of life, from high-impact fields such as crime prevention, finance and immigration, to everyday matters such as retail. but often the issues with analysing them are due to the lack of universalizability (???) of the methods. 

This research will address the stereotypical biases exhibited by one of the most popular language models - ChatGPT, with the aim of quantifying the difference between two languages – English and Latvian. We have chosen these languages in particular, due to the enormous contrast in training data - English being the primary language of most (if not all) popular language models, while Latvian being almost entirely excluded from them. Furthermore, 2 of our group members are native Latvian speakers, therefore they have the necessary insight and language skills to oversee the translation and comparison. The method we have chosen for our study is prompt probing, following the example of Tamkin et al. (2023), thanks to its feasibility within our time and skillset. We have attempted to analyse ChatGPT-3 with prompts acquired from Tamkin et al., testing both explicit and implicit bias in binary decisions.



## Introduction (500 words)

As LLMs are becoming increasingly used in everyday life. There has arisen a need [??] to detect and mitigate biases. There are various methods in how to approach this including creating new scores and data sets to gain better insight (Kotek et al., 2023). In this paper we chose to replicate a research that combined model-generated evaluation with human validation to provide a comprehensive study on model discrimination through prompt probing to assess the bias in LLMs.

In hopes of answering the question : to what extent ChatGPT-4o (and/or alternatively Gemini, BLOOM, LLaMA2) exhibits a difference in bias when encountering prompts in Latvian compared to English?

[what does this sentence even mean] _The main focus is on ChatGPT as research using Context Association Tests to measure stereotypical biases by comparing how a model compares to an idealistic model showed that ChatGPT compared to other models exhibited more idealistic scores (Nadeem et al., 2020)_. Additionally, the analysis of ChatGPT has been acquiring the most attention due to the model's swift growth in popularity, with record-breaking one million users acquired within a day. Along with the increasing number of users, ChatGPT has also undergone substantial enhancements, exemplified by the recent release of GPT-4o that is said to include more languages, achieving increased accessibility.  Nonetheless, there is a wide gap between smaller open-source models and larger ones based on the systems performance from both the system and user perspective, which could be explored further (Sun et al., 2023). 

They address the main issues with prompt probing by explaining the biases that play a role in the method itself. With also emphasizing the uncertainty that this method has and that it often does not even represent testing knowledge-related tasks (Cao et al., 2022). 



## Method (1500 words)
[what? how is that relevant for us] As prompt probing exibits biases a simpler method has been proposed to universalise the best probing criteria, when investigating factual knowledge probing (Cao et al., 2022). 



#### Theoretical background 
Tamkin et al. (2023) presented a method for evaluating and quantifying discriminatory outputs from LMs, specifically testing Claude 2.0 model. Their work focused on identifying and mitigating bias using English prompts for various decision-making scenarios. This study seeks to replicate and extend their research by assessing Chat-GPT4o on the difference in exhibited bias between English and Latvian. Considering the global population of Latvian speakers being less than 2 million, in contrast to an estimated 1.45 billion English speakers worldwide, language models are equipped with a significantly larger corpus of training data in English. As a result, they exhibit superior performance when processing English prompts, while smaller-scale languages remain significantly more prone to amplifying cultural stereotypes. Understanding bias in multilingual LMs is crucial for ensuring fair and ethical applications across diverse languages and directing efforts to mitigate and prevent discrimination from becoming codified with the increased use of algorithms across various industries.

#### Experimental setup 

We will utilize the existing dataset of prompts developed by Tamkin et al. (2023), encompassing over 90 diverse topic areas for realistic decision-making scenarios. These prompts have been validated by a human evaluation study, achieving high ratings on quality. The prompts will be translated into grammatically accurate and culturally appropriate Latvian by using Google API, and then cross-evaluated by two native Latvian speakers to ensure a reliable translation. The resulting dataset will comprise of **NUMBER** prompts (... in English, ... in Latvian) covering a range of decision-making domains, both high-risk (like loan approvals, employment opportunities, and criminal justice) and low-risk (such as approving a merchandise return). Each prompt will contain placeholders for varying demographic information (e.g., name, age, location) to assess potential bias based on these attributes.
We will employ ChatGPT4o to evaluate the translated prompts and output a yes/no decision, with "yes" being the favourable outcome for the hypothetical person in question. The model's outputs will be analyzed using the discrimination score metric outlined by Tamkin et al. (2023). This score quantifies the degree of bias exhibited by the model's decisions based on demographic variations within the prompts.

The primary algorithm used will be the built-in processing capabilities of BLOOM. We will not be modifying the internal algorithms of the model itself. 

The focus will be on analying the model's outputs for potential bias based on the translated prompts. Each prompt (English and Latvian) will be fed individually to a new session of ChatGPT4o to eliminate influence across prompts. 
After collecting the outputs in a dataframe, we will employ the mixed effects model, as outlined in the original study, or, alternatively a simplified version consisting of the average difference in logit transformed probability of a positive decision between advantaged and disadvantaged groups for each prompt.
Finally, we will conduct a statistical hypothesis test (for example a paired t-test) to compare the mean discrimination scores between English and Latvian prompts. This will determine if there is a statistically significant difference in the level of bias exhibited by the model across languages.

## Prompt Biases (500 words)
Prompt probing as a method in itself can be inconsistent and unreliable, so the Prompt Preference bias, Instance Verbalization bias and Sample Disparity bias are taken into account to make our evaluation of the results more reliable (Cao et al., 2022). 

## Discussion (750 words)
A few issues that were noticed during the research will be addressed in this section.

#### Limitations of the experiment. 
At the initial start of this project we discussed analysing popularly used models as ChatGPT. However, as most of these models are owned by companies they are not attainable for public use. This lead us to deviate to pre-trained open-source models that could be found on Hugging Face. 

The evaluation of the prompts was only done by two bachelor students that are native speakers, who are not specialists in linguistics in any way. Thus there could have been mistakes that went unnoticed, without taking into account various dialects that the language has as well. 


### Mitigating bias (300 words)
A proposed way to mitigate negative impacts of prompt bias in factual knowledge extraction is by using the representation vector of prompt-only querying (Xu et al., 2024). Based on their experiments this approach can rectify inflated benchmark performance. 

Reinforcement Learning regarding the mitigation of biases is quite interesting in training LLM’s. As it does not mitigate the biases, but only helps the user not gain unwanted answers. 


## Conclusion (150 words)
...





### References 
References Cao, B., Lin, H., Han, X., Liu, F., & Sun, L. (2022). Can Prompt Probe Pretrained Language Models? Understanding the Invisible Risks from a Causal View. https://arxiv.org/pdf/2203.12258Kotek  
H., Dockum, R., & Sun, D. (2023). Gender bias and stereotypes in Large Language Models. Proceedings of the ACM Collective Intelligence Conference. https://doi.org/10.1145/3582269.3615599Nadeem   
M., Bethke, A., & Reddy, S. (2020). StereoSet: Measuring stereotypical bias in pretrained language models. https://arxiv.org/pdf/2004.09456Sun   
D. Q., Abzaliev, A., Kotek, H., Xiu, Z., Klein, C., & Williams, J. D. (2023, November 7). DELPHI: Data for Evaluating LLMs’ Performance in Handling Controversial Issues. ArXiv.org. https://doi.org/10.48550/arXiv.2310.18130Tamkin   
A., Askell, A., Lovitt, L., Durmus, E., Joseph, N., Kravec, S., Nguyen, K., Kaplan, J., & Ganguli, D. (2023). Evaluating and Mitigating Discrimination in Language Model Decisions. In  arXiv.org. https://doi.org/10.48550/arxiv.2312.03689Xu   
Z., Peng, K., Ding, L., Tao, D., & Lu, X. (2024). Take Care of Your Prompt Bias! Investigating and Mitigating Prompt Bias in Factual Knowledge Extraction. https://arxiv.org/pdf/2403.09963v1
Tamkin, A., Askell, A., Lovitt, L., Durmus, E., Joseph, N., Kravec, S., Nguyen, K., Kaplan, J., & Ganguli, D. (2023). Evaluating and Mitigating Discrimination in Language Model Decisions. ArXiv (Cornell University). https://doi.org/10.48550/arxiv.2312.03689



### Author contributions:
Mara: literature review, writing the introduction and the abstract
Michalina: formulating the research question, choosing the study design and methodology
Ralfs: translations of prompts into Latvian
