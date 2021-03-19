# Understanding Political Bias with NLP

Looking for the key features of speech parciality in two partisan news portal of Argentina.

## 1. Dataset

Self-built from scrapping, using bs4 and selenium, targeted to gather news about local economy.

Site|Num. of Articles
--|--
"Izquierda Diario"|1032
"Derecha Diario"|339

## 2. Topic selection and modeling

Before making any comparison between sites, we decided to narrow, according to each article's title, the topics scope to the two most popular in Argentina.

Topic|Site|Num. of Articles
--|--|--
Inflation|"Izquierda Diario"|39
Currency Exchange|"Izquierda Diario"|26
--|--|--
Inflation|"Derecha Diario"|42
Currency Exchange|"Derecha Diario"|30

To check the coherence of this selection, we made a series of tests on a vectorized (with cv and tfidf) bag of words.

#### a. SVD (linear combination with dimensionality reduction)

- Izquierda Diario:<br>
Just one article was mislabeled

![](https://github.com/guidomitolo/pol_bias_nlp/blob/main/img/svd_izq.png)


- Derecha Diario:<br>
8 articles were hard to classify

![](https://github.com/guidomitolo/pol_bias_nlp/blob/main/img/svd_der.png)
  
  
#### b. LDA (Latent Dirichlet Allocation), with and without tag filtering (to keep only nouns)

- Izquierda Diario

> [(0,
  '0.034*"dolar" + 0.012*"dolares" + 0.011*"millones" + 0.010*"banco" + 0.010*"us" + 0.009*"central" + 0.008*"deuda" + 0.008*"guzman" + 0.008*"oficial" + 0.008*"gobierno"'),
 (1,
  '0.020*"precios" + 0.014*"inflacion" + 0.013*"aumento" + 0.012*"suba" + 0.011*"canasta" + 0.010*"alimentos" + 0.010*"productos" + 0.009*"salarios" + 0.009*"indec" + 0.008*"trabajadores"')

- Derecha Diario

> [(0,
  '0.011*"inflacion" + 0.009*"precios" + 0.008*"dolar" + 0.008*"gobierno" + 0.008*"mercado" + 0.007*"economia" + 0.007*"tipo" + 0.006*"aumento" + 0.005*"monetaria" + 0.004*"argentina"'),
 (1,
  '0.008*"precios" + 0.008*"gobierno" + 0.008*"inflacion" + 0.007*"dolar" + 0.006*"mercado" + 0.006*"monetaria" + 0.006*"economia" + 0.005*"argentina" + 0.005*"banco" + 0.005*"pais"')]

#### c. Naive Bayes

After a divided train-test split (0.75 ratio) of the vectorized (with cv) documents, the ones of Derecha Diario found more problems to be classified as those of Izquierda Diario, which were labeled with the max. accuracy.

- Derecha Diario

![](https://github.com/guidomitolo/pol_bias_nlp/blob/main/img/conf_matrix_der.png)

## 3. Versus

Word comparison by Tf-Idf score according to a particular economic topic.

#### a. Lexicon

- Inflation

Izquierda Diario VS Derecha Diario

![](https://github.com/guidomitolo/pol_bias_nlp/blob/main/img/inflation_VS.png)

- Foreign Currency Exchange

Izquierda Diario VS Derecha Diario

![](https://github.com/guidomitolo/pol_bias_nlp/blob/main/img/exchange_VS.png)

#### b. Supervised Classification

(in progress)

