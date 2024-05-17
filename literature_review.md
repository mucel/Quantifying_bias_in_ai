# Literature review 

#### Primary sources: 

DELPHI: Data for Evaluating LLMs’ Performance in Handling Controversial Issues
https://arxiv.org/abs/2310.18130 
This paper addressed the data set that was built for evaluating the systems performance from both the system and user perspective, by annotating controversial data. Concluding that smaller open-source models showed a concerning gap between larger (ChatGPT4). 
They used the acknowledgement rate and the comprehensiveness rate.  

Gender bias and stereotypes in Large Language Models
https://arxiv.org/pdf/2308.14921
This paper addressed the gender bias in LLMs by building on WinoBias, which is a commonly used data set. They tested 4 LLMs published in 2023 to see that their method could be generalizable, but mainly for testing gender bias. Highlighting that the models are trained on imbalanced datasets, and with Reinforced Learning they reflect those imbalances to the user.

What are the biases in my word embedding?
https://arxiv.org/pdf/1812.08769
This paper provided a Unsupervised Bias Enumerations algorithm for quantifying bias in word embedding that outputs the association tests. 

Men Also Like Shopping: Reducing Gender Bias Amplification using Corpus-level Constraints 
https://arxiv.org/pdf/1707.09457
In this paper they used comparisons of bias scores on unlabeled images to identify bias amplifications. Further, they proposed a RBA algorithm to reduce the bias amplifications.  

“I’m sorry to hear that”: Finding New Biases in Language Models with a Holistic Descriptor Dataset
https://aclanthology.org/2022.emnlp-main.625.pdf
This paper used a HolisticBias as a bias measurement to uncover new biases in LLMs that they analyzed with three measurements: token likelihoods, generation bias, and an offensiveness classifier. They identified that Holistic Bias  can detect and measure undetectable biases. 

StereoSet: Measuring stereotypical bias in pretrained language models
https://arxiv.org/pdf/2004.09456
This paper they developed a Context Association Test to measure stereotypical biases of pertain LLMs, and they evaluated it with a new metric Idealized CAT score - measuring how close a model is to an idealistic model. They used SterioSet as their dataset, finding that ChatGPT exhibits more idealistic scores than other models such as BRET etc. They also released the dataset to the public. 

Language (Technology) is Power: A Critical Survey of “Bias” in NLP  
https://aclanthology.org/2020.acl-main.485.pdf
They surveys almost 150 papers that analyzed bias in NLP, and came up wit three suggestions to analyzing bias: 
(R1) Ground work analyzing “bias” in NLP systems in the relevant literature outside of NLP that explores the relationships between language and social hierarchies. Treat representational harms as harmful in their own right. 
(R2) Provide explicit statements of why the system behaviors that are described as “bias” are harmful,l in what ways, and to whom. Be forthright about the normative reasoning (Green, 2019) underlying these statements. 
(R3) Examine language use in practice by engaging with the lived experiences of members of communities affected by NLP systems. Interrogate and reimagine the power relations between technologists and such communities. 

And some research question suggestions: 
How do social hierarchies and language ideologies infuence the decisions made during the development and deployment lifecycle? What kinds of NLP systems do these decisions result in, and what kinds do they foreclose?  General assumptions: To which linguistic norms do NLP systems adhere (Bender, 2019; Ruane et al., 2019)? Which language practices are implicitly assumed to be standard, ordinary, correct, or appropriate?  Task defnition: For which speakers are NLP systems (and NLP resources) developed? (See Joshi et al. (2020) for a discussion.) How do task defnitions discretize the world? For example, how are social groups delineated when defning demographic attribute prediction tasks (e.g., Koppel et al., 2002; Rosenthal and McKeown, 2011; Nguyen et al., 2013)? What about languages in native language prediction tasks (Tetreault et al., 2013)?  Data: How are datasets collected, preprocessed, and labeled or annotated? What are the impacts of annotation guidelines, annotator assumptions and perceptions (Olteanu et al., 2019; Sap et al., 2019; Geiger et al., 2020), and annotation aggregation processes (Pavlick and Kwiatkowski, 2019)?  Evaluation: How are NLP systems evaluated? What are the impacts of evaluation metrics (Olteanu et al., 2017)? Are any non-quantitative evaluations performed? . How do NLP systems reproduce or transform language ideologies? Which language varieties or practices come to be deemed good or bad? Might “good” language simply mean language that is easily handled by existing NLP systems? For example, linguistic phenomena arising from many language practices (Eisenstein, 2013) are described as “noisy text” and often viewed as a target for “normalization.” How do the language ideologies that are reproduced by NLP systems maintain social hierarchies? . Which representational harms are being measured or mitigated? Are these the most normatively concerning harms, or merely those that are well handled by existing algorithmic fairness techniques? Are there other representational harms that might be analyzed? 

Big Data's Disparate Impact
https://www.jstor.org/stable/24758720?sid=primo 
This more addresses the legal issues with bias in the USA, so not that useful but the abstract can provide some inspo for our abstract. Plus it addresses how data discriminates so could help decide on the marginal group. 



#### Secondary sources: 

 
https://medium.com/@arpitnarain/unmasking-bias-assessing-fairness-in-large-language-models-a722624e4483
This is for methods
