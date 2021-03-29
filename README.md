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

### a. SVD 

Linear combination with dimensionality reduction

- Izquierda Diario:<br>
Just one article was mislabeled

![](https://github.com/guidomitolo/pol_bias_nlp/blob/main/img/svd_izq.png)


- Derecha Diario:<br>
8 articles were hard to classify

![](https://github.com/guidomitolo/pol_bias_nlp/blob/main/img/svd_der.png)
  
  
### b. LDA (Latent Dirichlet Allocation)

Unsupervised word classification with and without tag filtering

- Izquierda Diario

All words

> [(0,
  '0.037*"dolar" + 0.013*"dolares" + 0.011*"millones" + 0.011*"banco" + 0.011*"us" + 0.010*"central" + 0.009*"deuda" + 0.009*"guzman" + 0.008*"gobierno" + 0.008*"bonos"'),<br>
 (1,
  '0.020*"precios" + 0.014*"inflacion" + 0.014*"aumento" + 0.012*"suba" + 0.010*"canasta" + 0.009*"salarios" + 0.009*"alimentos" + 0.009*"productos" + 0.008*"indec" + 0.008*"trabajadores"')]
  
Only nouns (with nltk.pos_tag)

> [(0,
  '0.065*"precios" + 0.031*"salarios" + 0.030*"alimentos" + 0.030*"productos" + 0.025*"incremento" + 0.022*"aumentos" + 0.019*"meses" + 0.019*"gobierno" + 0.018*"bebidas" + 0.017*"ingresos"'),<br>
 (1,
  '0.036*"banco" + 0.031*"deuda" + 0.030*"gobierno" + 0.027*"bonos" + 0.026*"economia" + 0.021*"medidas" + 0.019*"brecha" + 0.018*"mercado" + 0.016*"tipo" + 0.014*"presion"')]

- Derecha Diario

All words

> [(0,
  '0.011*"inflacion" + 0.009*"precios" + 0.008*"dolar" + 0.008*"gobierno" + 0.008*"mercado" + 0.007*"economia" + 0.007*"tipo" + 0.006*"aumento" + 0.005*"monetaria" + 0.004*"argentina"'),<br>
 (1,
  '0.008*"precios" + 0.008*"gobierno" + 0.008*"inflacion" + 0.007*"dolar" + 0.006*"mercado" + 0.006*"monetaria" + 0.006*"economia" + 0.005*"argentina" + 0.005*"banco" + 0.005*"pais"')]
  
Only nouns (with nltk.pos_tag)
 
> [(0,
  '0.037*"mercado" + 0.029*"tipo" + 0.029*"gobierno" + 0.025*"banco" + 0.018*"medidas" + 0.016*"brecha" + 0.016*"pais" + 0.014*"demanda" + 0.013*"economia" + 0.011*"divisas"'),<br>
 (1,
  '0.047*"precios" + 0.027*"economia" + 0.024*"gobierno" + 0.018*"nivel" + 0.014*"dinero" + 0.014*"pais" + 0.012*"indice" + 0.011*"actividad" + 0.011*"medidas" + 0.011*"dato"')]

### c. Naive Bayes

After a divided train-test split (0.75 ratio) of the vectorized (with cv) documents, the ones of Derecha Diario found more problems to be classified as those of Izquierda Diario, which were labeled with the max. accuracy.

- Derecha Diario

![](https://github.com/guidomitolo/pol_bias_nlp/blob/main/img/conf_matrix_der.png)

## 3. Versus

Bias detection per topic.

### a. Lexicon

Word comparison by Tf-Idf score according to a particular economic topic.

- Inflation

![](https://github.com/guidomitolo/pol_bias_nlp/blob/main/img/inflation_VS.png)

- Foreign Currency Exchange

![](https://github.com/guidomitolo/pol_bias_nlp/blob/main/img/exchange_VS.png)

### b. Supervised Classification

News classification by news portal (in progress)

#### b.1. Model performance per topic

- Inflation
<img src="https://github.com/guidomitolo/pol_bias_nlp/blob/main/img/inf_models.png" width="75%" height="75%">

- Exchange
<img src="https://github.com/guidomitolo/pol_bias_nlp/blob/main/img/ex_models.png" width="75%" height="75%">

