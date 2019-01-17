# music-genre-classification


# Project Abstract

Automated personalization is a growing goal of the music industry as music libraries are now almost entirely digital as most consumers listen to their music through streaming services like Spotify, Pandora and iTunes. To improve user experience, identifying the genre of a new song can be useful in matching it to users’ preferences. In this work, we examine several classification algorithms to determine the genre for songs from the Million Song Dataset (MSD) using genre labels extracted from the last.fm dataset for ground truth labels. To create the feature sets, we selected relevant quantitative features from the MSD and used time-series feature extraction techniques to reduce the multidimensional features. We then applied principal component analysis (PCA) to the entire set and selected the components which explained the most variance. We tuned and tested several models, as well as ensembles of these models, on this feature set and examined the accuracy of each. We also scraped lyrics from several public websites and applied natural language processing methods in order to classify songs based on lyrics.
Our analysis using the main MSD dataset yielded promising results of 46% overall accuracy using a Multi-Layer Perceptron (MLP) for classification of 6 genres. Models trained on lyrical data were less enlightening, achieving 25% overall accuracy over 4 genres. We surmise that the limited availability of lyrical data, similarities in genre, lack of colloquial vocabulary in the word model, and overlapping lyrical terms hindered performance of genre prediction with lyrics. 
