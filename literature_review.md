 
# Literature review

##### Main source for replication: 
Evaluating and Mitigating Discrimination in Language Model Decisions
https://arxiv.org/pdf/2312.03689 
....

#### Primary sources:

StereoSet: Measuring stereotypical bias in pretrained language models
https://arxiv.org/pdf/2004.09456        
sThis paper they developed a Context Association Test to measure stereotypical biases of pertain LLMs, and they evaluated it with a new metric Idealized CAT score - measuring how close a model is to an idealistic model. They used SterioSet as their dataset, finding that ChatGPT exhibits more idealistic scores than other models such as BRET etc. They also released the dataset to the public.


Language (Technology) is Power: A Critical Survey of “Bias” in NLP  
https://aclanthology.org/2020.acl-main.485.pdf  
They surveys almost 150 papers that analysed bias in NLP, and came up wit three suggestions to analysing bias:
(R1) Ground work analysing “bias” in NLP systems in the relevant literature outside of NLP that explores the relationships between language and social hierarchies. Treat representational harms as harmful in their own right.
(R2) Provide explicit statements of why the system behaviours that are described as “bias” are harmful,l in what ways, and to whom. Be forthright about the normative reasoning (Green, 2019) underlying these statements.
(R3) Examine language use in practice by engaging with the lived experiences of members of communities affected by NLP systems. Interrogate and reimagine the power relations between technologists and such communities.


And some research question suggestions:
How do social hierarchies and language ideologies influence the decisions made during the development and deployment lifecycle? What kinds of NLP systems do these decisions result in, and what kinds do they foreclose?  General assumptions: To which linguistic norms do NLP systems adhere (Bender, 2019; Ruane et al., 2019)? Which language practices are implicitly assumed to be standard, ordinary, correct, or appropriate?  Task definition: For which speakers are NLP systems (and NLP resources) developed? (See Joshi et al. (2020) for a discussion.) How do task definitions discretize the world? For example, how are social groups delineated when defining demographic attribute prediction tasks (e.g., Koppel et al., 2002; Rosenthal and McKeown, 2011; Nguyen et al., 2013)? What about languages in native language prediction tasks (Tetreault et al., 2013)?  Data: How are datasets collected, preprocessed, and labeled or annotated? What are the impacts of annotation guidelines, annotator assumptions and perceptions (Olteanu et al., 2019; Sap et al., 2019; Geiger et al., 2020), and annotation aggregation processes (Pavlick and Kwiatkowski, 2019)?  Evaluation: How are NLP systems evaluated? What are the impacts of evaluation metrics (Olteanu et al., 2017)? Are any non-quantitative evaluations performed? . How do NLP systems reproduce or transform language ideologies? Which language varieties or practices come to be deemed good or bad? Might “good” language simply mean language that is easily handled by existing NLP systems? For example, linguistic phenomena arising from many language practices (Eisenstein, 2013) are described as “noisy text” and often viewed as a target for “normalization.” How do the language ideologies that are reproduced by NLP systems maintain social hierarchies? . Which representational harms are being measured or mitigated? Are these the most normatively concerning harms, or merely those that are well handled by existing algorithmic fairness techniques? Are there other representational harms that might be analysed?


Take Care of Your Prompt Bias! Investigating and Mitigating Prompt
Bias in Factual Knowledge Extraction
https://arxiv.org/pdf/2403.09963v1
This paper is about investigating and mitigating prompt bias in factual knowledge tasks leading to overfitting in LLMs. It proposed debiasing through a representation-based method effectively improves benchmark accuracy by mitigating prompt bias. Focusing on the importance of addressing bias for performance enhancement.

Can Prompt Probe Pretrained Language Models? Understanding the
Invisible Risks from a Causal View
https://arxiv.org/pdf/2203.12258
This paper assessed biases that relate to prompt probing suggesting a causal analysis framework and a focus on theoretical not empirical analyses are better to reduce them. They also suggested that the distinction between what one is investigating is essential to the analysis.  

Probing via Prompting
https://aclanthology.org/2022.naacl-main.84.pdf
This paper proposed a new model-free approach to use probing as a prompting task, as to not analyse what the model learns through probing after conducting an empirical experiment to show that the properties are encoded. Suggesting that these model-free methods are useful for identifying embedded linguistic properties. 

Manual Prompt Generation For Language Model Probing
https://ceur-ws.org/Vol-3274/paper6.pdf 
This paper 


##### Not that useful for prompt probing :


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
In this paper they used comparisons of bias scores on unlaabeled images to identify bias amplifications. Further, they proposed a RBA algorithm to reduce the bias amplifications.  


“I’m sorry to hear that”: Finding New Biases in Language Models with a Holistic Descriptor Dataset
https://aclanthology.org/2022.emnlp-main.625.pdf  
This paper used a HolisticBias as a bias measurement to uncover new biases in LLMs that they analyzed with three measurements: token likelihoods, generation bias, and an offensiveness classifier. They identified that Holistic Bias can detect and measure undetectable biases.


Big Data's Disparate Impact
https://www.jstor.org/stable/24758720?sid=primo  
This more addresses the legal issues with bias in the USA, so not that useful but the abstract can provide some inspo for our abstract. Plus it addresses how data discriminates so could help decide on the marginal group.


Towards detecting unanticipated bias in Large Language Models
https://arxiv.org/pdf/2404.02650  
This paper discussed an Uncertainty and an Explainability research methods to discover unanticipated biases in internal decision making processes of LLMs (nit analysing training data). They porvided a comprehensive analysis of various methods that could be used for this.




----------------------------------------------------------------------

Su Lin Blodgett, Gilsinia Lopez, Alexandra Olteanu, Robert Sim, and Hanna Wallach. 2021. Stereotyping Norwegian Salmon: An Inventory of
Pitfalls in Fairness Benchmark Datasets. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th
International Joint Conference on Natural Language Processing (Volume 1: Long Papers), Chengqing Zong, Fei Xia, Wenjie Li, and Roberto Navigli
(Eds.). Association for Computational Linguistics, Online, 1004–1015. https://doi.org/10.18653/v1/2021.acl-long.81



Aylin Caliskan, Joanna J Bryson, and Arvind Narayanan. 2017. Semantics derived automatically from language corpora contain human-like biases.
Science 356, 6334 (2017), 183–186. https://doi.org/10.1126/science.aal4230


Isabel O. Gallegos, Ryan A. Rossi, Joe Barrow, Md Mehrab Tanjim, Sungchul Kim, Franck Dernoncourt, Tong Yu, Ruiyi Zhang, and Nesreen K.
Ahmed. 2023. Bias and Fairness in Large Language Models: A Survey. arXiv preprint arXiv:2309.00770 (2023).


Scott M. Lundberg and Su-In Lee. 2017. A unified approach to interpreting model predictions. In Advances in Neural Information Processing Systems,
Vol. 30. Curran Associates, Inc

-------------------------------------------------------------------

#### Secondary sources:


Factual Knowledge Probing in Pretrained Language Models
https://lukovnikov.medium.com/factual-knowledge-probing-in-pretrained-language-models-4c52f6c79fc3
X-FACTR: Multilingual Factual Knowledge Retrieval from PLM (Jiang et al. 2020): this paper addressed accuracy in various different languages, impacts on factual knowledge and the overlaps between language. Showing that English has a higher accuracy on new tasks.


Unmasking Bias —Assessing Fairness in Large Language Models
https://medium.com/@arpitnarain/unmasking-bias-assessing-fairness-in-large-language-models-a722624e4483
This article discussed three main methodologies for testing fairness. The first one is Bias Audit, which involves testing LLMs across varying demographic groups with calculating metrics regarding the errors. The second one is Counterfactual Testing, which involves changing the demographic information to see if there are variations in the outputs. The last one is Adversarial Testing, which involves tricking the models into reviling biases. This article also adresess the steps of how each approach can be done. Nonetheless, it suggest that one should use all methods to reduce the evaluators bias in testing the bias of the model.


Decoding LLM Performance: A Guide to Evaluating LLM Applications
https://medium.com/@amagastya/decoding-llm-performance-a-guide-to-evaluating-llm-applications-e8d7939cafce
This article discussed how the evaluation of NLP has shaped our understanding of the LLMs, with a great visual timeline of the metrics, with also addressing their limitations. It also beautifully showed the evaluation methods that can be used in the image below.
![Evaluation methods](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*WeX8kL9rzziiZaL4)
*"The tools we create to understand and generate language are simultaneously becoming the yardstick by which we measure their progress."*
It also indicated some limitations to these assisted evaluations. as they also might create (position, verbose, self-affinity) biases. Furthermore, they provide a guide to evaluating LLM applications. They concluded that the methods are still developing parallel to the developments in the models, so one can refine them as necessary.






