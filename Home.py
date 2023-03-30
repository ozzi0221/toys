import streamlit as st


def main():
    page_title = "TWY's Playground"
    page_icon = "📚"

    st.set_page_config(
        page_title=page_title,
        page_icon=page_icon,
        layout="centered"
    )

    st.write(f"## {page_icon} {page_title}")

    st.write(
        """
        ### What this site is for
        
        * This site is for my students and currently covers the following
          toy examples:

          - Simulation of dynamical systems described by differential
            equations
        
          - SVD (Singular Value Decomposition) and its relation
            to PCA (Principal Component Analysis)
          
          - SVD of an image file, which results in some sort of image compression
          
          - Fourier transform (of sound waves), which is an essential concept
            in signals and systems

          - Classification algorithms as an introduction to machine learning
 
          - Implementation of ChatGPT and DALL·E using their APIs.
                  
        ### How this site is written
          
        * All the pages and scripts are written in python using the Streamlit
          framework.
    
        #### What TWY does
    
        * TWY teaches engineering mathematics, signals and systems,
          technical writing, etc., at Korea University.
        
        * Lecture videos (in Korean)
        
          - [Linear Algebra](https://youtube.com/playlist?list=PLIzv0-ErbDpwNdtK1OZ7Ew54s3tlXzX4Q),
            2019
          - [Complex Functions](https://youtube.com/playlist?list=PLIzv0-ErbDpyqRVlmnLsGeC_mLmu-dU-L),
            2022
          - [Signals and Systems](https://youtube.com/playlist?list=PLIzv0-ErbDpxvwnZ3yFBLKuYP0fhDECov),
            2019
          - [Scientific and Mathematical Thinking](https://youtu.be/E1suPmxor5s),
            2022
          - [Mathematical Thinking and Writing](https://youtu.be/eqHsIbwvvrk),
            2021
          - [Science, Technology, and Gender Diversity](https://youtu.be/xUJ9e_hESG8),
            2020
          - [Foundations of Mathematics and Kurt Friedrich Gödel](https://youtu.be/RMvVxr8czTU),
            2013
        """
    )
    st.write("")

    c1, c2, c3, c4 = st.columns(4)
    c1.info('**[Email](mailto:yoon.tw@gmail.com)**', icon="✉️")
    c2.info('**[Youtube](https://www.youtube.com/@twy80)**', icon="📺")
    c3.info('**[GitHub](https://github.com/twy80)**', icon="💻")
    c4.info('**[GitHub Blog](https://twy80.github.io/)**', icon="📖")


if __name__ == "__main__":
    main()
