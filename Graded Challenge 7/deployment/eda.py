import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def run():
    st.title('Exploratory Data Analytics')
    st.write('## Ahmad Qais Alfiansyah')
    st.write("### Graded Challenge 7")

    color_codes = [
        '#1d3d71ff',
        '#f26634ff',
        '#b19802ff',
        '#56a3a6ff',
        '#80a4edff',
        '#1be7ffff',
        '#df57bcff',
        '#496f5dff',
        '#88a0a8ff',
        '#00c49aff']
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Load Data
    st.markdown("<h2 style='text-align:center;'>Data Sebelum Pre-processing</h2>", unsafe_allow_html=True)
    df= pd.read_table('https://s.id/tsv_gc7')
    eda_df_2= pd.read_csv('https://s.id/eda_gc7')
    df = df.drop(df.index[473])
    df = df.drop_duplicates()
    df['verified_reviews'] = df['verified_reviews'].str.strip()
    df = df[df['verified_reviews'] != '']
    df = df.reset_index(drop=True)
    eda_df= df.copy()
    eda_df['feedback_string']= eda_df['feedback'].map({0: 'Negative', 1: 'Positive'})  

    st.markdown("<h3 style='text-align:center;'>Analisa Rating</h3>", unsafe_allow_html=True)
    variations = df['variation'].unique()

    fig, axes = plt.subplots(4, 4, figsize=(20, 17)) 

    for i, variation in enumerate(variations):
        row = i // 4
        col = i % 4
        ax = axes[row, col]
        data_filtered = df[df['variation'] == variation]
        sns.countplot(x='rating', data=data_filtered, ax=ax, color=color_codes[i % len(color_codes)])
        ax.set_title(f'Rating for {variation}', fontsize=16)
        ax.set_xlabel('Rating')
        ax.set_ylabel('Count')

    plt.tight_layout()
    plt.show()

    st.pyplot(fig)

    mean_ratings = df.groupby('variation')['rating'].mean().sort_values(ascending=False).index

    plt.figure(figsize=(11, 7))
    sns.barplot(x='rating', y='variation', data=df, order=mean_ratings, hue='variation')
    plt.title('Average Rating for Each Product Variations', fontsize=16)
    plt.xlabel('Average Rating', fontsize=14)
    plt.ylabel('Variation', fontsize=14)
    plt.tight_layout()
    plt.show()
    st.pyplot()

    st.markdown("<h3 style='text-align:center;'>Analisa Feedback</h3>", unsafe_allow_html=True)

    color = [color_codes[0], color_codes[1]]
    target= eda_df['feedback_string'].value_counts()
    labels = [f'{index}\n({(val / sum(target)) * 100:.1f}%, Total: {val})' for index, val in zip(target.index, target)]
    plt.pie(target, labels=labels, startangle=350, colors=color, textprops={'fontsize': 7}, explode= [0.1,0.1], shadow=True)
    plt.title('Perbandingan Customer Feedback', fontsize=12)
    plt.tight_layout()
    st.pyplot()

    variations = eda_df['variation'].unique()
    color = [color_codes[0], color_codes[1]]
    fig, axes = plt.subplots(4, 4, figsize=(10, 10))
    fig.suptitle('Customer Feedback per Each Variation\n', fontsize=24, ha='center')

    for i, variation in enumerate(variations):
        row = i // 4
        col = i % 4
        ax = axes[row, col]
        data_filtered = eda_df[eda_df['variation'] == variation]
        class_counts = data_filtered['feedback_string'].value_counts()
        labels = [f'{index}\n({(val / sum(class_counts)) * 100:.1f}%, Total: {val})' for index, val in zip(class_counts.index, class_counts)]
        sizes = class_counts.values
        ax.pie(sizes, labels=labels, startangle=140, colors=color, textprops={'fontsize': 7})
        ax.set_title(f'Variation {variation}', fontsize=10)
        ax.axis('equal')

    plt.tight_layout()
    st.pyplot()

    eda_df['reviews_char'] = eda_df['verified_reviews'].apply(len)
    min_char_df1 = eda_df['reviews_char'].min()
    max_char_df1 = eda_df['reviews_char'].max()
    shortest_review_df1 = eda_df[eda_df['reviews_char'] == min_char_df1]
    longest_review_df1 = eda_df[eda_df['reviews_char'] == max_char_df1]
    mean_char_df1 = eda_df['reviews_char'].mean()

    def word_count(string):
        words = string.split()
        return len(words)
    
    eda_df['reviews_word'] = eda_df['verified_reviews'].apply(word_count)
    
    min_word_df1 = eda_df['reviews_word'].min()
    max_word_df1 = eda_df['reviews_word'].max()
    shortest_word_df1 = eda_df[eda_df['reviews_word'] == min_word_df1]
    longest_word_df1 = eda_df[eda_df['reviews_word'] == max_word_df1]
    mean_word_df1 = eda_df['reviews_word'].mean()

    st.markdown("<h3 style='text-align:center;'>Word Cloud Before Pre-Processing</h3>", unsafe_allow_html=True)
    
    reviews_word = ' '.join(eda_df['verified_reviews'].dropna())
    cloud_reviews = WordCloud().generate(reviews_word)

    contour_color = color_codes[0]  
    palette = color_codes  
    
    plt.figure(figsize=(10, 5))
    plt.imshow(cloud_reviews, interpolation='bilinear')
    
    plt.axis('off')
    plt.show()

    st.pyplot()

    st.markdown("<h2 style='text-align:center;'>Analasia After Pre-Processing</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Analasia Karakter</h3>", unsafe_allow_html=True)
    eda_df_2['reviews_char'] = eda_df_2['p_verified_reviews'].apply(len)
    min_char_df2 = eda_df_2['reviews_char'].min()
    max_char_df2 = eda_df_2['reviews_char'].max()
    shortest_review_df2 = eda_df_2[eda_df_2['reviews_char'] == min_char_df2]
    longest_review_df2 = eda_df_2[eda_df_2['reviews_char'] == max_char_df2]
    mean_char_df2 = eda_df_2['reviews_char'].mean()

    eda_df_2['reviews_word'] = eda_df_2['p_verified_reviews'].apply(word_count)
    min_word_df2 = eda_df_2['reviews_word'].min()
    max_word_df2 = eda_df_2['reviews_word'].max()
    shortest_word_df2 = eda_df_2[eda_df_2['reviews_word'] == min_word_df2]
    longest_word_df2 = eda_df_2[eda_df_2['reviews_word'] == max_word_df2]
    mean_word_df2 = eda_df_2['reviews_word'].mean()

    data = [
        [min_char_df1, min_char_df2],
        [max_char_df1, max_char_df2],
        [mean_char_df1, mean_char_df2]
    ]
    
    titles = ['Min Character', 'Max Character', 'Mean Character']
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))  
    
    for i in range(3):
        bars = axes[0, i].bar(['Pre-Processing', 'After Processing'], data[i], color=color_codes)
        axes[0, i].set_title(titles[i])
        for bar in bars:
            height = bar.get_height()
            axes[0, i].text(bar.get_x() + bar.get_width() / 2., height, f'{height}', ha='center', va='bottom')
    
    data_word = [
        [min_word_df1, min_word_df2],
        [max_word_df1, max_word_df2],
        [mean_word_df1, mean_word_df2]
    ]
    
    titles_word = ['Min Word', 'Max Word', 'Mean Word']
    for i in range(3):
        bars_word = axes[1, i].bar(['Pre-Processing', 'After Processing'], data_word[i], color=color_codes)
        axes[1, i].set_title(titles_word[i])
        for bar in bars_word:
            height = bar.get_height()
            axes[1, i].text(bar.get_x() + bar.get_width() / 2., height, f'{height}', ha='center', va='bottom')
    
    fig.suptitle('Comparison of Text Characteristics Before and After Processing', fontsize=16)
    for ax in axes.flat:
        ax.set_ylabel('Count')
        ax.set_xlabel('Stage')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
    st.pyplot(fig)

    reviews_word = ' '.join(eda_df_2['p_verified_reviews'].dropna())
    cloud_reviews = WordCloud().generate(reviews_word)
    contour_color = color_codes[0] 
    palette = color_codes 
    
    plt.figure(figsize=(10, 5))
    plt.imshow(cloud_reviews, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    st.pyplot()




if __name__ == '__main__':
    run()