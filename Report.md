# Report 
A 4-page, double-column PDF report (4 pages excluding references), following a standard structure (where applicable): abstract, introduction, related work, (brief) data collection, dataset description with summary statistics, methods with math and description of main algorithms, results and findings, conclusions. This report will be evaluated according to how clearly and succinctly it is written, if the style is appropriate (e.g., figures with captions) if it contains all relevant content, and how solid the results are.


## Abstract (300 words, but is not part of eord count!)
Large Language Models are known for perpetuating (if not – amplifying) the prejudices existing in society, yet still not enough has been done in the direction of bias prevention. Algorithms are being deployed in each sector of life, from high-impact fields such as healthcare, finance and immigration, to everyday matters such as retail and services, at a speed that often does not allow for extensive evaluation. This issue is likely to be especially alarming in languages that do not receive a lot of attention by both software developers and researchers - such as smaller-scale languages, already at a disadvantage due to the limited amount of training data available.
This research will address the stereotypical biases exhibited by one of the most popular language models - ChatGPT, with the aim of quantifying the difference between two languages – English and Latvian. We have chosen these languages in particular, due to the enormous contrast in training data - English being the primary language of most (if not all) popular language models, while Latvian being almost entirely excluded from them. Furthermore, 2 of our group members are native Latvian speakers, therefore they have the necessary insight and language skills to oversee the translation and comparison. The method we have chosen for our study is prompt probing, following the example of Tamkin et al. (2023), thanks to its feasibility within our time and skillset. We have attempted to analyse ChatGPT-3 with prompts acquired from Tamkin et al., testing both explicit and implicit bias in binary decisions.



## Introduction (500 words)

As LLMs are becoming increasingly used in everyday life. There has arisen a need [??] to detect and mitigate biases. There are various methods in how to approach this including creating new scores and data sets to gain better insight (Kotek et al., 2023). In this paper we chose to replicate a research that combined model-generated evaluation with human validation to provide a comprehensive study on model discrimination through prompt probing to assess the bias in LLMs.

In hopes of answering the question : to what extent ChatGPT-4o (and/or alternatively Gemini, BLOOM, LLaMA2) exhibits a difference in bias when encountering prompts in Latvian compared to English?

[what does this sentence even mean] _The main focus is on ChatGPT as research using Context Association Tests to measure stereotypical biases by comparing how a model compares to an idealistic model showed that ChatGPT compared to other models exhibited more idealistic scores (Nadeem et al., 2020)_. Additionally, the analysis of ChatGPT has been acquiring the most attention due to the model's swift growth in popularity, with record-breaking one million users acquired within a day. Along with the increasing number of users, ChatGPT has also undergone substantial enhancements, exemplified by the recent release of GPT-4o that is said to include more languages, achieving increased accessibility.  Nonetheless, there is a wide gap between smaller open-source models and larger ones based on the systems performance from both the system and user perspective, which could be explored further (Sun et al., 2023). 

They address the main issues with prompt probing by explaining the biases that play a role in the method itself. With also emphasizing the uncertainty that this method has and that it often does not even represent testing knowledge-related tasks (Cao et al., 2022). 


## Theoretical background (500 words)

Research suggested that to do suface-level evaluations of the preformance of LLMs form both systems and user perspective is done by using data sets, and with most they also created new metrics to evaluate the biases that the models exhibit, for example with the SterioSet created an idealized score that compared the model to an idealistic model (Sun et al., 2023, Kotek et al., 2023, Smith et al., 2022, Nadeem et al., 2020). Howevere, some maily focused on the evaluation of preformance by using these newly created scores (Sun et al., 2023) rather than focusing on the quantification of biases. Others, that did quantify biases, focused on a singular one for the evaluation (Kotek et al., 2023). Another method that was not rooted in data sets was a model-free approach, which is when probing is used as a prompting task in the hopes of not leveraging any specific knowlegde (Li et al., 2022). Sadly some research suggests that this is only useful to identify embedded linguistic properties, thus it is a surface-level analysis that misses propagated biases in the models and would be insufficient for causality analysis as it lacks the understanding of why and how biases occur. 
... 

As the intent was to eplore multiple biases, the focus was narrowed down to a popular approach .. prompt probing (???).  


Tamkin et al. (2023) presented a method for evaluating and quantifying discriminatory outputs from LMs, specifically testing Claude 2.0 model. Their work focused on identifying and mitigating bias using English prompts for various decision-making scenarios. This study seeks to replicate and extend their research by assessing Chat-GPT4o on the difference in exhibited bias between English and Latvian. Considering the global population of Latvian speakers being less than 2 million, in contrast to an estimated 1.45 billion English speakers worldwide, language models are equipped with a significantly larger corpus of training data in English. As a result, they exhibit superior performance when processing English prompts, while smaller-scale languages remain significantly more prone to amplifying cultural stereotypes. Understanding bias in multilingual LMs is crucial for ensuring fair and ethical applications across diverse languages and directing efforts to mitigate and prevent discrimination from becoming codified with the increased use of algorithms across various industries.

##  Mthology : Experimental setup (750 words)

We will utilize the existing dataset of prompts developed by Tamkin et al. (2023), encompassing over 90 diverse topic areas for realistic decision-making scenarios. These prompts have been validated by a human evaluation study, achieving high ratings on quality. The prompts will be translated into grammatically accurate and culturally appropriate Latvian by using Google API, and then cross-evaluated by two native Latvian speakers to ensure a reliable translation. The resulting dataset will comprise of **NUMBER** prompts (... in English, ... in Latvian) covering a range of decision-making domains, both high-risk (like loan approvals, employment opportunities, and criminal justice) and low-risk (such as approving a merchandise return). Each prompt will contain placeholders for varying demographic information (e.g., name, age, location) to assess potential bias based on these attributes.
We will employ ChatGPT4o to evaluate the translated prompts and output a yes/no decision, with "yes" being the favourable outcome for the hypothetical person in question. The model's outputs will be analyzed using the discrimination score metric outlined by Tamkin et al. (2023). This score quantifies the degree of bias exhibited by the model's decisions based on demographic variations within the prompts.

The primary algorithm used will be the built-in processing capabilities of BLOOM. We will not be modifying the internal algorithms of the model itself. 

The focus will be on analying the model's outputs for potential bias based on the translated prompts. Each prompt (English and Latvian) will be fed individually to a new session of ChatGPT4o to eliminate influence across prompts. 
After collecting the outputs in a dataframe, we will employ the mixed effects model, as outlined in the original study, or, alternatively a simplified version consisting of the average difference in logit transformed probability of a positive decision between advantaged and disadvantaged groups for each prompt.
Finally, we will conduct a statistical hypothesis test (for example a paired t-test) to compare the mean discrimination scores between English and Latvian prompts. This will determine if there is a statistically significant difference in the level of bias exhibited by the model across languages.


## The results (450 words)
... 

## Analysis of results (300 words)
... 



## Discussion (750 words)
A few issues that were noticed during the research as well as possible solutions will be addressed in this section.

#### Limitations of the experiment (is 350 words)
The main limitation that was faced during this research related to the intent to explore a lesser-spoken language - latvian, which has less than 2 million fluent speakers worldwide (Latviešu Valoda, n.d.). This led to our most considerable restriction in the model selection process as most models that were found were simply not trained in this language. Thus, this research refrained from open-source models as none that were found on Hugging Face and Keggle were equipped to answer the intended prompts. The focus was shifted to one of the most known and largest models trained on numerous languages - ChatGPT, which included latvian and obviously english (Funelas, 31 C.E.). Further the explicit selection of using ChatGPT3.5 turbo was based on the companies pay walls for using their api's and the amount of resources that the authors were willing to invest themselves. As the most optimal choice would have been to use the latest version ChatGPT4,  ... bit this was more expensive ???

The amount of resources also influenced the evaluation of the prompts. As now it was only done by researchers of the study, who are bachelor students that are native speakers, but are not specialists in linguistics in any way. Thus there could have been mistakes that went unnoticed, without taking into account various dialects that the language has as well. 

Another limitation was the amount of time that was allocated to this research as this was a project for a Text Mining course, around a month was given to complete it. Thus, the choice of only analysisng a one set of prompts could have lead to biases such as Prompt Preference bias, Instance Verbalization bias and Sample Disparity bias in the analysis, because LLMs are generally sensitive to subtle changes in the luigistic preferences expressed through wording, verbalization etc. of prompts (Cao et al., 2022). Further research could explore simpler methods, which have been proposed to universalise the best probing criteria, when investigating factual knowledge probing (Cao et al., 2022). 


### Solutions : Mitigating bias (300 words)
A proposed way to mitigate negative impacts of prompt bias in factual knowledge extraction is by using the representation vector of prompt-only querying (Xu et al., 2024). Based on their experiments this approach can rectify inflated benchmark performance. 

Reinforcement Learning regarding the mitigation of biases is quite interesting in training LLMs. As it does not mitigate the biases, but only helps the user not gain unwanted answers. 




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
