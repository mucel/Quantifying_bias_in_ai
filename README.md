# Quantifying bias in AI 
By Māra Učelniece, Michalina Loch, Ralfs Brutāns. 


#### Abstract

Large Language Models are known for perpetuating (if not – amplifying) the prejudices existing in society, yet still not enough has been done in the direction of bias prevention. Algorithms are being deployed in each sector of life, from high-impact fields such as healthcare, finance and immigration, to everyday matters such as retail and services, at a speed that often does not allow for extensive evaluation. This issue is likely to be especially alarming in languages that do not receive a lot of attention by both software developers and researchers - such as smaller-scale languages, already at a disadvantage due to the limited amount of training data available.

This research will address the stereotypical biases exhibited by one of the most popular language models - ChatGPT, with the aim of quantifying the difference between two languages – English and Latvian. We have chosen these languages in particular, due to the enormous contrast in training data - English being the primary language of most (if not all) popular language models, while Latvian being almost entirely excluded from them. Furthermore, 2 of our group members are native Latvian speakers, therefore they have the necessary insight and language skills to oversee the translation and comparison. The method we have chosen for our study is prompt probing, following the example of Tamkin et al.(2023), thanks to its feasibility within our time and skillset. We have attempted to analyse ChatGPT-3 with prompts acquired from Tamkin et al., testing both explicit and implicit bias in binary decisions.


#### Research questions 
> To what extent does ChatGPT3.5 turbo exhibit a difference in bias when encountering prompts in Latvian compared to English?

#### Dataset
+ Prompts:
    + [Tamkin et al. (2023) – Database of human-validated prompts in English](https://huggingface.co/datasets/Anthropic/discrim-eval)

+ Large Language Model:
    + ChatGPT3.5 Turbo 0125 (+OpenAI API tools)

#### A tentative list of milestones for the project
Add here a sketch of your planning for the coming weeks. Please mention who does what.

- [x] Explore current research + possible data sets (Mara) 
- [x] Decide on a method (all)
- [x] Find a study to base ourselves on an open-source data set (Michalina)
- [x] Translate to Latvian with Google API (Ralfs)
- [x] Do the model prompting with OpenAI API (Ralfs)
- [x] Work on the report (Mara + Michalina)
- [x] Documenting the steps along the way (all)
- [x] Evaluation of obtained bias (Ralfs)
- [x] Explanation/ summarizing the impact of bias in a report (all)
- [x] Relation to our (main) research question(s) (all)
additionally
- [x] code the report into Latex (Michalina)

##### Author contributions to the report:
* Mara: Abstract, introduction, theoretical background, discussion
* Michalina: Abstract, introduction, methodology, conclusion
* Ralfs: Results, analysis and all the visual aids (plots)



#### Documentation
This repository contains the documentation for a Text Mining project conducted by AUC students in 2024. It is organized into several folders, each clearly labeled to indicate its essential content, making navigation intuitive and straightforward.

