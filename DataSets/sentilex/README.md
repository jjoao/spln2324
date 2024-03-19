#  SentiLex-PT 02

SentiLex-PT is a sentiment lexicon for Portuguese, made up of 7,014 lemmas, and 82,347 inflected forms. In detail, the lexicon describes: 4,779 (16,863) adjectives, 1,081 (1,280) nouns, 489 (29,504) verbs, and 666 (34,700) idiomatic expressions.

The sentiment entries correspond to human predicates, i.e. predicates modifying human nouns, compiled from different publicly available resources (corpora and dictionaries).

SentiLex-PT is especially useful for opinion mining applications involving Portuguese, in particular for detecting and classifying sentiments and opinions targeting human entities.

The sentiment attributes for each entry are: the target of sentiment, the predicate polarity, and the polarity assignment.

Sentiment attributes were mostly manually labeled, but some entries (adjectives) have their attributes automatically assigned by software developed for this purpose. The inflected forms associated with the verbs and idiomatic expressions, and their corresponding morphological attributes, were semi-automatically extracted from LABEL-LEX, a publicly available lexicon for Portuguese, developed by Ranchhod et al. (1999), at LabEL.

SentiLex-PT is available in two separate .txt files:

SentiLex-lem-PT02.txt Each line includes information about: Lemma (conventionally, the masculine singular form for adjectives, the singular form for nouns that are inflected for number, and the infinitive form for verbs and idiomatic expressions), Part-of-speech (ADJ(ective), N(oun), V(erb) and IDIOM), and Sentiment attributes: Polarity (POL), which can be positive (1), negative (-1) or neutral (0); Target of polarity (TG), which corresponds to a human noun (HUM), functioning as the subject (N0) and/or the complement (N1) of the predicate; Polarity annotation (ANOT), which was performed manually (MAN) or automatically, by the Judgment Analysis Lexicon Classifier (JALC) tool, developed by the project team. Some entries also include an additional code (REV), which refers to specific notes included by the annotator. At this point, we can find the following notations: REV=AMB, which means that the entry is ambiguous with other words conveying different polarities, and REV:POL, which means that the polarity code previously assigned to the entry in SentiLex-PT01 was revised.

Below are five entries of SentiLex-lem-PT02.txt: aberração.PoS=N;TG=HUM:N0;POL:N0=-1;ANOT=MAN bonito.PoS=Adj;TG=HUM:N0;POL:N0=1;ANOT=MAN castigado;PoS=Adj;TG=HUM:N0;POL:N0=-1;ANOT=JALC estimado.PoS=Adj;TG=HUM:N0;POL:N0=1;ANOT=JALC;REV=AMB enganar.PoS=V;TG=HUM:N0:N1;POL:N0=-1;POL:N1=0;ANOT=MAN engolir em seco.PoS=IDIOM;TG=HUM:N0;POL:N0=-1;ANOT=MAN

SentiLex-flex-PT02.txt In each line, the inflected forms are associated with their corresponding lemma. In addition to the linguistic information described in dictionary of lemmas, each adjective and noun is classified according to their inflection (FLEX) in gender (masculine (m) or feminine (f)) and number (singular (s) or plural (p)). The morphological attributes characterizing verbs and idiomatic expressions correspond to tense, person and number. The inflected forms and corresponding attributes were automatically extracted from LABEL-LEX-sw.

Below are ten entries of SentiLex-flex-PT02.txt: aberração,aberração.PoS=N;FLEX=fs;TG=HUM:N0;POL:N0=-1;ANOT=MAN bonita,bonito.PoS=Adj;FLEX=fs;TG=HUM:N0;POL:N0=1;ANOT=MAN bonitas,bonito.PoS=Adj;FLEX=fp;TG=HUM:N0;POL:N0=1;ANOT=MAN bonito,bonito.PoS=Adj;FLEX=ms;TG=HUM:N0;POL:N0=1;ANOT=MAN bonitos,bonito.PoS=Adj;FLEX=mp;TG=HUM:N0;POL:N0=1;ANOT=MAN engoliste em seco,engolir em seco.PoS=IDIOM;Flex=J2p|J2s;TG=HUM:N0;POL:N0=-1;ANOT=MAN engolistes em seco,engolir em seco.PoS=IDIOM;Flex=J2p;TG=HUM:N0;POL:N0=-1;ANOT=MAN engoliu em seco,engolir em seco.PoS=IDIOM;Flex=J4s|P3s;TG=HUM:N0;POL:N0=-1;ANOT=MAN engulam em seco,engolir em seco.PoS=IDIOM;Flex=Y4p|S4p|S3p;TG=HUM:N0;POL:N0=-1;ANOT=MAN engulamos em seco,engolir em seco.PoS=IDIOM;Flex=Y1p|S1p;TG=HUM:N0;POL:N0=-1;ANOT=MAN

Mário J. Silva, Paula Carvalho and Luís Sarmento. "Building a Sentiment Lexicon for Social Judgement Mining". In Lecture Notes in Computer Science (LNCS) / Lecture Notes in Artificial Intelligence (LNAI), International Conference on Computational Processing of Portuguese (PROPOR), 17-20 April, 2012, Coimbra.

    B2SHARE Lexicon Sentiment Analysis 

Identifier
PID 	http://hdl.handle.net/11304/5a460083-d21a-4d12-89d8-b90f62eb5f3a
Metadata Access 	https://b2share.eudat.eu/api/oai2d?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:b2share.eudat.eu:b2rec/93ab120efdaa4662baec6adee8e7585f
Provenance
Creator 	Carvalho, Paula; Silva, Mário J
Publisher 	CLARIN
Publication Year 	2017
Rights 	info:eu-repo/semantics/openAccess; Creative Commons Attribution (CC-BY)
OpenAccess 	true
Representation
Discipline 	Linguistics
